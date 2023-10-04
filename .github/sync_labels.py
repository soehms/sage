#!/usr/bin/python
# -*- coding: utf-8 -*-

r"""
Python script to sync status and priority labels.
For more information see https://github.com/sagemath/sage/pull/35172
"""

##############################################################################
#       Copyright (C) 2023 Sebastian Oehms <seb.oehms@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
##############################################################################

import os
import sys
from logging import info, warning, debug, getLogger, INFO, DEBUG, WARNING
from json import loads
from enum import Enum
from datetime import datetime, timedelta
from subprocess import check_output, CalledProcessError

datetime_format = '%Y-%m-%dT%H:%M:%SZ'
default_bot = 'github-actions'


class Action(Enum):
    r"""
    Enum for GitHub event ``action``.
    """
    opened = 'opened'
    reopened = 'reopened'
    closed = 'closed'
    labeled = 'labeled'
    unlabeled = 'unlabeled'
    ready_for_review = 'ready_for_review'
    synchronize = 'synchronize'
    review_requested = 'review_requested'
    converted_to_draft = 'converted_to_draft'
    submitted = 'submitted'

class AuthorAssociation(Enum):
    r"""
    Enum for GitHub ``authorAssociation``.
    """
    def is_valid(self):
        r"""
        Return whether ``self`` has valid permissions.
        """
        c = self.__class__
        return self in [c.collaborator, c.member, c.owner]

    collaborator = 'COLLABORATOR' # Author has been invited to collaborate on the repository.
    contributor = 'CONTRIBUTOR' # Author has previously committed to the repository.
    first_timer = 'FIRST_TIMER' # Author has not previously committed to GitHub.
    first_time_contributor = 'FIRST_TIME_CONTRIBUTOR' # Author has not previously committed to the repository.
    mannequin = 'MANNEQUIN' # Author is a placeholder for an unclaimed user.
    member = 'MEMBER' # Author is a member of the organization that owns the repository.
    none = 'NONE' # Author has no association with the repository.
    owner = 'OWNER' # Author is the owner of the repository.

class RevState(Enum):
    r"""
    Enum for GitHub event ``review_state``.
    """
    commented = 'COMMENTED'
    changes_requested = 'CHANGES_REQUESTED'
    approved = 'APPROVED'

class Priority(Enum):
    r"""
    Enum for priority labels.
    """
    blocker = 'p: blocker /1'
    critical = 'p: critical /2'
    major = 'p: major /3'
    minor = 'p: minor /4'
    trivial = 'p: trivial /5'

class State(Enum):
    r"""
    Enum for state labels.
    """
    positive_review = 's: positive review'
    needs_work = 's: needs work'
    needs_review = 's: needs review'
    needs_info = 's: needs info'

class Resolution(Enum):
    r"""
    Enum for resolution labels.
    """
    duplicate = 'r: duplicate'
    invalid = 'r: invalid'
    wontfix = 'r: wontfix'
    worksforme = 'r: worksforme'

def selection_list(label):
    r"""
    Return the selection list to which ``label`` belongs to.
    """
    for sel_list in [Priority, State, Resolution]:
        for item in sel_list:
            if label == item.value:
                return sel_list
    return None

class GhLabelSynchronizer:
    r"""
    Handler for access to GitHub issue via the ``gh`` in the bash command line
    of the GitHub runner.
    """
    def __init__(self, url, actor):
        r"""
        Python constructor sets the issue / PR url and list of active labels.
        """
        self._url = url
        self._actor = actor
        self._warning_prefix = 'Label Sync Warning:'
        self._hint_prefix = 'Label Sync Hint:'
        self._labels = None
        self._author = None
        self._draft = None
        self._open = None
        self._review_decision = None
        self._reviews = None
        self._commits = None
        self._commit_date = None
        self._bot_login = None

        number = os.path.basename(url)
        self._pr = True
        self._issue = 'pull request #%s' % number
        if url.rfind('issue') != -1:
            self._issue = 'issue #%s' % number
            self._pr = False
        info('Create label handler for %s and actor %s' % (self._issue, self._actor))
        self.bot_login()
        self.clean_warnings()

    # -------------------------------------------------------------------------
    # methods to obtain properties of the issue
    # -------------------------------------------------------------------------
    def is_pull_request(self):
        r"""
        Return if we are treating a pull request.
        """
        return self._pr

    def reset_view(self):
        r"""
        Reset cache of ``gh view`` results. 
        """
        self._labels = None
        self._author = None
        self._draft = None
        self._open = None
        self._review_decision = None
        self._reviews = None
        self._commits = None
        self._commit_date = None

    def rest_api(self, path_args, method=None, query=''):
        r"""
        Return data obtained from ``gh`` command ``api``.
        """
        meth = '-X GET'
        if method:
            meth='-X %s' % method
        cmd = 'gh api %s -H \"Accept: application/vnd.github+json\" %s %s' % (meth, path_args, query)
        debug('Execute command: %s' % cmd)
        if method:
            return check_output(cmd, shell=True)
        return loads(check_output(cmd, shell=True))

    def view(self, key):
        r"""
        Return data obtained from ``gh`` command ``view``.
        """
        issue = 'issue'
        if self._pr:
            issue = 'pr'
        cmd = 'gh %s view %s --json %s' % (issue, self._url, key)
        debug('Execute command: %s' % cmd)
        return loads(check_output(cmd, shell=True))[key]

    def is_open(self):
        r"""
        Return ``True`` if the issue res. PR is open.
        """
        if self._open is not None:
            return self._open
        if self.view('state') == 'OPEN':
            self._open = True
        else:
            self._open = False
        info('Issue %s is open %s' % (self._issue, self._open))
        return self._open

    def is_draft(self):
        r"""
        Return ``True`` if the PR is a draft.
        """
        if self._draft is not None:
            return self._draft
        if self.is_pull_request():
            self._draft = self.view('isDraft')
        else:
            self._draft = False
        info('Issue %s is draft %s' % (self._issue, self._draft))
        return self._draft

    def bot_login(self):
        r"""
        Return the login name of the bot.
        """
        if self._bot_login:
            return self._bot_login
        cmd = 'gh auth status'
        from subprocess import run
        capt = run(cmd, shell=True, capture_output=True)
        l = str(capt.stderr).split()
        if not 'as' in l:
            l = str(capt.stdout).split()
        self._bot_login = l[l.index('as')+1]
        if self._bot_login.endswith('[bot]'):
            self._bot_login = self._bot_login.split('[bot]')[0]
        info('Bot is %s' % self._bot_login)
        return self._bot_login

    def is_this_bot(self, login):
        r"""
        Check whether login is the bot itself.
        """
        return login.startswith(self.bot_login())

    def is_auth_team_member(self, login):
        r"""
        Return ``True`` if the user with given login belongs to an authorized
        team.
        """
        def verify_membership(team):
            path_args = '/orgs/sagemath/teams/%s/memberships/%s' % (team, login)
            try:
                res = self.rest_api(path_args)
                if res['state'] == 'active' and res['role'] == 'member':
                    info('User %s is a member of %s' % (login, team))
                    return True
            except CalledProcessError:
                pass

            info('User %s is not a member of %s' % (login, team))
            return False

        # check for the Triage team
        if verify_membership('triage'):
            return True

        return False

    def actor_authorized(self):
        r"""
        Return ``True`` if the actor has sufficient permissions.
        """
        if self.is_this_bot(default_bot):
            # since the default bot is not a member of the SageMath
            # organization it cannot test membership for private members.
            # Therefore, we check here for public organization membership.
            rev = self.get_latest_review()
            if not rev:
                return False

            if rev['author']['login'] == self._actor:
                ass = rev['authorAssociation']
                info('Actor %s has association %s' % (self._actor, ass))
                return AuthorAssociation(ass).is_valid()
            info('Actor %s did not create latest review' % self._actor)
            return False
        else:
            return self.is_auth_team_member(self._actor)

    def clean_warnings(self):
        r"""
        Remove all warnings that have been posted by ``GhLabelSynchronizer``
        more than ``warning_lifetime`` ago.
        """
        warning_lifetime = timedelta(minutes=5)
        time_frame = timedelta(minutes=730) # timedelta to search for comments including 10 minutes overlap with cron-cycle
        per_page = 100
        today = datetime.today()
        since = today - time_frame
        query = '-F per_page=%s -F page={} -f since=%s' % (per_page, since.strftime(datetime_format))
        s = self._url.split('/')
        owner = s[3]
        repo = s[4]
        path_args = '/repos/%s/%s/issues/comments' % (owner, repo)
        page = 1
        comments = []
        while True:
            comments_page = self.rest_api(path_args, query=query.format(page))
            comments += comments_page
            if len(comments_page) < per_page:
                break
            page += 1

        info('Cleaning warning comments since %s (total found %s)' % (since, len(comments)))

        for c in comments:
            login = c['user']['login']
            body = c['body']
            comment_id = c['id']
            issue = c['issue_url'].split('/').pop()
            created_at = c['created_at']
            if self.is_this_bot(login):
                debug('%s comment %s created at %s on issue %s found' % (self.bot_login(), comment_id, created_at, issue))
                prefix = None
                if body.startswith(self._warning_prefix):
                    prefix = self._warning_prefix
                if body.startswith(self._hint_prefix):
                    prefix = self._hint_prefix
                if prefix:
                    created = datetime.strptime(created_at, datetime_format)
                    lifetime = today - created
                    debug('%s %s %s is %s old' % (self.bot_login(), prefix, comment_id, lifetime))
                    if lifetime > warning_lifetime:
                        try:
                            self.rest_api('%s/%s' % (path_args, comment_id), method='DELETE')
                            info('Comment %s on issue %s deleted' % (comment_id, issue))
                        except CalledProcessError:
                            # the comment may have been deleted by a bot running in parallel
                            info('Comment %s on issue %s has been deleted already' % (comment_id, issue))

    def get_labels(self):
        r"""
        Return the list of labels of the issue resp. PR.
        """
        if self._labels is not None:
            return self._labels
        data = self.view('labels')
        self._labels = [l['name'] for l in data]
        info('List of labels for %s: %s' % (self._issue, self._labels))
        return self._labels

    def get_author(self):
        r"""
        Return the author of the issue resp. PR.
        """
        if self._author is not None:
            return self._author
        data = self.view('author')
        self._author = self.view('author')['login']
        info('Author of %s: %s' % (self._issue, self._author))
        return self._author

    def get_commits(self):
        r"""
        Return the list of commits of the PR.
        """
        if not self.is_pull_request():
            return None

        if self._commits is not None:
            return self._commits

        self._commits = self.view('commits')
        self._commit_date = max( com['committedDate'] for com in self._commits )
        info('Commits until %s for %s: %s' % (self._commit_date, self._issue, self._commits))
        return self._commits

    def get_reviews(self, complete=False):
        r"""
        Return the list of reviews of the PR. Per default only those proper reviews
        are returned which have been submitted after the most recent commit. Use
        keyword ``complete`` to get them all.
        """
        if not self.is_pull_request():
            return None

        if self._reviews is None:
            self._reviews = self.view('reviews')
            debug('Reviews for %s: %s' % (self._issue, self._reviews))

        if complete or not self._reviews:
            return self._reviews

        if self._commit_date is None:
            self.get_commits()

        date = self._commit_date
        unproper_rev = RevState.commented.value
        new_revs = [rev for rev in self._reviews if rev['submittedAt'] > date]
        proper_new_revs = [rev for rev in new_revs if rev['state'] != unproper_rev]
        info('Proper reviews after %s for %s: %s' % (date, self._issue, proper_new_revs))
        return proper_new_revs

    def get_latest_review(self, complete=False):
        r"""
        Return the latest review of the PR. Per default only those proper reviews
        are considered which have been submitted after the most recent commit. Use
        keyword ``complete`` to get the latest of all.
        """
        revs = self.get_reviews(complete=complete)
        if not revs:
            return
        res = revs[0]
        max_date = res['submittedAt']
        for rev in revs:
            cur_date = rev['submittedAt']
            if cur_date > max_date:
                max_date = cur_date
                res = rev
        fill_in = ''
        if not complete:
            fill_in = ' proper'
        info('PR %s had latest%s review at %s: %s' % (self._issue, fill_in, max_date, res))
        return res

    def active_partners(self, item):
        r"""
        Return the list of other labels from the selection list
        of the given one that are already present on the issue / PR.
        """
        sel_list = type(item)
        partners = [i for i in sel_list if i != item and i.value in self.get_labels()]
        info('Active partners of  %s: %s' % (item, partners))
        return partners

    # -------------------------------------------------------------------------
    # methods to validate the issue state
    # -------------------------------------------------------------------------
    def review_comment_to_state(self):
        r"""
        Return a State label if the most recent review comment
        starts with its value.
        """
        rev = self.get_latest_review(complete=True)
        ass = AuthorAssociation(rev['authorAssociation'])
        for stat in State:
            body = rev['body']
            if body.startswith(stat.value):
                info('Latest review comment contains status label %s' % stat)
                return stat, ass
        return None, ass

    def check_review_decision(self, rev_decision):
        r"""
        Return ``True`` if the latest proper review of the PR has the
        given decision.
        """
        rev = self.get_latest_review()
        if not rev:
            # no proper review since most recent commit.
            return False

        return rev['state'] == rev_decision.value

    def needs_work_valid(self):
        r"""
        Return ``True`` if the PR needs work. This is the case if
        the latest proper review request changes.
        """
        if self.check_review_decision(RevState.changes_requested):
            info('PR %s needs work' % self._issue)
            return True
        info('PR %s doesn\'t need work' % self._issue)
        return False

    def positive_review_valid(self):
        r"""
        Return ``True`` if the PR is positively reviewed. This is the case if
        the latest proper review is approved.
        """
        if self.check_review_decision(RevState.approved):
            info('PR %s has positve review' % self._issue)
            return True
        info('PR %s doesn\'t have positve review' % self._issue)
        return False

    def needs_review_valid(self):
        r"""
        Return ``True`` if the PR needs review. This is the case if
        all proper reviews are older than the youngest commit.
        """
        if self.is_draft():
            return False

        if self.needs_work_valid():
            info('PR %s already under review (needs work)' % self._issue)
            return False

        if self.positive_review_valid():
            info('PR %s already reviewed' % self._issue)
            return False

        info('PR %s needs review' % self._issue)
        return True

    def approve_allowed(self):
        r"""
        Return if the actor has permission to approve this PR.
        """
        revs = self.get_reviews()
        revs = [rev for rev in revs if rev['author']['login'] != self._actor]
        ch_req = RevState.changes_requested
        if any(rev['state'] == ch_req.value for rev in revs):
            info('PR %s can\'t be approved by %s since others reqest changes' % (self._issue, self._actor))
            return False

        return self.actor_valid()

    def actor_valid(self):
        r"""
        Return if the actor has permission to approve this PR.
        """
        author = self.get_author()

        if author != self._actor:
            info('PR %s can be approved by %s' % (self._issue, self._actor))
            return True

        revs = self.get_reviews()
        revs = [rev for rev in revs if not self.is_this_bot(rev['author']['login'])]
        if not revs:
            info('PR %s can\'t be approved by the author %s since no other person reviewed it' % (self._issue, self._actor))
            return False

        coms = self.get_commits()
        authors = []
        for com in coms:
            for auth in com['authors']:
                login = auth['login']
                if not login in authors:
                    if not self.is_this_bot(login) and login != author:
                        debug('PR %s has recent commit by %s' % (self._issue, login))
                        authors.append(login)

        if not authors:
            info('PR %s can\'t be approved by the author %s since no other person commited to it' % (self._issue, self._actor))
            return False

        info('PR %s can be approved by the author %s as co-author' % (self._issue, author))
        return True

    # -------------------------------------------------------------------------
    # methods to change the issue
    # -------------------------------------------------------------------------
    def gh_cmd(self, cmd, arg, option):
        r"""
        Perform a system call to ``gh`` for ``cmd`` to an isuue resp. PR.
        """
        issue = 'issue'
        if self._pr:
            issue = 'pr'
        cmd_str = 'gh %s %s %s %s "%s"' % (issue, cmd, self._url, option, arg)
        debug('Execute command: %s' % cmd_str)
        ex_code = os.system(cmd_str)
        if ex_code:
            warning('Execution of %s failed with exit code: %s' % (cmd_str, ex_code))

    def edit(self, arg, option):
        r"""
        Perform a system call to ``gh`` to edit an issue resp. PR.
        """
        self.gh_cmd('edit', arg, option)

    def mark_as_ready(self):
        r"""
        Perform a system call to ``gh`` to mark a PR as ready for review.
        """
        self.gh_cmd('ready', '', '')

    def review(self, arg, text=None):
        r"""
        Perform a system call to ``gh`` to review a PR.
        """
        if text:
            self.gh_cmd('review', arg, '-b \"%s\"' % text)
        else:
            self.gh_cmd('review', arg, '')

    def approve(self):
        r"""
        Approve the PR by the actor.
        """
        self.review('--approve')
        info('PR %s approved by %s' % (self._issue, self._actor))

    def request_changes(self):
        r"""
        Request changes for this PR by the actor.
        """
        self.review('--request-changes', '@%s requested changes for this PR' % self._actor)
        info('Changes requested for PR %s by %s' % (self._issue, self._actor))

    def review_comment(self, text):
        r"""
        Add a review comment.
        """
        self.review('--comment', text)
        info('Add review comment for PR %s: %s' % (self._issue, text))

    def add_comment(self, text):
        r"""
        Perform a system call to ``gh`` to add a comment to an issue or PR.
        """
        self.gh_cmd('comment', text, '-b')
        info('Add comment to %s: %s' % (self._issue, text))

    def add_warning(self, text):
        r"""
        Perform a system call to ``gh`` to add a warning to an issue or PR.
        """
        self.add_comment('%s %s' % (self._warning_prefix, text))

    def add_hint(self, text):
        r"""
        Perform a system call to ``gh`` to add a hint to an issue or PR.
        """
        self.add_comment('%s %s' % (self._hint_prefix, text))

    def add_label(self, label):
        r"""
        Add the given label to the issue or PR.
        """
        if not label in self.get_labels():
            self.edit(label, '--add-label')
            info('Add label to %s: %s' % (self._issue, label))

    def add_default_label(self, item):
        r"""
        Add the given label if there is no active partner.
        """
        if not self.active_partners(item):
            self.add_label(item.value)

    def select_label(self, item):
        r"""
        Add the given label and remove all others.
        """
        self.add_label(item.value)
        sel_list = type(item)
        for other in sel_list:
            if other != item:
                self.remove_label(other.value)

    def remove_label(self, label):
        r"""
        Remove the given label from the issue or PR of the handler.
        """
        if label in self.get_labels():
            self.edit(label, '--remove-label')
            info('Remove label from %s: %s' % (self._issue, label))

    def reject_label_addition(self, item):
        r"""
        Post a comment that the given label can not be added and select
        a corresponding other one.
        """
        if not self.is_pull_request():
            self.add_warning('Label *%s* can not be added to an issue. Please use it on the corresponding PR' % item.value)
        elif item is State.needs_review:
            self.add_warning('Label *%s* can not be added, since there are unresolved reviews' % item.value)
        else:
            self.add_warning('Label *%s* can not be added. Please use the GitHub review functionality' % item.value)
        self.remove_label(item.value)
        return

    def reject_label_removal(self, item):
        r"""
        Post a comment that the given label can not be removed and select
        a corresponding other one.
        """
        if type(item) == State:
            sel_list = 'status'
        else:
            sel_list = 'priority'
        self.add_hint('You don\'t need to remove %s labels any more. You\'d better just add the label which replaces it' % sel_list)
        return

    # -------------------------------------------------------------------------
    # methods to act on events
    # -------------------------------------------------------------------------
    def on_label_add(self, label):
        r"""
        Check if the given label belongs to a selection list. If so, remove
        all other labels of that list. In case of a state label reviews are
        booked accordingly.
        """
        sel_list = selection_list(label)
        if not sel_list:
            return

        item = sel_list(label)
        if label not in self.get_labels():
            # this is possible if two labels of the same selection list
            # have been added in one step (via multiple selection in the
            # pull down menue). In this case `label` has been removed
            # on the `on_label_add` of the first of the two labels
            partn = self.active_partners(item)
            if partn:
                self.add_warning('Label *%s* can not be added due to *%s*!' % (label, partn[0].value))
            else:
                warning('Label %s of %s not found!' % (label, self._issue))
            return

        if sel_list is State:
            if not self.is_pull_request():
                if item != State.needs_info:
                    self.reject_label_addition(item)
                    return

            if item == State.needs_review:
                if self.needs_review_valid():
                    # here we come for example after a sequence:
                    # needs review -> needs info -> needs review
                    pass
                elif self.is_draft():
                    self.mark_as_ready()
                else:
                    self.reject_label_addition(item)
                    return

            if item == State.needs_work:
                if self.needs_work_valid():
                    # here we come for example after a sequence:
                    # needs work -> needs info -> needs work
                    pass
                elif not self.is_draft():
                    self.request_changes()
                else:
                    self.reject_label_addition(item)
                    return

            if item == State.positive_review:
                if self.positive_review_valid():
                    # here we come for example after a sequence:
                    # positive review -> needs info -> positive review
                    pass
                elif self.approve_allowed():
                    self.approve()
                else:
                    self.reject_label_addition(item)
                    return

        if sel_list is Resolution:
            self.remove_all_labels_of_sel_list(Priority)

        for other in sel_list:
            if other != item:
                self.remove_label(other.value)

    def on_label_removal(self, label):
        r"""
        Check if the given label belongs to a selection list. If so, the
        removement is rejected and a comment is posted to instead add a
        replacement for ``label`` from the list. Exceptions are State labels
        on issues and State.needs_info on a PR.
        """
        sel_list = selection_list(label)
        if not sel_list:
            return

        item = sel_list(label)

        if len(self.active_partners(item)) > 0:
            return

        if sel_list is State:
            if self.is_pull_request():
                if item != State.needs_info:
                    self.reject_label_removal(item)
        elif sel_list is Priority:
            self.reject_label_removal(item)
        return

    def on_review_comment(self):
        r"""
        Check if the text of the most recent review begins with a
        specific label name. In this case, simulate the corresponding
        label addition. This feature is needed for people who don't
        have permission to add labels (i.e. aren't a member of the
        Triage team).
        """
        rev_state, ass = self.review_comment_to_state()
        if ass is AuthorAssociation.owner:
            if rev_state is State.positive_review:
                # allow the repository owner to approve his own PR for testing
                # the bot
                info('Owner approves PR %s for testing the bot' % self._issue)
                self.approve()
        elif ass.is_valid() or ass is Author.Assoziation.contributor:
            if rev_state in (State.needs_info, State.needs_review):
                # allow contributors who are not Triage members to set
                # these labels
                info('Simulate label addition of %s for %s' % (label, self._issue))
                self.select_label(rev_state)
                self.run(Action.labeled, label=rev_state.value)
            
    def remove_all_labels_of_sel_list(self, sel_list):
        r"""
        Remove all labels of given selection list.
        """
        for item in sel_list:
            self.remove_label(item.value)

    def run(self, action, label=None, rev_state=None):
        r"""
        Run the given action.
        """
        self.reset_view() # this is just needed for run_tests

        if action is Action.opened and self.is_pull_request():
            if not self.is_draft():
                self.add_default_label(State.needs_review)

        if action in (Action.closed, Action.reopened, Action.converted_to_draft):
            self.remove_all_labels_of_sel_list(State)

        if action is Action.labeled:
            self.on_label_add(label)

        if action is Action.unlabeled:
            self.on_label_removal(label)

        if action in (Action.ready_for_review, Action.synchronize):
            if self.needs_review_valid():
                self.select_label(State.needs_review)

        if action is Action.review_requested:
            self.select_label(State.needs_review)

        if action is Action.submitted:
            rev_state = RevState(rev_state.upper())
            if rev_state is RevState.approved:
                if self.actor_authorized() and self.positive_review_valid():
                    self.select_label(State.positive_review)

            if rev_state is RevState.changes_requested:
                if self.needs_work_valid():
                    self.select_label(State.needs_work)

            if rev_state is RevState.commented:
                self.on_review_comment()

    def run_tests(self):
        r"""
        Simulative run over all posibble events.

        This is not intended to validate all functionality. It just
        tests for bugs on invoking the methods. The result in the
        issue or PR depends on timing. Note that the GitHub action runner
        may run in parallel on the triggered events possibly on an other
        version of the code.
        """
        self.add_comment('Starting tests for sync_labels')
        for action in Action:
            self.add_comment('Test action %s' % action.value)
            if action in (Action.labeled, Action.unlabeled):
                for stat in State:
                    if action is Action.labeled:
                        self.add_label(stat.value)
                    else:
                        self.remove_label(stat.value)
                    self.run(action, label=stat.value)
                for prio in Priority:
                    if action is Action.labeled:
                        self.add_label(prio.value)
                    else:
                        self.remove_label(prio.value)
                    self.run(action, label=prio.value)
                res = Resolution.worksforme
                if action is Action.labeled:
                    self.add_label(res.value)
                    self.run(action, label=prio.value)
            elif action == Action.submitted and self.is_pull_request():
                for rev_stat in RevState:
                    if rev_stat is RevState.approved:
                        self.approve()
                        self.run(action, rev_state=rev_stat.value)
                    elif rev_stat is RevState.changes_requested:
                        self.request_changes()
                        self.run(action, rev_state=rev_stat.value)
                    elif rev_stat is RevState.commented:
                        for stat in State:
                            self.review_comment(stat.value)
                            self.run(action, rev_state=rev_stat.value)
            elif self.is_pull_request():
                self.run(action)


###############################################################################
# Main
###############################################################################
last_arg = None
run_tests = False
default_actor = 'sagetrac-github-bot'
cmdline_args = sys.argv[1:]
num_args = len(cmdline_args)

if num_args:
    last_arg = cmdline_args[num_args-1]

if last_arg in ('-t', '--test'):
    getLogger().setLevel(DEBUG)
    cmdline_args.pop()
    run_tests = True
elif last_arg in ('-d', '--debug'):
    getLogger().setLevel(DEBUG)
    cmdline_args.pop()
elif last_arg in ('-i', '--info'):
    getLogger().setLevel(INFO)
    cmdline_args.pop()
elif last_arg in ('-w', '--warning'):
    getLogger().setLevel(INFO)
    info('cmdline_args (%s) %s' % (num_args, cmdline_args))
    getLogger().setLevel(WARNING)
    cmdline_args.pop()
else:
    getLogger().setLevel(DEBUG)

num_args = len(cmdline_args)
info('cmdline_args (%s) %s' % (num_args, cmdline_args))

if run_tests and num_args in (1,2):
    if num_args == 2:
        url, actor = cmdline_args
    else:
        url, = cmdline_args
        actor = default_actor

    info('url: %s' % url)
    info('actor: %s' % actor)

    gh = GhLabelSynchronizer(url, actor)
    gh.run_tests()

elif num_args == 5:
    action, url, actor, label, rev_state = cmdline_args
    action = Action(action)

    info('action: %s' % action)
    info('url: %s' % url)
    info('actor: %s' % actor)
    info('label: %s' % label)
    info('rev_state: %s' % rev_state)

    gh = GhLabelSynchronizer(url, actor)
    gh.run(action, label=label, rev_state=rev_state)

elif num_args == 1:
    url, = cmdline_args

    info('url: %s' % url)

    gh = GhLabelSynchronizer(url, default_actor)

else:
    print('Need 5 arguments to synchronize: action, url, actor, label, rev_state')
    print('Need 1 argument to clean warning comments: url')
    print('Need 1 argument to run tests: url')
    print('The following options may be appended:')
    print('    -t --test to run the test suite')
    print('    -i --info to set the log-level to INFO')
    print('    -d --debug to set the log-level to DEBUG (default)')
    print('    -w --warning to set the log-level to WARNING')
