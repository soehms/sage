r"""
Database of small combinatorial designs

This module implements combinatorial designs that cannot be obtained by more
general constructions. Most of them come from the Handbook of Combinatorial
Designs [DesignHandbook]_.

All this would only be a dream without the mathematical knowledge and help of
Julian R. Abel.

These functions can all be obtained through the ``designs.<tab>`` functions.

This module implements:

- {LIST_OF_OA_CONSTRUCTIONS}

- {LIST_OF_MOLS_CONSTRUCTIONS}

- `V(m,t)` vectors:
{LIST_OF_VMT_VECTORS}

- :func:`RBIBD(120,8,1) <RBIBD_120_8_1>`

- `(v,k,\lambda)`-difference families:
{LIST_OF_DF}

- `(v,k,\lambda)`-difference matrices:
{LIST_OF_DM}

REFERENCES:

.. [DesignHandbook] Handbook of Combinatorial Designs (2ed)
  Charles Colbourn, Jeffrey Dinitz
  Chapman & Hall/CRC
  2012

Functions
---------
"""

from sage.combinat.designs.orthogonal_arrays import (OA_from_quasi_difference_matrix,
                                                     OA_from_Vmt,
                                                     QDM_from_Vmt,
                                                     OA_from_wider_OA,
                                                     OA_from_PBD,
                                                     OA_n_times_2_pow_c_from_matrix,
                                                     orthogonal_array)
from orthogonal_arrays import wilson_construction
from string import join

# Cyclic shift of a list
cyclic_shift = lambda l,i : l[-i:]+l[:-i]

def _MOLS_from_string(s,k):
    r"""
    Return MOLS from a string

    INPUT:

    - ``s`` (string) -- represents the MOLS with entries in a-z. To understand
      how the string should be formatted, read the source code of a constructor
      that uses it.

    - ``k`` (integer) -- the number of MOLS encoded by the string.

    EXAMPLES::

        sage: _ = designs.mutually_orthogonal_latin_squares(2,10) # indirect doctest
    """
    from sage.matrix.constructor import Matrix
    matrices = [[] for _ in range(k)]
    for i,l in enumerate(s.split()):
        l = [ord(x) - 97 for x in l]
        matrices[i%k].append(l)
    return map(Matrix, matrices)

def MOLS_10_2():
    r"""
    Return a pair of MOLS of order 10

    Data obtained from
    `<http://www.cecm.sfu.ca/organics/papers/lam/paper/html/POLS10/POLS10.html>`_

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_10_2
        sage: MOLS = MOLS_10_2()
        sage: print are_mutually_orthogonal_latin_squares(MOLS)
        True

    The design is available from the general constructor::

        sage: designs.mutually_orthogonal_latin_squares(2,10,existence=True)
        True
    """
    from sage.matrix.constructor import Matrix
    return [Matrix([[1,8,9,0,2,4,6,3,5,7],
                    [7,2,8,9,0,3,5,4,6,1],
                    [6,1,3,8,9,0,4,5,7,2],
                    [5,7,2,4,8,9,0,6,1,3],
                    [0,6,1,3,5,8,9,7,2,4],
                    [9,0,7,2,4,6,8,1,3,5],
                    [8,9,0,1,3,5,7,2,4,6],
                    [2,3,4,5,6,7,1,8,9,0],
                    [3,4,5,6,7,1,2,0,8,9],
                    [4,5,6,7,1,2,3,9,0,8]]),

            Matrix([[1,7,6,5,0,9,8,2,3,4],
                    [8,2,1,7,6,0,9,3,4,5],
                    [9,8,3,2,1,7,0,4,5,6],
                    [0,9,8,4,3,2,1,5,6,7],
                    [2,0,9,8,5,4,3,6,7,1],
                    [4,3,0,9,8,6,5,7,1,2],
                    [6,5,4,0,9,8,7,1,2,3],
                    [3,4,5,6,7,1,2,8,0,9],
                    [5,6,7,1,2,3,4,0,9,8],
                    [7,1,2,3,4,5,6,9,8,0]])]

def MOLS_12_5():
    r"""
    Return 5 MOLS of order 12

    These MOLS have been found by Brendan McKay.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_12_5
        sage: MOLS = MOLS_12_5()
        sage: print are_mutually_orthogonal_latin_squares(MOLS)
        True
    """
    M = """
        abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijkl
        badcfehgjilk ghefklijcdab dcbahgfelkji jilkbadcfehg klijcdabghef
        cdabghefklij efghijklabcd lkjidcbahgfe ijklabcdefgh fehgjilkbadc
        dcbahgfelkji cdabghefklij ghefklijcdab badcfehgjilk hgfelkjidcba
        ijklabcdefgh klijcdabghef efghijklabcd fehgjilkbadc jilkbadcfehg
        jilkbadcfehg fehgjilkbadc hgfelkjidcba dcbahgfelkji lkjidcbahgfe
        klijcdabghef hgfelkjidcba jilkbadcfehg cdabghefklij dcbahgfelkji
        lkjidcbahgfe ijklabcdefgh badcfehgjilk efghijklabcd ghefklijcdab
        efghijklabcd jilkbadcfehg fehgjilkbadc lkjidcbahgfe cdabghefklij
        fehgjilkbadc dcbahgfelkji cdabghefklij ghefklijcdab badcfehgjilk
        ghefklijcdab badcfehgjilk klijcdabghef hgfelkjidcba ijklabcdefgh
        hgfelkjidcba lkjidcbahgfe ijklabcdefgh klijcdabghef efghijklabcd
        """

    return _MOLS_from_string(M,5)

def MOLS_14_4():
    r"""
    Return four MOLS of order 14

    These MOLS were shared by Ian Wanless.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_14_4
        sage: MOLS = MOLS_14_4()
        sage: print are_mutually_orthogonal_latin_squares(MOLS)
        True

    The design is available from the general constructor::

        sage: designs.mutually_orthogonal_latin_squares(4,14,existence=True)
        True
    """
    M = """
        bjihgkecalnfmd  bfmcenidgjhalk  bcdefghijklmna  bcdefghijklmna
        fckjbhledimagn  jcgndfalehkbim  gnkjdmiclbhaef  jflhnkaecmgdib
        mgdlkcbafejnih  ikdhaegnmfblcj  lifhbjemkangcd  emkdjbgfnliahc
        cnhemldbigfkaj  hjlebifkangcmd  dalmgnbjehcfik  anighmflkbdcej
        edabfnmkcjhgli  gbkmfcjeliahdn  njcaeifhbdgkml  kebcajimdgfhln
        nfeicgajldkbhm  khclngdafmjibe  mfbkcdlagnjihe  cgnflembihakjd
        iagfjdhnkmelcb  elbdmahfignkjc  aemnhkjdcifblg  ilabkdnhfcjegm
        dlnkeafimhcjbg  ceabkjnihdmgfl  hdnikbagmcelfj  ljgnihecbamfdk
        gemalfihjnbdkc  adficlkmjbenhg  cgjflhnbiekdam  ndmabcjglfeikh
        jhfnimgdbkacel  liegjdmhnkcfab  fkibmagenldhjc  mbhiefljadkncg
        hkbgajnmeclidf  nmjfhkecbaldgi  imhlneckdfajgb  difjcnkamehgbl
        ablchikgnfdmje  fankgbljdcimeh  klegafdnhjmcbi  ghckmlbdeinjaf
        licmdbjfhagenk  mgialhcbkedjnf  jhadicmlfgbekn  fajlgidkhncbme
        kmjdneclgbihfa  dnhjimbgclfeka  ebgcjlkfamindh  hkemdacngjblfi
        """

    return _MOLS_from_string(M,4)

def MOLS_15_4():
    r"""
    Return 4 MOLS of order 15.

    These MOLS were shared by Ian Wanless.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_15_4
        sage: MOLS = MOLS_15_4()
        sage: print are_mutually_orthogonal_latin_squares(MOLS)
        True

    The design is available from the general constructor::

        sage: designs.mutually_orthogonal_latin_squares(4,15,existence=True)
        True
    """
    M = """
        bcdefghijklmnoa  bdgiknfcamehjlo  bhealiofmdjgcnk  blhcmdinejofakg
        abcdefghijklmno  acehjlogdbnfikm  lcifbmjagnekhdo  hcmidnejofkagbl
        oabcdefghijklmn  nbdfikmahecogjl  amdjgcnkbhoflie  midnjeofkaglbhc
        noabcdefghijklm  mocegjlnbifdahk  fbnekhdolciagmj  dnjeokfaglbhmci
        mnoabcdefghijkl  lnadfhkmocjgebi  kgcoflieamdjbhn  jeokfalgbhmcind
        lmnoabcdefghijk  jmobegilnadkhfc  olhdagmjfbnekci  ekfalgbmhcindjo
        klmnoabcdefghij  dknacfhjmobelig  jamiebhnkgcofld  aflgbmhcnidjoek
        jklmnoabcdefghi  helobdgiknacfmj  ekbnjfciolhdagm  lbgmhcnidojekaf
        ijklmnoabcdefgh  kifmacehjlobdgn  nflcokgdjamiebh  gmchnidojeakflb
        hijklmnoabcdefg  oljgnbdfikmaceh  iogmdalhekbnjfc  chndiojeakfblgm
        ghijklmnoabcdef  iamkhocegjlnbdf  djahnebmiflcokg  ndioejakfblgcmh
        fghijklmnoabcde  gjbnliadfhkmoce  hekbiofcnjgmdal  ioejafkblgcmhdn
        efghijklmnoabcd  fhkcomjbegilnad  miflcjagdokhneb  ojafkbglcmhdnie
        defghijklmnoabc  egildankcfhjmob  cnjgmdkbhealiof  fakbglchmdnieoj
        cdefghijklmnoab  cfhjmeboldgikna  gdokhnelcifbmja  kgblchmdineojfa
        """

    return _MOLS_from_string(M,4)

def MOLS_18_3():
    r"""
    Return 3 MOLS of order 18.

    These MOLS were shared by Ian Wanless.

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: from sage.combinat.designs.database import MOLS_18_3
        sage: MOLS = MOLS_18_3()
        sage: print are_mutually_orthogonal_latin_squares(MOLS)
        True

    The design is available from the general constructor::

        sage: designs.mutually_orthogonal_latin_squares(3,18,existence=True)
        True
    """
    M = """
        bgejhkmodcnarilpfq  beqpodgcflkrjahnim  bcdefghijklmnopqra
        echfbilnprdokajmqg  gcfrqpehdnmlabkioj  rbkamfgdehqjinopcl
        qfdigcjmohaeplkbnr  ehdgarqfibonmkcljp  mlbqhifgajdcrenopk
        prgejhdbnaikfqmlco  jfiehkargqcponldmb  hijbcdefgqraklmnop
        oqahfbiecpkjlgrnmd  hbgjfilkacrdqpomen  gderbkamfpclhqjino
        dprkigcjfeqlbmhaon  kichbgjmlodaerqpnf  fgamlbqhiopkjdcren
        geqaljhdbofrmcnikp  mljdichbngpekfarqo  efghijbcdnopqraklm
        chfrkmbieqpgandojl  onmbejdicphqflgkar  amfgderbkinopclhqj
        fdigalncjmrqhkoepb  dponcfbejaqirgmhlk  qhifgamlbrenopkjdc
        lnbqcogpakmhdrifej  crhapeoqmkbgidnjfl  leqjponacbkidfgmhr
        kmocrdphqblnieajgf  ndaikqfprmlchjeobg  kjmcrponhlbqeafgid
        rlnpdaeqigcmojfkbh  aoekjlrgqhnmdibfpc  dqriklponajbcmhfge
        jamoqekfrihdnpbglc  rkpflbmahdionejcgq  nacleqjpomhrbkidfg
        abknprflgdjieoqchm  ialqgmcnkrejpofbdh  onhkjmcrpgidlbqeaf
        hkcloqagmnebjfprdi  ljkmrhndoiafbqpgce  pondqriklfgeajbcmh
        nildmprkhjofcbgqae  pmblnaioefjkgcrqhd  jponacleqdfgmhrbki
        iojmenqalfbpgdchrk  fqncmokjpegblhdari  crponhkjmeafgidlbq
        mjpbnforklgcqhedia  qgrodnplbjfhcmieka  iklpondqrcmhfgeajb
        """

    return _MOLS_from_string(M,3)

# Index of the MOLS constructions
#
# Associates to n the pair (k,f) where f() is a function that returns k MOLS of order n
#
# This dictionary is used by designs.mutually_orthogonal_latin_squares(k,n).

MOLS_constructions = {
    10 : (2, MOLS_10_2),
    12 : (5, MOLS_12_5),
    14 : (4, MOLS_14_4),
    15 : (4, MOLS_15_4),
    18 : (3, MOLS_18_3)
}

# Add this data to the module's doc
LIST_OF_MOLS_CONSTRUCTIONS = join([":func:`{} MOLS of order {} <MOLS_{}_{}>`".format(k,n,n,k)
                                for n,(k,_) in MOLS_constructions.items()],
                               ", ")

def OA_7_18():
    r"""
    Return an OA(7,18)

    Proved in [JulianAbel13]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_18
        sage: OA = OA_7_18()
        sage: print is_orthogonal_array(OA,7,18,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,18,existence=True)
        True
    """
    M = """
        000 100 100 000 100 100 100 000 000 000 100 000
        000 020 100 100 000 120 110 110 010 020 010 120
        000 100 022 102 112 001 101 120 121 001 020 002
        000 002 100 002 102 122 010 111 110 121 021 001
        000 021 000 100 020 112 100 021 112 102 102 012
        000 000 011 010 100 010 110 122 011 121 120 111
        000 100 002 022 011 121 020 122 100 010 112 112
        """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    from sage.categories.cartesian_product import cartesian_product
    G = cartesian_product([AdditiveCyclic(2),AdditiveCyclic(3),AdditiveCyclic(3)])
    M = [G(map(int,xxx)) for xxx in M.split()]
    M = [M[i*12:(i+1)*12] for i in range(7)]

    Mb = []

    for a,b,c,d,e,f,g in zip(*M):
        for y in range(3):
            Mb.append([a + G((0,  0  , 0 )),
                       b + G((0,  0  , y )),
                       c + G((0,  y  , 0 )),
                       d + G((0, 2*y , y )),
                       e + G((0, 2*y ,2*y)),
                       f + G((0,  y  ,2*y)),
                       g + G((0,  0  ,2*y))])

    M = OA_from_quasi_difference_matrix(Mb,G,add_col=False)
    M = [M[i] for i in range(len(M)) if i%18<9] # only develop w.r.t the last two coordinates
    return M

def OA_6_20():
    r"""
    Return an OA(6,20)

    As explained in the Handbook III.3.49 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_6_20
        sage: OA = OA_6_20()
        sage: print is_orthogonal_array(OA,6,20,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(6,20,existence=True)
        True
    """
    M=[[None,   7,  13,   1,  16,   9,   2],
       [   0,   1,  15,   7,  17,   6,  14],
       [   0,  11,  10,  11,   5,   4,   3],
       [   7,None,  13,  16,   1,   2,   9],
       [   1,   0,  15,  17,   7,  14,   6],
       [  11,   0,  10,   5,  11,   3,   4]]

    Mb=[]

    for R in zip(*M):
        a,b,c,d,e,f = R
        Mb.append([a,b,c,d,e,f])
        Mb.append([b,c,a,f,d,e])
        Mb.append([c,a,b,e,f,d])

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    M = OA_from_quasi_difference_matrix(Mb,AdditiveCyclic(19),add_col=False)

    return M

def OA_5_22():
    r"""
    Return an OA(5,22)

    As explained in the Handbook III.3.51 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_5_22
        sage: OA = OA_5_22()
        sage: print is_orthogonal_array(OA,5,22,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(5,22,existence=True)
        True
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(21)
    M = [
        [   1,  13,  18,   3,  16,  19,None],
        [  16,  19,   1,  13,  18,   3,   0],
        [  18,   3,  16,  19,   1,  13,   0],
        [   6,  15,   6,  15,   6,  15,   0],
        [  12,   9,  19,  16,   5,   2,   0],
        ]

    Mb=[[0,7,14,None,0],
        [0,14,7,0,None]]

    for R in zip(*M):
        a,b,c,d,e = [G(x) if x is not None else None for x in R]
        Mb.append([a,b,c,d,e])

        Mb.append([16*c,
                   None if a is None else 16*a,
                   16*b,
                   16*d+7,
                   16*e+14])

        Mb.append([4*b,
                   4*c,
                   None if a is None else 4*a,
                   4*d+14,
                   4*e+7])

    M = OA_from_quasi_difference_matrix(Mb,G,add_col=False)
    return M

def OA_6_26():
    r"""
    Return an OA(6,26)

    As explained in the Handbook III.3.53 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_6_26
        sage: OA = OA_6_26()
        sage: print is_orthogonal_array(OA,6,26,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(6,26,existence=True)
        True
    """
    M = [
        [None,None,None,None,None],
        [   0,   0,   0,   0,   0],
        [   1,   6,   7,   8,  14],
        [   3,  11,  20,  18,  10],
        [   6,  10,  14,   1,   5],
        [   4,  19,   5,  12,   2],
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(21)
    Mb=[[0,0,0,0,0,0]]

    for R in zip(*M):
        a,b,c,d,e,f = R
        Mb.append([a,b,c,d,e,f])
        Mb.append([b,c,d,e,f,a])
        Mb.append([c,d,e,f,a,b])
        Mb.append([d,e,f,a,b,c])
        Mb.append([e,f,a,b,c,d])
        Mb.append([f,a,b,c,d,e])

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M

def OA_6_30():
    r"""
    Return an OA(6,30)

    As explained in the Handbook III.3.55 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_6_30
        sage: OA = OA_6_30()
        sage: print is_orthogonal_array(OA,6,30,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(6,30,existence=True)
        True
    """
    M = [
        [(0,0),None,(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),None,(0,4),(0,2),(0,3),(0,1)],
        [(0,0),(3,1),(3,0),None,(4,0),(1,0),(2,0)],
        [(0,0),(3,0),(0,2),(1,2),None,(0,1),(0,3)],
        [(0,0),(3,3),(1,2),(4,2),(2,0),None,(0,4)],
        [(0,0),(4,2),(2,4),(0,3),(2,3),(3,2),None]
        ]

    from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
    from sage.modules.free_module_element import free_module_element as vector
    G = AdditiveAbelianGroup([5,5])
    M = [[None if x is None else G(vector(x)) for x in L] for L in M]

    Mb=[]

    for R in zip(*M):
        a,b,c,d,e,f = R
        for i in range(5):
            Mb.append([
                None if a is None else a+G(vector((i,i))),
                None if b is None else b+G(vector((2*i,i))),
                None if c is None else c+G(vector((i,0))),
                None if d is None else d+G(vector((4*i,0))),
                None if e is None else e+G(vector((3*i,4*i))),
                None if f is None else f+G(vector((4*i,4*i)))])

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M

def OA_6_34():
    r"""
    Return an OA(6,34)

    As explained in the Handbook III.3.57 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_6_34
        sage: OA = OA_6_34()
        sage: print is_orthogonal_array(OA,6,34,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(6,34,existence=True)
        True
    """
    M = [
        [None,   0,   0,   0,   0,   0],
        [  30,  17,  10,  25,  23,   8],
        [  22,   4,  32,  29,  28,  22],
        [  25,  10,  20,  15,  21,  16],
        [   0,  12,  15,  16,  32,  23],
        [   6,  11,  18,  14,   9,  20]
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(33)

    Mb = [[ 0,  0,  0,  0,  0,   0],
          [ 1,  4, 16, 31, 25,  11],
          [ 3, 12, 15, 27,  9,  11],
          [10,  7, 28, 13, 19,   0],
          [ 5, 20, 14, 23, 26,None]]

    times4 = lambda x : None if x is None else 4*x
    for R in zip(*M):
        a,b,c,d,e,f = [None if x is None else G(x) for x in R]
        for i in range(5):
            Mb.append([a,b,c,d,e,f])
            a,b,c,d,e,f = map(times4,[e,a,b,c,d,f])

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M

def OA_6_38():
    r"""
    Return an OA(6,38)

    As explained in the Handbook III.3.60 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_6_38
        sage: OA = OA_6_38()
        sage: print is_orthogonal_array(OA,6,38,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(6,38,existence=True)
        True
    """
    M = [
        [None,  10,   1,   2,   6,   3,  22,   5,   7,   9,  14,  18,  28],
        [   0,   1,  10,  20,  23,  30,  35,  13,  33,  16,  29,  32,  21],
        [   0,  26,  26,  15,   8,   4,  17,  19,  34,  12,  31,  24,  25],
        [  10,None,  10,   6,   2,  22,   3,   7,   5,  14,   9,  28,  18],
        [   1,   0,  26,  23,  20,  35,  30,  33,  13,  29,  16,  21,  32],
        [  26,   0,   1,   8,  15,  17,   4,  34,  19,  31,  12,  25,  24]
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(37)

    Mb=[]

    for R in zip(*M):
        a,b,c,d,e,f = R
        Mb.append([a,b,c,d,e,f])
        Mb.append([b,c,a,f,d,e])
        Mb.append([c,a,b,e,f,d])

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M


def OA_9_40():
    r"""
    Return an OA(9,40)

    As explained in the Handbook III.3.62 [DesignHandbook]_. Uses the fact that
    `40 = 2^3 \times 5` and that `5` is prime.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_40
        sage: OA = OA_9_40()
        sage: print is_orthogonal_array(OA,9,40,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(9,40,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None)],
        [(0,None),(1,None),   (2,2),   (3,2),   (4,2),(2,None),(3,None),(4,None),   (0,2),   (1,2)],
        [(0,None),   (2,5),   (4,5),   (1,2),   (3,6),   (3,4),   (0,0),   (2,1),   (4,1),   (1,6)],
        [(0,None),   (3,4),   (1,4),   (4,0),   (2,5),(3,None),   (1,0),   (4,1),   (2,2),   (0,3)],
        [(0,None),   (4,6),(3,None),   (2,3),   (1,4),   (2,1),(1,None),   (0,4),   (4,0),   (3,2)],
        [(0,None),   (1,2),   (4,6),   (4,4),   (1,0),   (0,6),   (2,3),   (3,6),   (3,5),   (2,5)],
        [(1,None),   (0,3),   (1,2),   (4,5),(4,None),   (2,3),   (0,0),   (2,2),   (3,0),(3,None)],
        [(4,None),   (1,3),   (0,0),   (1,1),   (4,0),   (3,1),   (2,5),(0,None),   (2,1),(3,None)]
        ]
    Y = [None, 0, 1, 6, 5, 4, 3, 2]

    return OA_n_times_2_pow_c_from_matrix(9,3,FiniteField(5),A,Y,check=False)

def OA_7_42():
    r"""
    Return an OA(7,42)

    As explained in the Handbook III.3.63 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_42
        sage: OA = OA_7_42()
        sage: print is_orthogonal_array(OA,7,42,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,42,existence=True)
        True
    """
    M = [
        [None,None,None,None,None,None,None],
        [   0,   0,   0,   0,   0,   0,   0],
        [  18, -18,  11, -11,   5,  -5,   4],
        [  26, -26,  10, -10,  30, -30,  23],
        [  20, -20,   3,  -3,  33, -33,  23],
        [   5,  -5,  25, -25,  24, -24,   4],
        [  17, -17,   4,  -4,  22, -22,   0]
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(35)

    Mb=[]

    for R in zip(*M):
        for i in range(7):
            Mb.append(cyclic_shift(R,i))

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M

def OA_7_54():
    r"""
    Return an OA(7,54)

    As explained in the Handbook III.3.71 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_54
        sage: OA = OA_7_54()
        sage: print is_orthogonal_array(OA,7,54,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,54,existence=True)
        True
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(45)

    M = [
        [None,None,None,None,None,None,None,None,None],
        [   0,   0,   0,   0,   0,   0,   0,   0,   0],
        [   1,  27,  16,   7,  -1, -27, -16,  -7,   3],
        [  24,  40,   1,  35, -24, -40,  -1, -35,   7],
        [  10,  30,  22,  44, -10, -30, -22, -44,   7],
        [   5,  18,  14,  33,  -5, -18, -14, -33,   3],
        [  30,  16,  33,  27, -30, -16, -33, -27,   0],
        ]

    Mb=[]

    for R in zip(*M):
        for c in range(7):
            Mb.append(cyclic_shift(R,c))

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M

def OA_7_62():
    r"""
    Return an OA(7,62)

    As explained in the Handbook III.3.74 [DesignHandbook]_.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_62
        sage: OA = OA_7_62()
        sage: print is_orthogonal_array(OA,7,62,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,62,existence=True)
        True
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(54)

    M = [
        [ 0 ,None,None,None, 0   ,None ,None ,None,None,None],
        [17 , 0  , 0  , 0  , -17 ,  0  ,  0  ,  0 ,  1 , 11 ],
        [29 , 28 , 35 , 23 , -29 , -28 , -35 , -23,  3 , 19 ],
        [36 , 50 , 5  , 33 , -36 , -50 , -5  , -33,  7 , 33 ],
        [31 ,  2 , 43 , 30 , -31 , - 2 , -43 , -30, 34 , 33 ],
        [16 , 47 , 44 , 51 , -16 , -47 , -44 , -51, 30 , 19 ],
        [41 , 11 ,  1 , 17 , -41 , -11 , - 1 , -17, 28 , 11 ]
        ]

    Mb=[]

    for R in zip(*M):
        for c in range(7):
            Mb.append(cyclic_shift(R,c))

    M = OA_from_quasi_difference_matrix(Mb,G,add_col = False)
    return M

def OA_9_65():
    r"""
    Return an OA(9,65)

    Construction shared by Julian R. Abel

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_quasi_difference_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_65
        sage: OA = OA_9_65()
        sage: print is_orthogonal_array(OA,9,65,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(9,65,existence=True)
        True
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as G

    B = [None,1, 6, 7, 9, 19, 38, 42, 49] # Base block of a (57,8,1)-BIBD
    OA = orthogonal_array(9,9,2)
    M = [R for R in OA if any(R[0] != x for x in R)]

    M = [[B[x] for x in R] for R in M] # replacing [0,..,8] by the elements of B
    M.append([0]*9)

    M = OA_from_quasi_difference_matrix(M, G(57),add_col=False)
    return M

def OA_7_66():
    r"""
    Return an OA(7,66)

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_66
        sage: OA = OA_7_66()
        sage: print is_orthogonal_array(OA,7,66,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,66,existence=True)
        True
    """

    # base block of a (73,9,1) BIBD
    B = [0, 19, 26, 14, 63, 15, 32, 35, 65]
    # The corresponding BIBD
    BIBD= [[(x+i)%73 for x in B] for i in range(73)]
    # the first 7 elements of an oval
    #
    # (this is the only difference with the OA(7,68) construction)
    oval = [(-x)%73 for x in B][:7]
    # PBD minus the oval
    PBD = [[x for x in B if x not in oval] for B in BIBD]
    # We relabel the points to 0,1,2,...
    V = [x for x in range(73) if x not in oval]
    rel = dict(zip(V,range(len(V))))
    PBD = [[rel[x] for x in B] for B in PBD]
    return OA_from_PBD(7,66,PBD,check=False)

def OA_7_68():
    r"""
    Return an OA(7,68)

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_68
        sage: OA = OA_7_68()
        sage: print is_orthogonal_array(OA,7,68,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,68,existence=True)
        True
    """

    # base block of a (73,9,1) BIBD
    B = [0, 19, 26, 14, 63, 15, 32, 35, 65]
    # The corresponding BIBD
    BIBD= [[(x+i)%73 for x in B] for i in range(73)]
    # the first 5 elements of an oval
    #
    # (this is the only difference with the OA(7,66) construction)
    oval = [(-x)%73 for x in B][:5]
    # PBD minus the oval
    PBD = [[x for x in B if x not in oval] for B in BIBD]
    # We relabel the points to 0,1,2,...
    V = [x for x in range(73) if x not in oval]
    rel = dict(zip(V,range(len(V))))
    PBD = [[rel[x] for x in B] for B in PBD]
    return OA_from_PBD(7,68,PBD,check=False)

def OA_8_69():
    r"""
    Return an OA(8,69)

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_8_69
        sage: OA = OA_8_69()
        sage: print is_orthogonal_array(OA,8,69,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(8,69,existence=True)
        True
    """
    # base block of a (73,9,1) BIBD
    B = [1,2,4,8,16,32,37,55,64]
    # The corresponding BIBD
    BIBD= [[(x+i)%73 for x in B] for i in range(73)]
    oval = [72,71,69,65]
    # PBD minus the oval
    PBD = [[x for x in B if x not in oval] for B in BIBD]

    sets_of_size_seven = [R for R in PBD if len(R) == 7]
    others             = [R for R in PBD if len(R) != 7]

    # 68, 27, and 52 are the only elements appearing twice in the rows of
    # sets_of_size_seven, and each row contains exactly one of them.

    # We split them into "balanced" halves.
    O1 = sets_of_size_seven[:3]
    O2 = sets_of_size_seven[-3:]
    assert all(x in sum(O1,[]) for x in (68,27,52))
    assert all(x in sum(O2,[]) for x in (68,27,52))

    # Blocks of "others", without the 0..0,1..1,2..2 ... rows
    OA = OA_from_PBD(8,69,others,check=False)[:-69]

    # Blocks of O1
    OA_8_7 = orthogonal_array(8,7,check=False)
    for B in O1:
        for BB in OA_8_7:
            OA.append([B[i] for i in BB])

    # Blocks of O2
    OA_8_7_minus_TD_8_1 = OA_8_7
    OA_8_7_minus_TD_8_1.remove([0]*8)
    for B in O2:
        # Making sure the double element is the first one
        B.sort(key=lambda x: int(bool(x not in (68,27,52))))
        for BB in OA_8_7:
            OA.append([B[i] for i in BB])


    # Adding the  missing 0..0,1..1,... rows
    done = sum(O1,[])+sum(O2,[])
    missing = [x for x in range(73) if x not in done and x not in oval]
    for x in missing:
        OA.append([x]*8)

    # Relabelling everything to 0..68
    relabel = dict(zip([x for x in range(73) if x not in oval],range(69)))
    OA = [[relabel[x] for x in B] for B in OA]
    return OA

def OA_7_74():
    r"""
    Return an OA(7,74)

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_7_74
        sage: OA = OA_7_74()
        sage: print is_orthogonal_array(OA,7,74,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(7,74,existence=True)
        True
    """

    # base block of a (91,10,1) BIBD
    B = [0,1,3,9,27,81,61,49,56,77]
    # The corresponding BIBD
    BIBD= [[(x+i)%91 for x in B] for i in range(91)]
    # an oval
    oval = [(-x)%91 for x in B][-7:]
    # PBD minus the oval+B
    to_delete = oval + B
    PBD = [[x for x in B if x not in to_delete] for B in BIBD]
    PBD.remove([])
    # We relabel the points to 0,1,2,...
    V = [x for x in range(91) if x not in to_delete]
    rel = dict(zip(V,range(len(V))))
    PBD = [[rel[x] for x in B] for B in PBD]
    return OA_from_PBD(7,74,PBD,check=False)

def OA_8_76():
    r"""
    Return an OA(8,76)

    Construction shared by Julian R. Abel.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_8_76
        sage: OA = OA_8_76()
        sage: print is_orthogonal_array(OA,8,76,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(8,76,existence=True)
        True
    """
    # base block of a (91,10,1) BIBD
    B = [0,1,3,9,27,81,61,49,56,77]
    # The corresponding BIBD
    BIBD= [[(x+i)%91 for x in B] for i in range(91)]
    oval = [2,4,5,12,24]
    to_remove = oval + B
    # PBD minus the oval
    PBD = [[x for x in B if x not in to_remove] for B in BIBD]
    PBD.remove([])

    sets_of_size_seven = [R for R in PBD if len(R) == 7]
    others             = [R for R in PBD if len(R) != 7]

    # critical_points are the 10 elements appearing twice in the rows of the 10
    # sets_of_size_seven, and each row contains exactly two of them
    critical_points = [57,83,52,13,15,64,37,50,63,31]

    # We reorder the rows such that every element of critical_points is exactly
    # once the first element of a row.
    for i,x in zip(critical_points,sets_of_size_seven):
        x.sort(key=lambda x:-int(x==i))
        assert x[0]==i

    # Blocks of "others", without the 0..0,1..1,2..2 ... rows
    OA = OA_from_PBD(8,76,others,check=False)[:-76]

    OA_8_7 = orthogonal_array(8,7,check=False)
    OA_8_7_minus_TD_8_1 = OA_8_7
    OA_8_7_minus_TD_8_1.remove([0]*8)
    for B in sets_of_size_seven:
        for BB in OA_8_7:
            OA.append([B[i] for i in BB])

    # Adding the  missing 0..0,1..1,... rows
    done = sum(sets_of_size_seven,[])
    missing = [x for x in range(91) if x not in done and x not in to_remove]
    for x in missing:
        OA.append([x]*8)

    # Relabelling everything to 0..68
    relabel = dict(zip([x for x in range(91) if x not in to_remove],range(91)))
    OA = [[relabel[x] for x in B] for B in OA]
    return OA

def OA_11_80():
    r"""
    Return an OA(11,80)

    As explained in the Handbook III.3.76 [DesignHandbook]_. Uses the fact that
    `80 = 2^4 \times 5` and that `5` is prime.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_80
        sage: OA = OA_11_80()
        sage: print is_orthogonal_array(OA,11,80,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(11,80,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None)],
        [(0,None), (1,None),    (2,3), (3,None),    (4,3), (2,None),    (3,3), (4,None),    (0,3),    (1,3)],
        [(0,None),    (2,8),    (4,6),    (1,3),    (3,3),   (3,13),   (0,13),    (2,6),   (4,14),   (1,12)],
        [(0,None),   (3,11),    (1,0),    (4,9),    (2,0),    (3,7),    (1,8),   (4,10),   (2,10),   (0,11)],
        [(0,None),    (4,8),   (3,14),   (2,14),   (1,12),   (2,10),   (1,10),    (0,3),    (4,5),    (3,8)],
        [(0,None),    (1,8),   (4,14),   (4,12),    (1,1),    (0,1),    (2,8),   (3,12),    (3,6),    (2,1)],
        [(1,None),    (0,6),    (1,1),    (4,4),   (4,13),    (2,6),   (0,14),    (2,9),    (3,0),    (3,3)],
        [(4,None),    (1,9),    (0,7),    (1,1),    (4,8),    (3,5),   (2,14),    (0,0), (2,None),    (3,0)],
        [(4,None),    (4,6),    (1,2), (0,None),   (1,13),    (3,8),    (3,2),    (2,0),   (0,14), (2,None)],
        [(1,None),    (4,9),    (4,1),    (1,0),    (0,4),    (2,5), (3,None),    (3,5), (2,None), (0,None)]
        ]
    Y = [None, 0, 1, 14, 12, 7, 2, 11, 3, 6]

    return OA_n_times_2_pow_c_from_matrix(11,4,FiniteField(5),A,Y,check=False)

def OA_15_112():
    r"""
    Returns an OA(15,112)

    Published by Julian R. Abel in [AbelThesis]_. Uses the fact that 112 = `2^4
    \times 7` and that `7` is prime.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_15_112
        sage: OA = OA_15_112()
        sage: print is_orthogonal_array(OA,15,112,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(15,112,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (1,None), (4,None), (2,None), (2,None), (4,None), (1,None)],
        [(0,None), (1,None), (2,None), (3,   5), (4,   9), (5,  11), (6,  12), (1,  10), (0,  10), (1,  11), (4,  13), (2,   6), (2,   2), (4,   1)],
        [(0,None), (2,   3), (4,   6), (6,   0), (1,   1), (3,  12), (5,   6), (4,   2), (1,   9), (0,   3), (1,   7), (4,   7), (2,   8), (2,   5)],
        [(0,None), (3,   3), (6,   2), (2,   3), (5,   2), (1,   9), (4,  13), (2,   8), (4,  12), (1,  12), (0,   7), (1,  10), (4,  11), (2,  14)],
        [(0,None), (4,None), (1,   0), (5,   1), (2,   0), (6,   7), (3,   4), (2,  11), (2,   9), (4,  13), (1,   3), (0,   7), (1,  11), (4,   2)],
        [(0,None), (5,None), (3,  14), (1,   7), (6,   5), (4,   3), (2,   1), (4,   6), (2,   5), (2,  14), (4,  12), (1,   1), (0,   2), (1,   2)],
        [(0,None), (6,None), (5,   0), (4,   4), (3,  11), (2,   2), (1,   7), (1,  13), (4,   8), (2,  11), (2,   3), (4,None), (1,   8), (0,  10)],
        [(0,None), (4,   3), (2,  14), (1,   5), (1,   4), (2,   5), (4,   2), (0,   8), (6,  10), (3,  11), (5,   6), (5,   5), (3,   0), (6,  11)],
        [(0,None), (5,   3), (4,   0), (4,   6), (5,   4), (0,   3), (3,  11), (6,None), (0,   4), (6,   5), (3,  13), (5,   6), (5,   4), (3,   4)],
        [(0,None), (6,   3), (6,   4), (0,   5), (2,   5), (5,   5), (2,None), (3,   6), (6,   7), (0,  12), (6,  12), (3,  12), (5,None), (5,  10)],
        [(0,None), (0,   3), (1,None), (3,   9), (6,   8), (3,  14), (1,  14), (5,   6), (3,   8), (6,  13), (0,   8), (6,   3), (3,   9), (5,   0)], # the last 3,9 was a 3,3
        [(0,None), (1,   3), (3,   1), (6,   6), (3,None), (1,  10), (0,   1), (5,   7), (5,   7), (3,  14), (6,   0), (0,  10), (6,   9), (3,   6)],
        [(0,None), (2,None), (5,   3), (2,  10), (0,   8), (6,   5), (6,   0), (3,   7), (5,   1), (5,  12), (3,  14), (6,   4), (0,  10), (6,   4)],
        [(0,None), (3,None), (0,   4), (5,   6), (4,   1), (4,   7), (5,   1), (6,   8), (3,   2), (5,   2), (5,   2), (3,  13), (6,   7), (0,   2)]
    ]
    Y = [None, 0, 1, 14, 12, 7, 2, 11, 3, 4, 5, 10, 8, 6]

    return OA_n_times_2_pow_c_from_matrix(15,4,FiniteField(7),zip(*A),Y,check=False)

def OA_9_120():
    r"""
    Return an OA(9,120)

    Construction shared by Julian R. Abel:

        From a resolvable `(120,8,1)-BIBD`, one can obtain 7 `MOLS(120)` or a
        resolvable `TD(8,120)` by forming a resolvable `TD(8,8) - 8.TD(8,1)` on
        `I_8 \times B` for each block `B` in the BIBD.  This gives a `TD(8,120)
        - 120 TD(8,1)` (which is resolvable as the BIBD is resolvable).

    .. SEEALSO::

        :func:`RBIBD_120_8_1`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_120
        sage: OA = OA_9_120()
        sage: print is_orthogonal_array(OA,9,120,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(9,120,existence=True)
        True
    """
    from incidence_structures import IncidenceStructure
    RBIBD_120 = RBIBD_120_8_1()
    equiv = [RBIBD_120[i*15:(i+1)*15] for i in range(17)]

    OA8 = orthogonal_array(9,8)
    assert all( (len(set(B[:-1])) == 1) == (B[-1] == 0) for B in OA8)
    OA = []

    for i,classs in enumerate(equiv):
        for S in classs:
            for B in OA8:
                if B[-1] != 0:
                    OA.append([S[x] for x in B[:-1]]+[i*7+B[-1]])

    for i in range(120):
        OA.append([i]*8+[0])

    return OA

def OA_9_135():
    r"""
    Return an OA(9,135)

    Construction shared by Julian R. Abel:

        This design can be built by Wilson's method (`135 = 8.16 + 7`) applied
        to an Orthogonal Array `OA(9+7,16)` with 7 groups truncated to size 1 in
        such a way that a block contain 0, 1 or 3 points of the truncated
        groups.

        This is possible, because `PG(2,2)` (the projective plane over `GF(2)`)
        is a subdesign in `PG(2,16)` (the projective plane over `GF(16)`); in a
        cyclic `PG(2,16)` or `BIBD(273,17,1)` the points `\equiv 0
        \pmod{39}` form such a subdesign (note that `273=16^2 + 16 +1` and
        `273 = 39 \times 7` and `7 = 2^2 + 2 + 1`).

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_135
        sage: OA = OA_9_135()
        sage: print is_orthogonal_array(OA,9,135,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(9,135,existence=True)
        True

    As this orthogonal array requires a `(273,17,1)` cyclic difference set, we check that
    it is available::

        sage: G,D = designs.difference_family(273,17,1)
        sage: G
        Ring of integers modulo 273
    """
    from bibd import BIBD_from_difference_family
    from difference_family import singer_difference_set
    G,B = singer_difference_set(16,2)
    PG16 = BIBD_from_difference_family(G,B)

    n = 273

    # We consider a PG(2,2) (or a (7,3,1)-design, or a Fano plane) contained in
    # PG16: it is a set of 7 points such that any block of PG16 intersect on
    # 0,1, or 3 points. The set of points congruent to 0 mod 39 does the job!
    #
    # ... check that it works
    assert all(sum((x%39 == 0) for x in B) in [0,1,3] for B in PG16)

    # We now build an OA(17,16) from our PG16, in such a way that all points of
    # our PG(2,2) are in different columns. For this, we need to find a point p
    # that is not located on any of the lines defined by the points of the
    # PG(2,2).

    lines = [B for B in PG16 if sum((x%39 == 0) for x in B) == 3]
    p = set(range(237)).difference(*lines).pop()

    # We can now build a TD from our PG16 by removing p.
    for B in PG16:
        B.sort(key=lambda x:int(x%39 != 0))
    PG16.sort(key=lambda B:sum((x%39 == 0) for x in B))

    r = {}
    for B in PG16:
        if p in B:
            for x in B:
                if x != p:
                    r[x] = len(r)
    r[p] = n-1

    # The columns containing points from PG2 will be the last 7
    assert all(r[x*39] >= (n-1)-16*7 for x in range(7))
    # Those points are the first of each column
    assert all(r[x*39]%16 == 0 for x in range(7))

    PG = [sorted([r[x] for x in B]) for B in PG16]
    OA = [[x%16 for x in B] for B in PG if n-1 not in B]

    # We truncate the last 7 columns to size 1. We also drop the first column
    truncated_OA = [B[1:-7]+[x if x==0 else None for x in B[-7:]] for B in OA]

    # And call Wilson's construction
    return wilson_construction(truncated_OA, 9, 16, 8,7,(1,)*7,check=False)

def OA_11_160():
    r"""
    Returns an OA(11,160)

    Published by Julian R. Abel in [AbelThesis]_. Uses the fact that `160 = 2^5
    \times 5` is a product of a power of `2` and a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_160
        sage: OA = OA_11_160()
        sage: print is_orthogonal_array(OA,11,160,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(11,160,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
         [(0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (1,None), (4,None), (4,None), (1,None)],
         [(0,None), (1,None), (2,   5), (3,   9), (4,   9), (1,  16), (0,  20), (1,  23), (4,  24), (4,  19)],
         [(0,None), (2,   4), (4,   3), (1,  10), (3,  10), (4,  20), (1,   1), (0,  24), (1,   5), (4,   2)],
         [(0,None), (3,None), (1,  28), (4,   7), (2,   6), (4,   4), (4,  23), (1,   5), (0,   8), (1,   1)],
         [(0,None), (4,   4), (3,  25), (2,  24), (1,  13), (1,   6), (4,   6), (4,   2), (1,  18), (0,   1)],
         [(0,None), (2,None), (3,   3), (3,  21), (2,  18), (0,   6), (2,  20), (3,   3), (3,  11), (2,   1)],
         [(0,None), (3,   4), (0,   5), (1,  27), (1,  30), (2,None), (0,   0), (2,   2), (3,   2), (3,  18)],
         [(0,None), (4,None), (2,  19), (4,  26), (0,  12), (3,  19), (2,   4), (0,   2), (2,   0), (3,   0)],
         [(0,None), (0,   4), (4,  29), (2,  29), (4,None), (3,   0), (3,   0), (2,   1), (0,  18), (2,None)],
         [(0,None), (1,   4), (1,   5), (0,  19), (3,   2), (2,   0), (3,None), (3,   0), (2,None), (0,None)],
        ]

    Y = [None, 0, 1, 2, 15, 27, 22, 12, 3, 28]

    return OA_n_times_2_pow_c_from_matrix(11,5,FiniteField(5),zip(*A),Y,check=False)

def OA_16_176():
    r"""
    Returns an OA(16,176)

    Published by Julian R. Abel in [AbelThesis]_. Uses the fact that `176 = 2^4
    \times 11` is a product of a power of `2` and a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_16_176
        sage: OA = OA_16_176()
        sage: print is_orthogonal_array(OA,16,176,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(16,176,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(0 ,None),(1 ,None),(4 ,None),(9 ,None)],
        [(0 ,None),(1 ,None),(2 ,None),(3 ,   0),(4 ,   2),(5 ,  12),(6 ,   5),(7 ,   6),(8 ,  13),(9 ,   9),(10,  11),(1 ,   3),(0 ,   6),(1 ,  14),(4 ,  12)],
        [(0 ,None),(2 ,None),(4 ,   4),(6 ,   4),(8 ,   7),(10,   2),(1 ,   2),(3 ,  13),(5 ,   0),(7 ,   3),(9 ,   7),(4 ,   6),(1 ,  12),(0 ,   1),(1 ,  10)], # 5,1 became 5,0
        [(0 ,None),(3 ,None),(6 ,   3),(9 ,   4),(1 ,   6),(4 ,  13),(7 ,   1),(10,   1),(2 ,   7),(5 ,   1),(8 ,   0),(9 ,   6),(4 ,   4),(1 ,   5),(0 ,   1)],
        [(0 ,None),(4 ,None),(8 ,  13),(1 ,   8),(5 ,   0),(9 ,   5),(2 ,  14),(6 ,None),(10,   5),(3 ,   7),(7 ,  10),(5 ,   3),(9 ,  10),(4 ,  11),(1 ,  14)],
        [(0 ,None),(5 ,None),(10,  10),(4 ,   2),(9 ,   7),(3 ,   2),(8 ,   3),(2 ,  13),(7 ,   7),(1 ,   9),(6 ,None),(3 ,   7),(5 ,   1),(9 ,  10),(4 ,  11)],
        [(0 ,None),(6 ,None),(1 ,   8),(7 ,  14),(2 ,   2),(8 ,   3),(3 ,  11),(9 ,  12),(4 ,   8),(10,  13),(5 ,   1),(3 ,   6),(3 ,   5),(5 ,  10),(9 ,   9)],
        [(0 ,None),(7 ,None),(3 ,   3),(10,None),(6 ,  14),(2 ,   4),(9 ,   1),(5 ,   7),(1 ,   5),(8 ,   7),(4 ,  13),(5 ,   6),(3 ,   6),(3 ,  11),(5 ,   3)],
        [(0 ,None),(8 ,None),(5 ,  14),(2 ,  11),(10,  14),(7 ,   8),(4 ,  14),(1 ,  14),(9 ,   9),(6 ,  14),(3 ,   9),(9 ,   2),(5 ,   6),(3 ,   3),(3 ,  10)],
        [(0 ,None),(9 ,None),(7 ,   5),(5 ,   5),(3 ,   8),(1 ,   8),(10,None),(8 ,  12),(6 ,   9),(4 ,  12),(2 ,   9),(4 ,   7),(9 ,   2),(5 ,   0),(3 ,   7)],
        [(0 ,None),(10,None),(9 ,  11),(8 ,   7),(7 ,   6),(6 ,  12),(5 ,None),(4 ,   1),(3 ,  13),(2 ,   8),(1 ,   9),(1 ,None),(4 ,   3),(9 ,   7),(5 ,  13)],
        [(0 ,None),(6 ,   3),(2 ,   0),(10,   8),(8 ,  12),(7 ,   9),(7 ,   2),(8 ,   0),(10,   7),(2 ,  10),(6 ,   4),(0 ,   7),(10,  10),(7 ,   3),(2 ,  11)],
        [(0 ,None),(7 ,   3),(4 ,None),(2 ,  12),(1 ,  10),(1 ,   3),(2 ,   8),(4 ,   9),(7 ,   0),(0 ,   1),(5 ,   6),(10,   3),(0 ,   9),(10,  13),(7 ,  11)],
        [(0 ,None),(8 ,   3),(6 ,   8),(5 ,   2),(5 ,  13),(6 ,   1),(8 ,   9),(0 ,   2),(4 ,  10),(9 ,   8),(4 ,  12),(7 ,   7),(10,   2),(0 ,  12),(10,   4)],
        [(0 ,None),(9 ,   3),(8 ,   3),(8 ,   9),(9 ,   1),(0 ,   4),(3 ,   3),(7 ,  11),(1 ,   9),(7 ,  10),(3 ,   8),(2 ,  10),(7 ,   6),(10,  14),(0 ,   3)],
        [(0 ,None),(10,   3),(10,   5),(0 ,   1),(2 ,   1),(5 ,   8),(9 ,   2),(3 ,   5),(9 ,   5),(5 ,   3),(2 ,   4),(6 ,  12),(2 ,   6),(7 ,  11),(10,   7)],
        [(0 ,None),(0 ,   3),(1 ,None),(3 ,   2),(6 ,   8),(10,  11),(4 ,   6),(10,None),(6 ,None),(3 ,   1),(1 ,   1),(8 ,   0),(6 ,  14),(2 ,   0),(7 ,  14)],
        [(0 ,None),(1 ,   3),(3 ,   8),(6 ,   9),(10,   8),(4 ,  10),(10,   1),(6 ,  10),(3 ,   0),(1 ,   8),(0 ,  11),(8 ,  10),(8 ,  14),(6 ,  10),(2 ,  14)],
        [(0 ,None),(2 ,   3),(5 ,   1),(9 ,   8),(3 ,   4),(9 ,  14),(5 ,   5),(2 ,   4),(0 ,   2),(10,   2),(10,None),(6 ,   2),(8 ,   5),(8 ,   1),(6 ,   9)],
        [(0 ,None),(3 ,   3),(7 ,   0),(1 ,None),(7 ,   1),(3 ,  10),(0 ,   8),(9 ,  13),(8 ,None),(8 ,  10),(9 ,  14),(2 ,   0),(6 ,   5),(8 ,   5),(8 ,   7)], # 2,None became 2,0
        [(0 ,None),(4 ,   3),(9 ,  10),(4 ,  14),(0 ,  14),(8 ,  14),(6 ,  14),(5 ,   6),(5 ,  13),(6 ,   5),(8 ,  12),(7 ,   1),(2 ,   4),(6 ,   3),(8 ,   6)],
        [(0 ,None),(5 ,   3),(0 ,   8),(7 ,   3),(4 ,  10),(2 ,   1),(1 ,   3),(1 ,  10),(2 ,None),(4 ,   8),(7 ,  12),(10,   6),(7 ,  10),(2 ,   6),(6 ,   1)], # 7,12 became 4,8
    ]

    Y = [None, 0, 1, 2, 8, 6, 9, 4, 10, 3, 5, 11, 13, 14, 12]
    return OA_n_times_2_pow_c_from_matrix(16,4,FiniteField(11),zip(*A),Y,check=False)

def OA_11_185():
    r"""
    Returns an OA(11,185)

    The construction is given in [Greig99]_. In Julian R. Abel's words:

        Start with a `PG(2,16)` with a `7` points Fano subplane; outside this
        plane there are `7(17-3) = 98` points on a line of the subplane and
        `273-98-7 = 168` other points.  Greig notes that the subdesign
        consisting of these `168` points is a `(168, \{10,12\})-PBD`. Now add
        the `17` points of a line disjoint from this subdesign (e.g. a line of
        the Fano subplane).  This line will intersect every line of the `168`
        point subdesign in `1` point. Thus the new line sizes are `11` and
        `13`, plus a unique line of size `17`, giving a `(185,\{11,13,17\}`-PBD
        and an `OA(11,185)`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_185
        sage: OA = OA_11_185()
        sage: print is_orthogonal_array(OA,11,185,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(11,185,existence=True)
        True

    """
    from sage.combinat.designs.difference_family import difference_family

    G,(B,) = difference_family(273,17)
    BIBD = [[int(x+i) for x in B] for i in G] # a cyclic PG(2,16)

    # All points congruent to 0 mod[39] form a Fano subplane with the property
    # that each block of the PG(2,16) intersect the Fano subplane in either 0,1
    # or 3 points
    assert all(sum(x%39==0 for x in B) in [0,1,3] for B in BIBD)

    # Lines of the Fano subplane that are contained in blocks
    fano_lines = [B for B in BIBD if sum(x%39==0 for x in B) == 3]

    # Points on a line of the Fano sublane
    on_a_fano_line = set().union(*fano_lines)

    # Not on a line of the Fano plane
    not_on_a_fano_line = set(range(273)).difference(on_a_fano_line)

    # The PBD
    ground_set = not_on_a_fano_line.union(fano_lines[0])
    PBD = [ground_set.intersection(B) for B in BIBD]
    relabel = {v:i for i,v in enumerate(ground_set)}
    PBD = [[relabel[x] for x in B] for B in PBD if len(B)>1]
    special_set = [relabel[x] for x in fano_lines[0]]

    # Check that everything is fine
    assert all(len(B) in (11,13) or set(B) == set(special_set) for B in PBD)

    OA = OA_from_PBD(11,185,[B for B in PBD if len(B)<17],check=False)[:-185]
    OA.extend([[i]*11 for i in range(185) if i not in special_set])
    OA.extend([[special_set[x] for x in B] for B in orthogonal_array(11,17)])
    return OA

def OA_10_205():
    r"""
    Return an OA(10,205)

    Julian R. Abel shared the following construction, which originally appeared
    in Theorem 8.7 of [Greig99]_, and can in Lemmas 5.14-5.16 of [ColDin01]_:

        Consider a `PG(2,4^2)` containing a Baer subplane (i.e. a `PG(2,4)`) `B`
        and a point `p\in B`. Among the `4^2+1=17` lines of `PG(2,4^2)`
        containing `p`:

        * `4+1=5` lines intersect `B` on `5` points

        * `4^2-4=12` lines intersect `B` on `1` point

        As those lines are disjoint outside of `B` we can use them as groups to
        build a GDD on `16^2+16+1-(4^4+4+1)=252` points. By keeping only 9 lines
        of the second kind, however, we obtain a `(204,\{9,13,17\})`-GDD of type
        12^5.16^9.

        We complete it into a PBD by adding a block `g\cup \{204\}` for each
        group `g`. We then build an OA from this PBD using the fact that all
        blocks of size 9 are disjoint.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_205
        sage: OA = OA_10_205()
        sage: print is_orthogonal_array(OA,10,205,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(10,205,existence=True)
        True
    """
    # Base block of a cyclic PG(2,4^2)
    pplane_size = 16**2+16+1
    baer_subplane_size = 4**2+4+1

    B = [0, 1, 22, 33, 83, 122, 135, 141, 145, 159, 175, 200, 226, 229, 231, 238, 246]
    pplane = [[(xx+i)%pplane_size for xx in B]  for i in range(pplane_size)]
    baer_subplane = set([i*pplane_size/baer_subplane_size for i in range(baer_subplane_size)])

    p = list(baer_subplane)[0]

    # We want all lines through p, but keep only 9 of those which intersect the
    # subplane on 1 point.
    lines_through_p = [B for B in pplane if p in B]
    lines_through_p.sort(key=lambda s:len(baer_subplane.intersection(s)))

    # Remove the Baer subplane and relabel everything to a (204,{9,13})-GDD of type
    # 12^5.16^9 whose groups are the subset of (truncated) lines through p
    groups = [[xx for xx in l if xx not in baer_subplane] for l in lines_through_p[4**2-4-9:]]
    relabel = {v:i for i,v in enumerate(sum(groups,[]))}
    GDD = [[relabel[xx] for xx in B if xx in relabel] for B in pplane if p not in B]

    # We turn the GDD into a PBD by extending the groups with a new point 204.
    GDD.extend([[relabel[xx] for xx in G]+[204] for G in groups])

    # We build the OA, knowing that the blocks of size 9 are disjoint
    blocks_of_size_9 = [B for B in GDD if len(B) == 9]
    blocks_of_size_9_union = sum(blocks_of_size_9,[])

    OA = OA_from_PBD(10,205,[B for B in GDD if len(B)!=9],check=False)[:-205]

    OA.extend([[B[xx] for xx in R]
               for R in orthogonal_array(10,9)
               for B in blocks_of_size_9])

    # The missing [i,i,...] blocks
    OA.extend([[i]*10
               for i in set(range(205)).difference(blocks_of_size_9_union)])

    return OA

def OA_16_208():
    r"""
    Returns an OA(16,208)

    Published by Julian R. Abel in [AbelThesis]_. Uses the fact that `208 = 2^4
    \times 13` is a product of `2` and a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_16_208
        sage: OA = OA_16_208()                        # not tested -- too long
        sage: print is_orthogonal_array(OA,16,208,2)  # not tested -- too long
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(16,208,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (0 ,None), (1 ,None)],
        [(0 ,None), (1 ,None), (2 ,   0), (3 ,   7), (4 ,   1), (5 ,  11), (6 ,   2), (7 ,  10), (8 ,None), (9 ,  10), (10,None), (11,   3), (12,   3), (1 ,   4), (0 ,   8)],
        [(0 ,None), (2 ,None), (4 ,   4), (6 ,   3), (8 ,   0), (10,   5), (12,  14), (1 ,None), (3 ,  10), (5 ,   7), (7 ,   3), (9 ,  12), (11,   6), (4 ,   9), (1 ,  14)],
        [(0 ,None), (3 ,None), (6 ,   4), (9 ,   6), (12,  10), (2 ,  11), (5 ,  14), (8 ,   3), (11,  13), (1 ,   1), (4 ,  12), (7 ,  14), (10,   1), (9 ,   7), (4 ,   8)],
        [(0 ,None), (4 ,None), (8 ,   9), (12,   5), (3 ,  10), (7 ,  14), (11,   0), (2 ,   6), (6 ,  11), (10,  11), (1 ,   9), (5 ,   3), (9 ,   9), (3 ,   6), (9 ,   8)],
        [(0 ,None), (5 ,None), (10,   5), (2 ,   5), (7 ,   3), (12,   3), (4 ,  12), (9 ,   3), (1 ,   2), (6 ,   2), (11,None), (3 ,  13), (8 ,   7), (12,  10), (3 ,   1)],
        [(0 ,None), (6 ,None), (12,  13), (5 ,   5), (11,  13), (4 ,   6), (10,   6), (3 ,   2), (9 ,   4), (2 ,  12), (8 ,  13), (1 ,  13), (7 ,   2), (10,   8), (12,None)],
        [(0 ,None), (7 ,None), (1 ,   2), (8 ,  12), (2 ,   4), (9 ,  12), (3 ,   0), (10,  10), (4 ,  14), (11,  11), (5 ,  14), (12,   9), (6 ,   8), (10,   3), (10,   6)],
        [(0 ,None), (8 ,None), (3 ,None), (11,   4), (6 ,  12), (1 ,  12), (9 ,  14), (4 ,   2), (12,   9), (7 ,   9), (2 ,None), (10,   1), (5 ,  14), (12,   5), (10,   8)],
        [(0 ,None), (9 ,None), (5 ,   9), (1 ,   7), (10,   6), (6 ,   3), (2 ,   6), (11,  10), (7 ,  11), (3 ,  13), (12,   2), (8 ,   0), (4 ,  13), (3 ,   3), (12,  14)],
        [(0 ,None), (10,None), (7 ,   7), (4 ,   1), (1 ,   8), (11,   1), (8 ,  11), (5 ,   4), (2 ,  11), (12,   8), (9 ,  12), (6 ,   4), (3 ,   0), (9 ,   4), (3 ,   8)],
        [(0 ,None), (11,None), (9 ,   3), (7 ,  11), (5 ,  14), (3 ,  10), (1 ,  10), (12,   0), (10,   2), (8 ,   2), (6 ,   6), (4 ,   2), (2 ,  12), (4 ,   8), (9 ,  10)],
        [(0 ,None), (12,None), (11,   4), (10,   9), (9 ,   2), (8 ,None), (7 ,   9), (6 ,  12), (5 ,   5), (4 ,None), (3 ,   7), (2 ,  10), (1 ,  13), (1 ,   6), (4 ,   0)],
        [(0 ,None), (5 ,   3), (7 ,   5), (6 ,   5), (2 ,  14), (8 ,   5), (11,   1), (11,   6), (8 ,  13), (2 ,  13), (6 ,   9), (7 ,None), (5 ,  10), (0 ,   5), (2 ,   8)],
        [(0 ,None), (6 ,   3), (9 ,   4), (9 ,  13), (6 ,   4), (0 ,   5), (4 ,   6), (5 ,   2), (3 ,None), (11,  14), (3 ,   3), (5 ,   7), (4 ,   1), (2 ,   8), (0 ,   2)],
        [(0 ,None), (7 ,   3), (11,   5), (12,  12), (10,None), (5 ,   5), (10,   7), (12,   9), (11,   9), (7 ,   7), (0 ,   0), (3 ,  12), (3 ,  11), (8 ,  13), (2 ,  14)],
        [(0 ,None), (8 ,   3), (0 ,   8), (2 ,   6), (1 ,None), (10,   9), (3 ,  12), (6 ,   8), (6 ,   4), (3 ,   9), (10,   2), (1 ,  11), (2 ,   7), (5 ,   2), (8 ,   2)],
        [(0 ,None), (9 ,   3), (2 ,   3), (5 ,   3), (5 ,   8), (2 ,   0), (9 ,   1), (0 ,   3), (1 ,  14), (12,   3), (7 ,   6), (12,   4), (1 ,   3), (6 ,  10), (5 ,   7)],
        [(0 ,None), (10,   3), (4 ,   2), (8 ,   0), (9 ,   8), (7 ,   1), (2 ,   5), (7 ,None), (9 ,   2), (8 ,   4), (4 ,  14), (10,  13), (0 ,  10), (11,   7), (6 ,  10)],
        [(0 ,None), (11,   3), (6 ,   9), (11,  14), (0 ,  10), (12,  13), (8 ,   6), (1 ,   8), (4 ,   7), (4 ,   0), (1 ,  14), (8 ,   2), (12,   8), (7 ,  10), (11,   7)], # 6,10 became 6,9
        [(0 ,None), (12,   3), (8 ,  12), (1 ,   9), (4 ,   6), (4 ,  13), (1 ,   6), (8 ,   1), (12,   4), (0 ,   7), (11,   5), (6 ,   6), (11,  14), (7 ,   3), (7 ,   5)],
        [(0 ,None), (0 ,   3), (10,  10), (4 ,   2), (8 ,   1), (9 ,None), (7 ,   2), (2 ,  10), (7 ,  13), (9 ,   5), (8 ,  14), (4 ,   7), (10,  11), (11,  13), (7 ,   0)],
        [(0 ,None), (1 ,   3), (12,  11), (7 ,  12), (12,  13), (1 ,   2), (0 ,   9), (9 ,   6), (2 ,  13), (5 ,   4), (5 ,  13), (2 ,   4), (9 ,  12), (6 ,   5), (11,   1)],
        [(0 ,None), (2 ,   3), (1 ,   8), (10,None), (3 ,  13), (6 ,None), (6 ,   1), (3 ,   0), (10,   4), (1 ,  14), (2 ,   0), (0 ,   3), (8 ,  13), (5 ,   1), (6 ,   7)], # 2,None became 2,0
        [(0 ,None), (3 ,   3), (3 ,  14), (0 ,   1), (7 ,  14), (11,   4), (12,   9), (10,   1), (5 ,   9), (10,None), (12,  13), (11,None), (7 ,   7), (8 ,   6), (5 ,   0)],
        [(0 ,None), (4 ,   3), (5 ,  10), (3 ,   8), (11,   8), (3 ,   0), (5 ,   7), (4 ,  12), (0 ,  13), (6 ,None), (9 ,  11), (9 ,   5), (6 ,   0), (2 ,   5), (8 ,   8)],
    ]

    Y = [None, 0, 1, 2, 12, 9, 13, 11, 7, 4, 8, 5, 14, 6, 3]

    return OA_n_times_2_pow_c_from_matrix(16,4,FiniteField(13),zip(*A),Y,check=False)

def OA_15_224():
    r"""
    Returns an OA(15,224)

    Published by Julian R. Abel in [AbelThesis]_ (uses the fact that `224=2^5
    \times 7` is a product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_15_224
        sage: OA = OA_15_224()                         # not tested -- too long
        sage: print is_orthogonal_array(OA,15,224,2)   # not tested -- too long
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(15,224,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (1,None), (4,None), (2,None), (2,None), (4,None), (1,None)],
        [(0,None), (1,None), (2,   9), (3,  23), (4,  29), (5,   4), (6,  30), (1,  26), (0,None), (1,  11), (4,   2), (2,  28), (2,None), (4,  13)],
        [(0,None), (2,None), (4,   8), (6,None), (1,  29), (3,  21), (5,   4), (4,   5), (1,   4), (0,  14), (1,   5), (4,   6), (2,   0), (2,   2)],
        [(0,None), (3,None), (6,   8), (2,  12), (5,   4), (1,   1), (4,   2), (2,   1), (4,  18), (1,  27), (0,   5), (1,None), (4,   1), (2,None)],
        [(0,None), (4,None), (1,   9), (5,   2), (2,  29), (6,  17), (3,   0), (2,  12), (2,   5), (4,  22), (1,   0), (0,  29), (1,  19), (4,None)],
        [(0,None), (5,None), (3,  26), (1,   0), (6,  29), (4,  16), (2,  11), (4,  21), (2,  28), (2,  16), (4,   0), (1,   3), (0,  11), (1,   2)],
        [(0,None), (6,None), (5,   3), (4,  19), (3,  24), (2,  20), (1,  28), (1,  12), (4,  23), (2,   0), (2,   5), (4,  29), (1,   0), (0,   2)],
        [(0,None), (4,   4), (2,  14), (1,  23), (1,  22), (2,  17), (4,  17), (0,  25), (6,  21), (3,  11), (5,   2), (5,  27), (3,   5), (6,   2)],
        [(0,None), (5,   4), (4,   3), (4,   0), (5,  20), (0,   4), (3,   8), (6,  28), (0,  16), (6,   1), (3,  22), (5,   0), (5,   0), (3,   2)],
        [(0,None), (6,   4), (6,None), (0,  18), (2,   0), (5,  20), (2,   4), (3,  11), (6,  15), (0,  18), (6,   5), (3,   0), (5,None), (5,   2)],
        [(0,None), (0,   4), (1,  15), (3,  29), (6,  20), (3,  24), (1,  13), (5,  30), (3,   2), (6,None), (0,  10), (6,   3), (3,   0), (5,None)],
        [(0,None), (1,   4), (3,   4), (6,  12), (3,  28), (1,  27), (0,   6), (5,   7), (5,  29), (3,   0), (6,   0), (0,   0), (6,   0), (3,None)], # 6,19 became 6,12
        [(0,None), (2,   4), (5,  11), (2,   5), (0,  21), (6,  11), (6,  24), (3,  24), (5,  11), (5,  30), (3,None), (6,None), (0,None), (6,   1)],
        [(0,None), (3,   4), (0,  11), (5,  11), (4,  22), (4,   2), (5,  23), (6,  22), (3,  27), (5,   1), (5,   0), (3,None), (6,None), (0,None)]
    ]

    Y = [None, 0, 1, 2, 27, 22, 11, 4, 26, 25, 29, 24, 7, 20]

    return OA_n_times_2_pow_c_from_matrix(15,5,FiniteField(7),zip(*A),Y,check=False)

def OA_11_254():
    r"""
    Return an OA(11,254)

    This constructions appears in [Greig99]_.

    From a cyclic `PG(2,19)` whose base blocks contains 7,9, and 4 points in the
    congruence classes mod 3, build a `(254,{11,13,16})-PBD` by ignoring the
    points of a congruence class. There exist `OA(12,11),OA(12,13),OA(12,16)`,
    which gives the `OA(11,254)`.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_PBD`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_254
        sage: OA = OA_11_254()
        sage: print is_orthogonal_array(OA,11,254,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(11,254,existence=True)
        True
    """

    # Base block of a PG(2,19)
    B = (0,1,19,28,96,118,151,153,176,202,240,254,290,296,300,307,337,361,366,369)
    BIBD = [[(x+i)%381 for x in B]  for i in range(381)]

    # We only keep points congruent to 0,1 mod 3 and relabel the PBD. The result is
    # a (254,{11,13,16})-PBD
    BIBD = [[2*(x//3)+x%3 for x in B if x%3<2] for B in BIBD]

    return OA_from_PBD(11,254,BIBD,check=False)

def OA_20_352():
    r"""
    Returns an OA(20,352)

    Published by Julian R. Abel in [AbelThesis]_ (uses the fact that `352=2^5
    \times 11` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_20_352
        sage: OA = OA_20_352()                        # not tested (~25s)
        sage: print is_orthogonal_array(OA,20,352,2)  # not tested (~25s)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(20,352,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    # Column 8, line 6 : 4,25 became 4,27
    #           line 17: 3,0  became 3,None
    # Column 14,line 1 : 4,1  became 4,0
    # Column 18,line 18: 0,0  became 0,None
    A = [
        [(0,None),(0, None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(1,None),(4,None),(9,None),(5, None),(3,None),(3,None),(5,None)],
        [(0,None),(1, None),(2,  13),(3,   2),(4,   0),(5,   8),(6,  30),(7,   0),(8,  13),(9,  26),(10, 10),(1,  29),(0,   9),(1,  11),(4,   0),(9,   23),(5,   7),(3,  25),(3,  29)],
        [(0,None),(2, None),(4,  29),(6,   6),(8,   3),(10, 18),(1,  21),(3,  24),(5,   4),(7,   7),(9,  29),(4,  22),(1,   2),(0,  27),(1,  10),(4,   13),(9,  22),(5,   6),(3,  20)],
        [(0,None),(3, None),(6,  25),(9,  21),(1,  23),(4,  25),(7,  12),(10, 16),(2,  26),(5,  27),(8,  19),(9,  27),(4,   6),(1,   5),(0,   6),(1,   15),(4,  10),(9,   2),(5,  14)],
        [(0,None),(4, None),(8,   3),(1,  23),(5,  17),(9,   7),(2,   7),(6,  25),(10, 27),(3,  30),(7,   5),(5,  23),(9,  24),(4,  16),(1,  12),(0,    8),(1,  12),(4,  17),(9,  28)],
        [(0,None),(5, None),(10, 10),(4,  27),(9,   4),(3,  24),(8,  21),(2,   3),(7,  22),(1,  21),(6,  24),(3,  28),(5,   3),(9,  26),(4,  29),(1,    9),(0,  19),(1,   2),(4,   0)],
        [(0,None),(6, None),(1,  11),(7,   9),(2,  14),(8,  15),(3,  11),(9,   7),(4,  27),(10, 13),(5,   4),(3,  18),(3,   0),(5,   5),(9,   2),(4,    7),(1,  30),(0,  10),(1,None)],
        [(0,None),(7, None),(3,  25),(10,  7),(6,  29),(2,   4),(9,  10),(5,  22),(1,  25),(8,  18),(4,  11),(5,  21),(3,  29),(3,  14),(5,  12),(9,   25),(4,   2),(1,  13),(0,  19)],
        [(0,None),(8, None),(5,  27),(2,  30),(10, 24),(7,   4),(4,   6),(1,   4),(9,   5),(6,  27),(3,   0),(9,   2),(5,  20),(3,  10),(3,  13),(5,    2),(9,   5),(4,  21),(1,  12)],
        [(0,None),(9, None),(7,  21),(5,   0),(3,   9),(1,  13),(10, 17),(8,   1),(6,  15),(4,  30),(2,  28),(4,   3),(9,  28),(5,   0),(3,None),(3,    2),(5,  23),(9,  10),(4,  15)],
        [(0,None),(10,None),(9,  29),(8,   8),(7,   6),(6,   6),(5,  18),(4,  20),(3,  22),(2,   7),(1,  13),(1,  24),(4,  13),(9,  14),(5,  29),(3,   27),(3,  16),(5,  12),(9,   4)],
        [(0,None),(6,    4),(2,  17),(10, 16),(8,  26),(7,  17),(7,  21),(8,   9),(10,  2),(2,  25),(6,  27),(0,  20),(10,  8),(7,  12),(2,  26),(6,   22),(8,   8),(8,  16),(6,  13)],
        [(0,None),(7,    4),(4,   1),(2,   0),(1,   8),(1,  18),(2,  10),(4,   9),(7,   2),(0,  11),(5,  27),(10, 27),(0,  16),(10, 19),(7,   0),(2,    2),(6,  26),(8,  30),(8,   6)],
        [(0,None),(8,    4),(6,  19),(5,  24),(5,  16),(6,  20),(8,None),(0,  17),(4,   5),(9,  23),(4,  27),(7,  22),(10, 25),(0,  23),(10, 11),(7,   10),(2,  16),(6,  28),(8,   3)],
        [(0,None),(9,    4),(8,  14),(8,  30),(9,  16),(0,   0),(3,  25),(7,  30),(1,  27),(7,   4),(3,  10),(2,   5),(7,   3),(10, 11),(0,  21),(10,None),(7,   7),(2,  19),(6,  24)],
        [(0,None),(10,   4),(10, 30),(0,  12),(2,   9),(5,   9),(9,   0),(3,  14),(9,  17),(5,  17),(2,  18),(6,  10),(2,   0),(7,  16),(10, 23),(0,    1),(10, 26),(7,  18),(2,   9)],
        [(0,None),(0,    4),(1,  13),(3,  28),(6,  25),(10, 28),(4,  16),(10, 17),(6,  23),(3,   7),(1,  22),(8,  22),(6,  27),(2,  29),(7,   5),(10,  14),(0,  12),(10, 14),(7,   6)],
        [(0,None),(1,    4),(3,   6),(6,   4),(10, 13),(4,  12),(10, 15),(6,  27),(3,None),(1,  26),(0,   3),(8,  21),(8,  26),(6,  13),(2,  27),(7,   11),(10,  5),(0,   3),(10,  3)],
        [(0,None),(2,    4),(5,  12),(9,  27),(3,   7),(9,  21),(5,None),(2,  22),(0,  28),(10, 30),(10, 25),(6,  12),(8,   6),(8,  30),(6,  28),(2,    6),(7,  26),(10,  3),(0,None)],
        [(0,None),(3,    4),(7,  22),(1,   7),(7,   8),(3,  12),(0,  27),(9,   1),(8,  17),(8,   4),(9,  12),(2,  16),(6,  23),(8,  14),(8,   2),(6,   26),(2,  14),(7,  22),(10, 30)],
        [(0,None),(4,    4),(9,  21),(4,  25),(0,   9),(8,  23),(6,   5),(5,  20),(5,  13),(6,  19),(8,   0),(7,  30),(2,  29),(6,  24),(8,  18),(8,   10),(6,   9),(2,  20),(7,   4)],
        [(0,None),(5,    4),(0,  25),(7,   4),(4,  20),(2,   3),(1,None),(1,  21),(2,None),(4,  26),(7,   1),(10, 23),(7,  20),(2,   3),(6,   5),(8,   19),(8,   9),(6,  23),(2,   7)],
    ]

    Y = [None, 0, 1, 2, 18, 5, 11, 4, 13, 26, 25, 29, 24, 7, 20, 19, 9, 12, 15]

    return OA_n_times_2_pow_c_from_matrix(20,5,FiniteField(11),zip(*A),Y,check=False)

def OA_20_416():
    r"""
    Returns an OA(20,416)

    Published by Julian R. Abel in [AbelThesis]_ (uses the fact that `416=2^5
    \times 13` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_20_416
        sage: OA = OA_20_416()                        # not tested (~35s)
        sage: print is_orthogonal_array(OA,20,416,2)  # not tested
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(20,416,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    Z = None
    A=[
        [(0,Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (0 , Z), (1 , Z), (4 , Z), (9 , Z), (3 , Z), (12, Z)],
        [(0,Z), (1 , Z), (2 ,18), (3 , 2), (4 ,20), (5 ,22), (6 ,11), (7 ,19), (8 , 0), (9 ,26), (10, Z), (11, 5), (12,27), (1 ,17), (0 ,30), (1 ,22), (4 ,29), (9 , 6), (3 ,19)],
        [(0,Z), (2 , 4), (4 ,21), (6 ,10), (8 ,24), (10,13), (12, 7), (1 ,11), (3 ,29), (5 ,12), (7 ,21), (9 , 2), (11,11), (4 , 5), (1 ,11), (0 ,23), (1 ,13), (4 , 6), (9 ,15)],
        [(0,Z), (3 , 4), (6 ,17), (9 ,20), (12,26), (2 , 2), (5 ,12), (8 ,29), (11, 1), (1 , Z), (4 ,15), (7 ,16), (10,27), (9 , 2), (4 , 7), (1 , 5), (0 ,23), (1 ,24), (4 , 8)],
        [(0,Z), (4 , 4), (8 ,29), (12, 8), (3 , 3), (7 , 8), (11, 2), (2 ,17), (6 , 4), (10, 2), (1 ,21), (5 ,29), (9 ,20), (3 , 2), (9 , 1), (4 ,14), (1 ,21), (0 ,24), (1 ,28)],
        [(0,Z), (5 , 4), (10,22), (2 ,18), (7 , 6), (12, 2), (4 ,18), (9 ,27), (1 ,15), (6 , Z), (11,20), (3 ,15), (8 , 9), (12, 9), (3 , 3), (9 ,13), (4 , 4), (1 , 7), (0 ,14)],
        [(0,Z), (6 , Z), (12,23), (5 ,13), (11,11), (4 ,10), (10, 0), (3 , 4), (9 ,16), (2 ,28), (8 ,27), (1 , 1), (7 ,23), (10,17), (12, 9), (3 ,20), (9 ,16), (4 ,17), (1 ,26)],
        [(0,Z), (7 , Z), (1 , 3), (8 ,13), (2 , 8), (9 , 9), (3 , 0), (10,26), (4 , 5), (11, 6), (5 ,22), (12, 1), (6 ,17), (10,10), (10, 5), (12,15), (3 ,25), (9 , Z), (4 , 4)],
        [(0,Z), (8 , 4), (3 ,10), (11, 3), (6 ,17), (1 ,21), (9 ,18), (4 , 5), (12,27), (7 ,20), (2 ,16), (10,25), (5 ,22), (12,21), (10,25), (10,12), (12,28), (3 ,19), (9 ,29)],
        [(0,Z), (9 , 4), (5 , 6), (1 ,16), (10, 4), (6 ,24), (2 ,14), (11,11), (7 , 2), (3 , 9), (12,30), (8 ,28), (4 , 2), (3 , 7), (12, 6), (10,17), (10, 2), (12,13), (3 ,26)],
        [(0,Z), (10, 4), (7 ,11), (4 ,18), (1 ,23), (11,21), (8 ,28), (5 ,21), (2 ,29), (12,20), (9 , 0), (6 , 8), (3 , 6), (9 , 7), (3 ,12), (12, 5), (10, 1), (10,21), (12, 5)],
        [(0,Z), (11, 4), (9 ,22), (7 ,11), (5 ,17), (3 , Z), (1 ,17), (12,25), (10,14), (8 ,18), (6 , 2), (4 ,17), (2 ,25), (4 ,29), (9 , 6), (3 , 2), (12, 8), (10,13), (10,14)],
        [(0,Z), (12, Z), (11, 7), (10,26), (9 ,24), (8 , 4), (7 ,25), (6 , Z), (5 ,13), (4 , 9), (3 , 5), (2 ,19), (1 ,10), (1 ,26), (4 ,14), (9 , 7), (3 ,11), (12, 9), (10,20)],
        [(0,Z), (5 , Z), (7 , 7), (6 ,27), (2 , 5), (8 , 1), (11,23), (11, Z), (8 ,23), (2 ,21), (6 ,20), (7 , 5), (5 , 6), (0 , 2), (2 ,12), (8 ,15), (5 ,22), (6 ,25), (11,10)],
        [(0,Z), (6 , 4), (9 ,24), (9 ,18), (6 ,26), (0 ,26), (4 ,17), (5 ,24), (3 , 5), (11, 9), (3 ,15), (5 ,23), (4 ,22), (2 ,26), (0 , 8), (2 ,21), (8 ,25), (5 ,15), (6 , 8)],
        [(0,Z), (7 , 4), (11,11), (12, 9), (10,10), (5 , 6), (10, 1), (12,24), (11, 6), (7 ,26), (0 , 8), (3 ,10), (3 ,29), (8 , 3), (2 ,24), (0 ,22), (2 ,13), (8 , 2), (5 , 0)],
        [(0,Z), (8 , Z), (0 ,27), (2 , 0), (1 ,25), (10,21), (3 ,10), (6 ,20), (6 ,14), (3 , 1), (10, 3), (1 ,15), (2 ,14), (5 ,12), (8 ,11), (2 ,28), (0 ,15), (2 ,13), (8 ,22)],
        [(0,Z), (9 , Z), (2 ,13), (5 ,11), (5 , 6), (2 ,24), (9 , 9), (0 ,14), (1 ,30), (12, 1), (7 ,15), (12,15), (1 , 5), (6 ,23), (5 , 9), (8 , 3), (2 ,27), (0 ,28), (2 ,12)],
        [(0,Z), (10, Z), (4 ,18), (8 ,23), (9 ,27), (7 , 4), (2 , 2), (7 , Z), (9 ,10), (8 , 8), (4 , 0), (10,12), (0 ,21), (11,28), (6 ,15), (5 ,23), (8 , 5), (2 ,28), (0 , 7)],
        [(0,Z), (11, Z), (6 , 7), (11,27), (0 , 0), (12,17), (8 ,11), (1 ,12), (4 ,22), (4 ,15), (1 ,16), (8 , 0), (12, 6), (7 ,16), (11,30), (6 ,21), (5 ,14), (8 ,17), (2 ,26)],
        [(0,Z), (12, 4), (8 ,28), (1 ,22), (4 , 2), (4 ,15), (1 , 6), (8 ,12), (12,19), (0 ,21), (11, 2), (6 , 4), (11,19), (7 ,30), (7 ,11), (11,12), (6 ,20), (5 , 3), (8 , 7)],
        [(0,Z), (0 , 4), (10,21), (4 , 4), (8 , 1), (9 , 6), (7 ,30), (2 , 4), (7 , 8), (9 ,30), (8 , 3), (4 ,22), (10, 3), (11,25), (7 , 1), (7 ,24), (11,20), (6 ,30), (5 , 4)],
        [(0,Z), (1 , 4), (12,21), (7 , 3), (12, 2), (1 , 1), (0 , 6), (9 ,14), (2 ,19), (5 , 6), (5 ,12), (2 , 9), (9 , 9), (6 ,19), (11, Z), (7 , 4), (7 , 6), (11,29), (6 ,15)],
        [(0,Z), (2 , Z), (1 ,22), (10, Z), (3 , 5), (6 ,30), (6 ,26), (3 , 1), (10,12), (1 ,16), (2 ,28), (0 ,20), (8 ,11), (5 ,29), (6 , 7), (11,21), (7 ,14), (7 , 8), (11,11)],
        [(0,Z), (3 , Z), (3 , 4), (0 ,18), (7 , 2), (11,16), (12,28), (10, 4), (5 ,28), (10, 0), (12, 4), (11,10), (7 ,11), (8 ,17), (5 , 6), (6 ,16), (11, 4), (7 ,22), (7 ,28)],
        [(0,Z), (4 , Z), (5 ,22), (3 ,18), (11, Z), (3 ,15), (5 , 1), (4 ,26), (0 ,10), (6 , 8), (9 , 9), (9 ,29), (6 , Z), (2 ,23), (8 ,28), (5 ,30), (6 , 8), (11,24), (7 ,16)]
    ]

    Y = [None, 0, 1, 2, 18, 5, 11, 4, 13, 26, 25, 29, 24, 7, 20, 19, 9, 12, 15]

    return OA_n_times_2_pow_c_from_matrix(20,5,FiniteField(13),zip(*A),Y,check=False)

def OA_9_514():
    r"""
    Returns an OA(9,514)

    Construction shared by Julian R. Abel:

        A `V(8,57)` vector appears on page p281 of the Brouwer-Van Rees paper
        [BvR82]_. This gives a `TD(8+2, 514) - TD(8+2,57)`. Using a `TD(9,57)`
        (not a `TD(10,57)`) it yields a `TD(9,514)`.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_from_Vmt`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_9_514
        sage: OA = OA_9_514()
        sage: print is_orthogonal_array(OA,9,514,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(9,514,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField
    q = 8*57+1
    Fq = FiniteField(q)

    Vm8_57 = [0,1,3,2,12,333,363,154,340]
    QDM = QDM_from_Vmt(8,57,Vm8_57)
    QDM = [B[:-1] for B in QDM]
    return OA_from_quasi_difference_matrix(QDM,Fq,add_col=False)

def OA_20_544():
    r"""
    Returns an OA(20,544)

    Published by Julian R. Abel in [AbelThesis]_ (uses the fact that
    `544=2^5 \times 17` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_20_544
        sage: OA = OA_20_544()                        # not tested (too long ~1mn)
        sage: print is_orthogonal_array(OA,20,544,2)  # not tested
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(20,544,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    Z = None

    A=[
        [(0,Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(0 , Z),(1 , Z)],
        [(0,Z),(1 , 4),(2 , 7),(3 ,30),(4 ,17),(5 , 2),(6 ,22),(7 ,23),(8 ,28),(9 , 2),(10,27),(11,26),(12,13),(13,25),(14,18),(15,15),(16,18),(1 ,14),(0 , 1)],
        [(0,Z),(2 , 4),(4 ,20),(6 ,29),(8 ,27),(10, 7),(12,20),(14,19),(16,26),(1 ,28),(3 , Z),(5 ,27),(7 , Z),(9 ,11),(11, Z),(13,17),(15, 1),(4 ,14),(1 ,14)],
        [(0,Z),(3 , Z),(6 ,14),(9 ,26),(12,17),(15,15),(1 ,26),(4 ,24),(7 ,27),(10,13),(13,10),(16, 7),(2 , 1),(5 , Z),(8 , 1),(11,15),(14,18),(9 ,21),(4 , 6)],
        [(0,Z),(4 , 4),(8 , Z),(12, 2),(16,23),(3 ,19),(7 ,26),(11, 7),(15,26),(2 , 3),(6 ,11),(10,16),(14,23),(1 ,30),(5 , 1),(9 ,30),(13,19),(16,10),(9 , 4)],
        [(0,Z),(5 , Z),(10,17),(15,19),(3 ,13),(8 , 4),(13,21),(1 , 9),(6 , 7),(11, 4),(16,24),(4 , 6),(9 ,11),(14, Z),(2 , 6),(7 ,14),(12,10),(8 ,12),(16, 1)],
        [(0,Z),(6 , Z),(12, 1),(1 ,23),(7 ,21),(13,10),(2 , 0),(8 ,15),(14,19),(3 ,30),(9 ,21),(15,17),(4 ,25),(10,20),(16,15),(5 ,16),(11,15),(2 ,22),(8 ,29)], # 2,Z -> 2,0
        [(0,Z),(7 , Z),(14,30),(4 ,26),(11,24),(1 ,22),(8 ,22),(15,27),(5 ,23),(12,13),(2 ,18),(9 ,22),(16, 6),(6 ,27),(13,19),(3 , 1),(10,16),(15, 9),(2 , 5)],
        [(0,Z),(8 , 4),(16, 5),(7 ,18),(15,11),(6 , 1),(14,21),(5 ,28),(13,19),(4 , 7),(12,19),(3 ,15),(11,13),(2 ,23),(10, 1),(1 ,23),(9 ,19),(13,27),(15,25)], # 13,9 -> 15,25
        [(0,Z),(9 , Z),(1 , 3),(10, 4),(2 ,29),(11,13),(3 ,27),(12,11),(4 ,30),(13, 9),(5 ,18),(14,17),(6 ,18),(15,10),(7 ,11),(16,28),(8 ,26),(13,12),(13, 9)],
        [(0,Z),(10, Z),(3 ,18),(13,21),(6 , 8),(16, 1),(9 ,11),(2 ,11),(12,12),(5 ,20),(15,21),(8 ,12),(1 , 5),(11,28),(4 ,16),(14,16),(7 ,21),(15, 0),(13,20)],
        [(0,Z),(11, 4),(5 ,25),(16, 2),(10,18),(4 , 6),(15,20),(9 ,29),(3 ,13),(14,24),(8 ,18),(2 ,22),(13, 1),(7 , 8),(1 ,21),(12,16),(6 ,23),(2 ,10),(15,26)],
        [(0,Z),(12, 4),(7 ,11),(2 , 4),(14,25),(9 , 0),(4 , 5),(16,21),(11,18),(6 ,18),(1 ,22),(13,27),(8 ,23),(3 ,20),(15,18),(10, 7),(5 ,10),(8 ,11),(2 ,18)],
        [(0,Z),(13, Z),(9 ,21),(5 ,17),(1 ,26),(14,30),(10,11),(6 , 1),(2 , 8),(15, 9),(11, 5),(7 ,29),(3 ,17),(16, 3),(12, 3),(8 ,30),(4 , 3),(16, 5),(8 ,21)],
        [(0,Z),(14, Z),(11,20),(8 ,24),(5 , Z),(2 , 2),(16,24),(13,12),(10,21),(7 ,26),(4 ,29),(1 , 1),(15, 1),(12,19),(9 , 8),(6 ,26),(3 ,10),(9 ,20),(16,21)],
        [(0,Z),(15, Z),(13,21),(11,10),(9 , 7),(7 ,21),(5 ,11),(3 ,19),(1 ,29),(16,13),(14, 9),(12, 9),(10, 8),(8 ,16),(6 ,15),(4 ,14),(2 ,29),(4 ,16),(9 , 9)],
        [(0,Z),(16, 4),(15,19),(14,21),(13, 0),(12,13),(11,28),(10,21),(9 , 5),(8 ,18),(7 , 2),(6 , Z),(5 ,20),(4 ,26),(3 , 8),(2 , 9),(1 ,23),(1 ,19),(4 ,23)], # 13,Z -> 13,0
        [(0,Z),(3 , 4),(12,11),(10,17),(14,14),(7 , 1),(6 ,27),(11,25),(5 , 2),(5 ,24),(11,15),(6 , 8),(7 ,28),(14,21),(10, 4),(12,20),(3 ,26),(0 , 5),(3 ,12)],
        [(0,Z),(4 , Z),(14,17),(13,26),(1 ,12),(12,12),(12,23),(1 ,13),(13, 7),(14,10),(4 ,28),(0 ,11),(2 , 7),(10,15),(7 , Z),(10, 1),(2 , 6),(3 ,24),(0 ,18)],
        [(0,Z),(5 , 4),(16,24),(16, 1),(5 ,27),(0 ,14),(1 ,11),(8 ,13),(4 ,25),(6 ,25),(14,14),(11, 6),(14, 4),(6 ,24),(4 , 4),(8 ,28),(1 ,14),(12,22),(3 ,11)],
        [(0,Z),(6 , 4),(1 ,10),(2 , 6),(9 ,12),(5 , 3),(7 ,11),(15,30),(12,21),(15,26),(7 , 3),(5 ,12),(9 , 0),(2 ,25),(1 , 2),(6 , 0),(0 ,13),(10,13),(12,14)],
        [(0,Z),(7 , 4),(3 ,24),(5 ,25),(13,20),(10,19),(13,16),(5 , 4),(3 ,23),(7 ,20),(0 , 8),(16, 4),(4 ,19),(15, 0),(15,10),(4 ,11),(16, 7),(14,11),(10, 6)],
        [(0,Z),(8 , Z),(5 , 1),(8 ,21),(0 , 1),(15,17),(2 ,26),(12, 2),(11, 6),(16, 2),(10,15),(10,13),(16,16),(11,12),(12,22),(2 ,11),(15,22),(7 ,30),(14,22)], # 8,9 -> 8,21
        [(0,Z),(9 , 4),(7 ,20),(11,24),(4 , 7),(3 ,11),(8 ,21),(2 ,23),(2 , 2),(8 ,12),(3 , 8),(4 ,13),(11,17),(7 , 4),(9 , 3),(0 ,18),(14,12),(6 ,26),(7 ,28)],
        [(0,Z),(10, 4),(9 ,22),(14,23),(8 , 5),(8 , 8),(14,12),(9 , 6),(10,20),(0 ,11),(13,23),(15,26),(6 ,12),(3 ,15),(6 , Z),(15,18),(13, 1),(11,22),(6 ,24)],
        [(0,Z),(11, Z),(11,11),(0 ,28),(12,16),(13,18),(3 , 3),(16,22),(1 , 9),(9 , Z),(6 ,21),(9 , 6),(1 , 0),(16, 1),(3 , 2),(13,28),(12, 6),(5 ,18),(11, 9)],
        [(0,Z),(12, Z),(13, 5),(3 ,14),(16,22),(1 , 5),(9 , 1),(6 , Z),(9 , 3),(1 , 9),(16,21),(3 ,18),(13,17),(12,29),(0 ,13),(11, 4),(11,18),(5 ,21),(5 , 6)],
        [(0,Z),(13, 4),(15,27),(6 ,26),(3 ,20),(6 ,29),(15,11),(13,18),(0 , 4),(10, 5),(9 ,16),(14,26),(8 ,20),(8 , 8),(14,11),(9 ,10),(10, 9),(11,17),(5 ,21)],
        [(0,Z),(14, 4),(0 ,29),(9 , 8),(7 , 2),(11,18),(4 ,22),(3 ,22),(8 ,13),(2 ,23),(2 ,21),(8 , 9),(3 ,30),(4 ,21),(11, 5),(7 ,25),(9 , Z),(6 , 0),(11,17)],
        [(0,Z),(15, 4),(2 ,27),(12,27),(11,28),(16, 0),(10, 6),(10,12),(16,11),(11,15),(12, 2),(2 ,10),(15,19),(0 ,11),(8 ,10),(5 , 6),(8 , 5),(7 , 7),(6 ,16)],
        [(0,Z),(16, Z),(4 ,23),(15, 4),(15,30),(4 ,27),(16,12),(0 , 8),(7 , 9),(3 , 6),(5 ,26),(13,28),(10,12),(13,14),(5 ,30),(3 ,27),(7 , 6),(14,15),(7 ,18)],
        [(0,Z),(0 , 4),(6 ,13),(1 ,14),(2 , 2),(9 ,11),(5 , 5),(7 ,13),(15,24),(12,16),(15,20),(7 ,24),(5 ,19),(9 ,25),(2 ,26),(1 ,20),(6 ,28),(10, 5),(14,11)],
        [(0,Z),(1 , Z),(8 ,25),(4 , 5),(6 , 6),(14, 6),(11,11),(14,22),(6 , 2),(4 , 2),(8 ,14),(1 ,13),(0 , 3),(5 , 6),(16,21),(16,11),(5 , 8),(12,15),(10,20)], # 12,14->12,15
        [(0,Z),(2 , Z),(10,19),(7 ,29),(10,22),(2 ,23),(0 ,15),(4 ,19),(14, 6),(13,14),(1 , 5),(12,24),(12, 8),(1 , 4),(13, 1),(14,21),(4 ,17),(3 , 3),(12,27)],
    ]

    Y = [None, 0, 1, 2, 18, 5, 11, 4, 13, 26, 25, 29, 24, 7, 20, 19, 9, 12, 15]

    return OA_n_times_2_pow_c_from_matrix(20,5,FiniteField(17),zip(*A),Y,check=False)

def OA_17_560():
    r"""
    Returns an OA(17,560)

    This OA is built in Corollary 2.2 of [Thwarts]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_17_560
        sage: OA = OA_17_560()
        sage: print is_orthogonal_array(OA,17,560,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(17,560,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField as GF
    alpha = 5
    beta  = 4
    p     = 2
    k     = 17
    m     = 16
    n     = p**alpha

    G = GF(p**alpha,prefix='x',conway=True)
    G_set = sorted(G) # sorted by lexicographic order, G[1] = 1
    G_to_int = {v:i for i,v in enumerate(G_set)}
    # Builds an OA(n+1,n) whose last n-1 colums are
    #
    # \forall x \in G and x!=0, C_x(i,j) = i+x*j
    #
    # (only the necessary columns are built)
    OA = [[G_to_int[i+x*j] for i in G_set for j in G_set] for x in G_set[k+1:0:-1]]
    OA.append([j for i in range(n) for j in range(n)])
    OA.append([i for i in range(n) for j in range(n)])

    # The additive group F_{p^beta} appears in F_{p^alpha} as all polynomials
    # with degree < beta
    #
    # We remove all elements except those from F_{p^alpha} in the last three
    # columns

    elements_of_subgroup = set([x for x in G_set if x.polynomial().degree() < beta])
    relabel = {G_to_int[v]:i for i,v in enumerate(elements_of_subgroup)}
    for x in range(p**alpha):
        if x not in relabel:
            relabel[x] = None

    for C in OA[-3:]:
        for i,x in enumerate(C):
            C[i] = relabel[x]

    OA=zip(*OA)

    return wilson_construction(OA,k,n,m,3,[p**beta]*3,check=False)

def OA_11_640():
    r"""
    Returns an OA(11,640)

    Published by Julian R. Abel in [AbelThesis]_ (uses the fact that `640=2^7
    \times 5` is the product of a power of `2` and a prime number).

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_11_640
        sage: OA = OA_11_640()                        # not tested (too long)
        sage: print is_orthogonal_array(OA,11,640,2)  # not tested (too long)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(11,640,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (1,None), (4,None), (4,None), (1,None)],
        [(0,None), (1,None), (2,   7), (3,  55), (4,  54), (1,  87), (0, 124), (1, 123), (4,  83), (4,  61)], # 0,25 became 0,124
        [(0,None), (2,None), (4,  14), (1,  63), (3,   6), (4,  87), (1,  16), (0,  47), (1,  29), (4,  16)],
        [(0,None), (3,None), (1,   1), (4,  15), (2,   5), (4,  32), (4,  30), (1,   3), (0,  12), (1,  14)],
        [(0,None), (4,None), (3,  28), (2,  62), (1,  64), (1,  55), (4,  63), (4,   4), (1,   0), (0,   0)],
        [(0,None), (2,   6), (3,   8), (3,   7), (2,  12), (0,   1), (2,   6), (3,  97), (3,  45), (2,   0)],
        [(0,None), (3,   6), (0,  63), (1,   5), (1,   6), (2,  97), (0,  28), (2,  63), (3,   0), (3,   2)],
        [(0,None), (4,   6), (2,   4), (4,  65), (0,   6), (3,  68), (2,   1), (0,  14), (2,   1), (3,   0)],
        [(0,None), (0,   6), (4,   9), (2,None), (4,  29), (3,  15), (3,   0), (2,   1), (0,   7), (2,   4)],
        [(0,None), (1,   6), (1,  14), (0,  14), (3,   4), (2,   0), (3,None), (3,   4), (2,   0), (0,None)]
    ]
    Y = [None, 0, 1, 2, 121, 66, 77, 78, 41, 100]

    return OA_n_times_2_pow_c_from_matrix(11,7,FiniteField(5),zip(*A),Y,check=False)

def OA_10_796():
    r"""
    Returns an OA(10,796)

    Construction shared by Julian R. Abel, from [AC07]_:

        Truncate one block of a `TD(17,47)` to size `13`, then add an extra
        point. Form a block on each group plus the extra point: we obtain a
        `(796, \{13,16,17,47,48\})`-PBD in which only the extra point lies in
        more than one block of size `48` (and each other point lies in exactly 1
        such block).

        For each block `B` (of size `k` say) not containing the extra point,
        construct a `TD(10, k) - k.TD(k,1)` on `I(10) X B`.  For each block `B`
        (of size `k=47` or `48`) containing the extra point, construct a
        `TD(10,k) - TD(k,1)` on `I(10) X B`, the size `1` hole being on `I(10) X
        P` where `P` is the extra point. Finally form `1` extra block of size
        `10` on `I(10) X P`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_796
        sage: OA = OA_10_796()
        sage: print is_orthogonal_array(OA,10,796,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(10,796,existence=True)
        True
    """
    from sage.combinat.designs.orthogonal_arrays import OA_relabel
    from sage.combinat.designs.orthogonal_arrays import OA_from_PBD
    from orthogonal_arrays import incomplete_orthogonal_array

    OA = orthogonal_array(17,47)
    OA = OA_relabel(OA,17,47,blocks=[OA[0]]) # making sure [46]*17 is a block
    PBD = [[i*47+x for i,x in enumerate(B) if (x<46 or i<13)] for B in OA]
    extra_point = 10000
    PBD.extend([range(i*47,(i+1)*47-int(i>=13))+[extra_point] for i in range(17)]) # Adding the columns

    rel = {v:i for i,v in enumerate(set(range(17*47)).difference([(i+1)*47-1 for i in range(13,17)]))}
    rel[extra_point] = len(rel)

    PBD = [[rel[x] for x in B] for B in PBD]
    assert set(map(len,PBD)) == set([13, 16, 17, 47, 48])
    extra_point = rel[extra_point]

    others = []
    OA = []
    span = set()
    iOA = {47: incomplete_orthogonal_array(10,47,(1,)),
           48: incomplete_orthogonal_array(10,48,(1,))}

    for B in PBD:
        if len(B) >= 47:
            B.sort(key=lambda x:int(x==extra_point))
            OA.extend([[B[i] for i in BB] for BB in iOA[len(B)]])
            span.update(B[:-1])
        else:
            others.append(B)

    OA.extend(OA_from_PBD(10,796,others,check=False))
    OA = OA[:-796] # removes the [x]*k

    for x in set(range(796)).difference(span):
        OA.append([x]*10)

    return OA

def OA_10_469():
    r"""
    Return an OA(10,469)

    This construction appears in [Brouwer80]_. It is based on the same technique
    used in
    :func:`~sage.combinat.designs.orthogonal_arrays_recursive.brouwer_separable_design`.

    Julian R. Abel's instructions:

        Brouwer notes that a cyclic `PG(2,37)` (or `(1407,38,1)`-BIBD) can be
        obtained with a base block containing `13,9,` and `16` points in each
        residue class mod 3. Thus, by reducing the `PG(2,37)` to its points
        congruent to `0 \pmod 3` one obtains a `(469,\{9,13,16\})`-PBD which
        consists in 3 symmetric designs, i.e. 469 blocks of size 9, 469 blocks
        of size 13, and 469 blocks of size 16.

        For each block size `s`, one can build a matrix with size `s\times 469`
        in which each block is a row, and such that each point of the PBD
        appears once per column. By multiplying a row of an `OA(9,s)-s.OA(9,1)`
        with the rows of the matrix one obtains a parallel class of a resolvable
        `OA(9,469)`.

        Add to this the parallel class of all blocks `(0,0,...),(1,1,...),...`
        to obtain a resolvable `OA(9,469)` equivalent to an `OA(10,469)`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_469
        sage: OA = OA_10_469()
        sage: print is_orthogonal_array(OA,10,469,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(10,469,existence=True)
        True
    """
    from orthogonal_arrays_recursive import _reorder_matrix
    from orthogonal_arrays import incomplete_orthogonal_array

    OA = []

    # A cyclic (1407,38,1)-BIBD
    B = (0,1,27,44,63,69,102,149,237,249,395,436,510,515,525,533,547,592,665,
         731,824,837,848,932,1002,1051,1055,1089,1105,1145,1165,1196,1217,1226,
         1274,1281,1309,1405)

    BIBD = [[(x+i)%1407 for x in B]  for i in range(1407)]

    # Only keep points v congruent to 0 mod 3 and relabel
    PBD = [[x//3 for x in B if x%3==0] for B in BIBD]

    # Split the block according to their size
    blocks = {9:[],13:[],16:[]}
    for B in PBD:
        blocks[len(B)].append(B)

    # Product of each symmetric design with the OA
    for b_size,symmetric_design in blocks.iteritems():
        matrix = _reorder_matrix(symmetric_design)
        OA.extend([[B[xx] for xx in R]
                   for R in incomplete_orthogonal_array(9,b_size,[1]*b_size)
                   for B in matrix])

    # Last parallel class
    OA.extend([[i]*9 for i in range(469)])

    for i,R in enumerate(OA):
        R.append(i//469)

    return OA

def OA_520_plus_x(x):
    r"""
    Return an `OA(10+x,520+x)`.

    The consruction shared by Julian R. Abel can build three designs:
    `OA(10,520), OA(12,522), OA(14,524)`.

        Let `n=520+x` and `k=10+x`. Build a `TD(17,31)`. Remove `8-x` points
        contained in a common block, add a new point `p` and create a block
        `g_i\cup \{p\}` for every (possibly truncated) group `g_i`. The result
        is a `(520+x,{9+x,16,17,31,32})-PBD`. Note that all blocks of size `\geq
        30` only intersect on `p`, and that the unique block `B_9` of size `9`
        intersects all blocks of size `32` on one point. Now:

        * Build an `OA(k,16)-16.OA(k,16)` for each block of size 16

        * Build an `OA(k,17)-17.OA(k,17)` for each block of size 17

        * Build an `OA(k,31)-OA(k,1)` for each block of size 31 (with the hole on
          `p`).

        * Build an `OA(k,32)-2.OA(k,1)` for each block `B` of size 32 (with the
          holes on `p` and `B\cap B_9`).

        * Build an `OA(k,9)` on `B_9`.

        Only a row `[p,p,...]` is missing from the `OA(10+x,520+x)`

    This construction is used in :func:`OA(10,520) <OA_10_520>`,
    :func:`OA(12,522) <OA_12_522>`, and :func:`OA(14,524) <OA_10_524>`.

    EXAMPLE::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_520_plus_x
        sage: OA = OA_520_plus_x(0)                   # not tested (already tested in OA_10_520
        sage: print is_orthogonal_array(OA,10,520,2)  # not tested (already tested in OA_10_520
        True

    """
    from orthogonal_arrays import incomplete_orthogonal_array
    k = 9+x+1

    # The OA(17,31) with a block [30,30,...]
    OA = incomplete_orthogonal_array(17,31,[1])
    OA.append([30]*17)

    # We truncate [30,30,...] to its first 9+x coordinates, and add sets
    # corresponding to each (possibly truncated) group extended with a new
    # point. The result is a (520+x,{9+x,16,17,31,32})-PBD.
    new_point = 31*17
    PBD = [[i*31+xx for i,xx in enumerate(B) if i<9+x or xx<30] for B in OA] # truncated blocks
    PBD.extend([range(i*31,i*31+30+bool(i<9+x))+[new_point] for i in range(17)]) # extended (+truncated) groups

    relabel = {v:i for i,v in enumerate(sorted(set().union(*PBD)))}
    PBD = [[relabel[xx] for xx in B] for B in PBD]

    subdesigns = {
        9+x: orthogonal_array(k,9+x),
        16 : incomplete_orthogonal_array(k,16,[1]*16),
        17 : incomplete_orthogonal_array(k,17,[1]*17),
        31 : incomplete_orthogonal_array(k,31,[1]),
        32 : incomplete_orthogonal_array(k,32,[1]*2),
       }

    OA = []
    for B in PBD:
        OA.extend([[B[xx] for xx in R]
                   for R in subdesigns[len(B)]])

    OA.append([relabel[new_point]]*k)
    return OA

def OA_10_520():
    r"""
    Return an OA(10,520).

    This design is built by the slightly more general construction
    :func:`OA_520_plus_x`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_10_520
        sage: OA = OA_10_520()
        sage: print is_orthogonal_array(OA,10,520,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(10,520,existence=True)
        True
    """
    return OA_520_plus_x(0)

def OA_12_522():
    r"""
    Return an OA(12,522)

    This design is built by the slightly more general construction
    :func:`OA_520_plus_x`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_12_522
        sage: OA = OA_12_522()
        sage: print is_orthogonal_array(OA,12,522,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(12,522,existence=True)
        True
    """
    return OA_520_plus_x(2)

def OA_14_524():
    r"""
    Return an OA(14,524)

    This design is built by the slightly more general construction
    :func:`OA_520_plus_x`.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_14_524
        sage: OA = OA_14_524()
        sage: print is_orthogonal_array(OA,14,524,2)
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(14,524,existence=True)
        True
    """
    return OA_520_plus_x(4)

def OA_15_896():
    r"""
    Returns an OA(15,896)

    Uses the fact that `896 = 2^7 \times 7` is the product of a power of `2` and
    a prime number.

    .. SEEALSO::

        :func:`sage.combinat.designs.orthogonal_arrays.OA_n_times_2_pow_c_from_matrix`

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_15_896
        sage: OA = OA_15_896()                          # not tested -- too long (~2min)
        sage: print is_orthogonal_array(OA,15,896,2)    # not tested -- too long
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(15,896,existence=True)
        True
    """
    from sage.rings.finite_rings.constructor import FiniteField

    A = [
        [(0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (0,None), (1,None), (4,None), (2,None), (2,None), (4,None), (1,None)],
        [(0,None), (1,None), (2,  17), (3,  20), (4,  49), (5,   4), (6,  59), (1,  15), (0, 114), (1,  76), (4, 106), (2,  87), (2, 118), (4,  49)], # 4,120 became the leftmost 4,49
        [(0,None), (2,None), (4,   2), (6,  98), (1,  53), (3,  97), (5, 123), (4,   3), (1,  32), (0,  10), (1,  45), (4,   3), (2,   1), (2,  14)],
        [(0,None), (3,None), (6,  16), (2,  86), (5, 102), (1,  64), (4,  69), (2,  11), (4,  55), (1,  90), (0, 115), (1,  15), (4,   7), (2,   0)],
        [(0,None), (4,None), (1,   4), (5, 110), (2,  51), (6, 118), (3,   8), (2,  81), (2,  79), (4,  98), (1,   2), (0,   3), (1,   7), (4,None)],
        [(0,None), (5,None), (3,  66), (1,  70), (6, 102), (4, 119), (2,  20), (4,  86), (2,  59), (2,  15), (4,  63), (1, 126), (0,   1), (1,   0)],
        [(0,None), (6,None), (5,  94), (4,  48), (3,  90), (2,   2), (1,  13), (1,  53), (4, 117), (2,  21), (2,   2), (4,   1), (1,   0), (0,   0)],
        [(0,None), (4,   6), (2,  21), (1, 112), (1,  36), (2,  14), (4,  60), (0,   1), (6,  64), (3,   0), (5,  31), (5,   3), (3,   3), (6,  14)],
        [(0,None), (5,   6), (4,  61), (4,None), (5, 108), (0,  91), (3,  10), (6,  15), (0,None), (6,  15), (3,   7), (5,   0), (5,   1), (3,   0)],
        [(0,None), (6,   6), (6, 107), (0,  88), (2,  12), (5,  44), (2,  31), (3,  64), (6,   0), (0,None), (6,   2), (3,   3), (5,None), (5,   0)],
        [(0,None), (0,   6), (1,  52), (3, 115), (6,  30), (3,  78), (1,  64), (5,  63), (3,   5), (6,None), (0,None), (6,   3), (3,   1), (5,None)],
        [(0,None), (1,   6), (3, 117), (6,  19), (3,   9), (1,  31), (0,  56), (5,   0), (5,  63), (3,None), (6,None), (0,None), (6,   7), (3,None)],
        [(0,None), (2,   6), (5, 116), (2,   3), (0,   0), (6,None), (6,   1), (3,   0), (5,   0), (5,   2), (3,None), (6,None), (0,None), (6,   0)],
        [(0,None), (3,   6), (0,   0), (5,   0), (4,   1), (4,None), (5,None), (6,   0), (3,   2), (5,   0), (5,None), (3,None), (6,None), (0,None)] # 0,0 became the rightmost 0,None
    ]

    Y = [None, 0,1,2,121,66,77,78,41,100,74,118,108,43]

    return OA_n_times_2_pow_c_from_matrix(15,7,FiniteField(7),zip(*A),Y,check=False)

def OA_25_1262():
    r"""
    Returns an OA(25,1262)

    The construction is given in [Greig99]_. In Julian R. Abel's words:

        Start with a cyclic `PG(2,43)` or `(1893,44,1)`-BIBD whose base block
        contains respectively `12,13` and `19` point in the residue classes mod
        3. In the resulting BIBD, remove one of the three classes: the result is
        a `(1262, \{25, 31,32\})`-PBD, from which the `OA(25,1262)` is obtained.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_orthogonal_array
        sage: from sage.combinat.designs.database import OA_25_1262
        sage: OA = OA_25_1262()                       # not tested -- too long
        sage: print is_orthogonal_array(OA,25,1262,2) # not tested -- too long
        True

    The design is available from the general constructor::

        sage: designs.orthogonal_array(25,1262,existence=True)
        True
    """

    from sage.combinat.designs.orthogonal_arrays import OA_from_PBD
    B = (0, 68, 78, 106, 227, 296, 304, 330, 354, 411, 624, 631, 636, 732, 747,
         772, 794, 846, 869, 939, 948, 1011, 1015, 1031, 1135, 1171, 1188, 1206,
         1217, 1219, 1220, 1261, 1306, 1349, 1370, 1400, 1461, 1480, 1517, 1714,
         1768, 1827, 1833, 1866)

    BIBD = [[(x+i)%1893 for x in B] for i in range(1893)] # a (1893,44,1)-BIBD
    PBD = [[x for x in B if (x%3)<2] for B in BIBD]       # We only keep the x with x%3=0,1
    PBD = [[2*(x//3)+(x%3) for x in B] for B in PBD]      # The (1262, {25, 31,32})-PBD

    return OA_from_PBD(25,1262,PBD,check=False)

# Index of the OA constructions
#
# Associates to n the pair (k,f) where f() is a function that returns an OA(k,n)
#
# This dictionary is used by designs.orthogonal_array(k,n).

OA_constructions = {
    18  : (7  , OA_7_18),
    20  : (6  , OA_6_20),
    22  : (5  , OA_5_22),
    26  : (6  , OA_6_26),
    30  : (6  , OA_6_30),
    34  : (6  , OA_6_34),
    38  : (6  , OA_6_38),
    40  : (9  , OA_9_40),
    42  : (7  , OA_7_42),
    54  : (7  , OA_7_54),
    62  : (7  , OA_7_62),
    65  : (9  , OA_9_65),
    66  : (7  , OA_7_66),
    68  : (7  , OA_7_68),
    69  : (8  , OA_8_69),
    74  : (7  , OA_7_74),
    76  : (8  , OA_8_76),
    80  : (11 , OA_11_80),
    112 : (15 , OA_15_112),
    120 : (9  , OA_9_120),
    135 : (9  , OA_9_135),
    160 : (11 , OA_11_160),
    176 : (16 , OA_16_176),
    185 : (11 , OA_11_185),
    205 : (10 , OA_10_205),
    208 : (16 , OA_16_208),
    224 : (15 , OA_15_224),
    254 : (11 , OA_11_254),
    352 : (20 , OA_20_352),
    416 : (20 , OA_20_416),
    469 : (10 , OA_10_469),
    514 : (9  , OA_9_514),
    520 : (10 , OA_10_520),
    522 : (12 , OA_12_522),
    524 : (14 , OA_14_524),
    544 : (20 , OA_20_544),
    560 : (17 , OA_17_560),
    640 : (11 , OA_11_640),
    796 : (10 , OA_10_796),
    896 : (15 , OA_15_896),
    1262 : (25 , OA_25_1262),
}
# Add this data to the module's doc
LIST_OF_OA_CONSTRUCTIONS = join((":func:`OA({},{}) <OA_{}_{}>`".format(k,n,k,n)
                                for n,(k,_) in OA_constructions.items()),
                               ", ")

Vmt_vectors = {
    (4,9) : ((0,1,3,2,8),
             """A. Brouwer and J. van Rees, More mutually orthogonal Latin squares,
             Discrete Mathematics 1982, vol 39, num 3, pp 263-281"""),

    (6,7) : ((0,1,3,16,35,26,36),
             """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
             Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (8,9) : ((0,1,20,70,23,59,3,8,19),
             """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
             Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (8,11) : ((0,1,6,56,22,35,47,23,60),
              """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
              Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (8,17) : ((0,1,3,2,133,126,47,109,74),
              """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
              Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (8,29) : ((0,1,4,11,94,60,85,16,198),
              """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
              Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,13) : ((0,1,5,10,22,6,14,9,53,129,84),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,19) : ((0,1,3,96,143,156,182,142,4,189,25),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,25) : ((0,1,3,85,140,178,195,22,48,179,188),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,27) : ((0,1,3,82,109,241,36,112,141,263,126),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,31) : ((0,1,3,57,128,247,289,239,70,271,96),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,43) : ((0,1,6,29,170,207,385,290,375,32,336),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10, 81) : ((0,1,3,2,27,438,615,708,168,410,656),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10, 97) : ((0,1,3,6,11,274,772,340,707,157,556),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,103) : ((0,1,3,2,7,744,342,797,468,46,561),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,181) : ((0,1,3,8,5,68,514,16,1168,225,929),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,187) : ((0,1,3,7,2,325,1138,730,1013,534,366),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,259) : ((0,1,3,7,2,15,324,1956,1353,2041,1616),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,273) : ((0,1,3,6,11,28,2573,38,1215,1299,2468),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,319) : ((0,1,3,7,2,43,239,1335,1586,2724,63),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,391) : ((0,1,3,2,5,32,555,3450,1242,1823,3833),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (10,409) : ((0,1,3,2,5,11,505,3202,1502,2521,3023),
               """Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
               Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104"""),

    (12,73) : ((0,1,607,719,837,496,240,645,184,829,451,830,770),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40 pp 69-85"""),

    (12, 83) : ((0,1,627,898,836,939,742,42,847,531,173,607,361),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12, 89) : ((0,1,602,894,827,661,350,647,304,47,430,533,550),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,101) : ((0,1,787,1049,818,1064,288,346,464,958,1188,340,1192),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,103) : ((0,1,770,1027,806,1082,515,436,1096,1060,57,1135,1144),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,121) : ((0,1,713,1265,848,421,998,69,874,1126,693,467,1164),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,169) : ((0,1,425,326,951,1211,1881,1063,1631,1363,1554,665,1600),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,191) : ((0,1,491,527,939,377,1685,1735,1967,1176,391,2192,681),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,199) : ((0,1,377,524,946,560,316,1591,2036,273,1841,2091,713),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

    (12,229) : ((0,1,338,312,933,380,401,2398,612,1279,1514,268,528),
               """J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
               Australasian Journal of Combinatorics 2008, vol 40, pp 69-85"""),

}
# Translate all V(m,t) into OA constructors
for (m,t),(vec,source) in Vmt_vectors.iteritems():
    OA_constructions[(m+1)*t+1] = (m+2, lambda m=m,t=t,vec=vec:OA_from_Vmt(m,t,vec))

# Create the list of V(m,t) vectors for the doc
_all_m = sorted(set(m for m,_ in Vmt_vectors.keys()))
LIST_OF_VMT_VECTORS = join(("    - `m={}` and `t=` ".format(m)+
                           join(("`{}`".format(t) for _,t in sorted(Vmt_vectors.keys()) if _ == m),", ")
                           for m in _all_m), "\n")

r""""
Tests for the Vmt vectors

EXAMPLES::

    sage: from sage.combinat.designs.orthogonal_arrays import is_orthogonal_array
    sage: from sage.combinat.designs.orthogonal_arrays import OA_from_Vmt
    sage: from sage.combinat.designs.database import Vmt_vectors
    sage: for (m,t),(vec,source) in sorted(Vmt_vectors.items()):
    ....:     k,n = m+2,(m+1)*t+1
    ....:     if n < 1000:
    ....:         assert is_orthogonal_array(OA_from_Vmt(m,t,vec),k,n)
    ....:     print "{:11}{}".format("V({},{}):".format(m,t),source)
    V(4,9):    A. Brouwer and J. van Rees, More mutually orthogonal Latin squares,
                 Discrete Mathematics 1982, vol 39, num 3, pp 263-281
    V(6,7):    Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                 Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(8,9):    Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                 Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(8,11):   Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                  Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(8,17):   Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                  Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(8,29):   Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                  Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,13):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,19):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,25):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,27):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,31):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,43):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,81):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,97):  Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,103): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,181): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,187): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,259): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,273): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,319): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,391): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(10,409): Charles J. Colbourn, Some direct constructions for incomplete transversal designs,
                   Journal of Statistical Planning and Inference, vol 56, num 1, pp 93-104
    V(12,73):  J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40 pp 69-85
    V(12,83):  J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,89):  J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,101): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,103): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,121): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,169): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,191): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,199): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
    V(12,229): J.R. Abel, Some V(12,t) vectors and designs from difference and quasi-difference matrices,
                   Australasian Journal of Combinatorics 2008, vol 40, pp 69-85
"""


DF = {
##############
# lambda = 1 #
##############
( 15, 3, 1):
  {(15,): [[0,1,4],[0,2,9],[0,5,10]]},
( 21, 3, 1):
  {(21,): [[0,1,3],[0,4,12],[0,5,11],[0,7,14]]},
( 21, 5, 1):
  {(21,): [[0,1,4,14,16]]},
( 25, 3, 1):
  {(25,): [[0,1,3],[0,4,11],[0,5,13],[0,6,15]]},
( 25, 4, 1):
  {(5,5): [[(0,0),(0,1),(1,0),(2,2)],[(0,0),(0,2),(2,0),(4,4)]]},
( 27, 3, 1):
  {(27,): [[0,1,3],[0,4,11],[0,5,15],[0,6,14],[0,9,18]]},
( 33, 3, 1):
  {(33,): [[0,1,3],[0,4,10],[0,5,18],[0,7,19],[0,8,17],[0,11,22]]},
( 37, 4, 1):
  {(37,): [[0,1,3,24],[0,4,26,32],[0,10,18,30]]},
( 39, 3, 1):
  {(39,): [[0,1,3],[0,4,18],[0,5,27],[0,6,16],[0,7,15],[0,9,20],[0,13,26]]},
( 40, 4, 1):
  {(40,): [[0,1,4,13],[0,2,7,24],[0,6,14,25],[0,10,20,30]]},
( 45, 3, 1):
  {(45,): [[0,1,3],[0,4,10],[0,5,28],[0,7,34],[0,8,32],[0,9,29],[0,12,26],[0,15,30]]},
( 45, 5, 1):
  {(3,3,5): [[(0,1,0),(0,2,0),(1,0,2),(2,0,2),(0,0,1)],
             [(2,1,0),(1,2,0),(2,2,2),(1,1,2),(0,0,1)],
             [(0,0,0),(0,0,1),(0,0,2),(0,0,3),(0,0,4)]]},
( 49, 3, 1):
  {(49,): [[0,1,3],[0,4,9],[0,6,17],[0,7,23],[0,8,30],[0,10,31],[0,12,36],[0,14,34]]},
( 49, 4, 1):
  {(49,): [[0,1,3,8,],[0,4,18,29],[0,6,21,33],[0,9,19,32]]},
( 51, 3, 1):
  {(51,): [[0,1,3],[0,4,9],[0,6,25],[0,7,35],
           [0,8,22],[0,10,21],[0,12,27],[0,13,31],[0,17,34]]},
( 52, 4, 1):
  {(52,): [[0,1,3,7,],[0,5,19,35],[0,8,20,31],[0,9,24,34],[0,13,26,39]]},
( 55, 3, 1):
  {(55,): [[0,1,3],[0,4,9],[0,6,16],[0,7,32],[0,8,29],
           [0,11,42],[0,12,27],[0,14,36],[0,17,37]]},
( 57, 3, 1):
  {(57,): [[0,1,3],[0,4,9],[0,6,13],[0,8,26],[0,10,33],
           [0,11,32],[0,12,40],[0,14,41],[0,15,35],[0,19,38]]},
( 63, 3, 1):
  {(63,): [[0,1,3],[0,4,9],[0,6,13],[0,8,25],[0,10,41],[0,11,44],
          [0,12,36],[0,14,37],[0,15,43],[0,16,34],[0,21,42]]},
( 64, 4, 1):
  {(64,): [[0,1,3,7,],[0,5,18,47],[0,8,33,44],
           [0,9,19,43],[0,12,26,49],[0,16,32,48]]},
( 65, 5, 1):
  {(65,): [[0,1,3,31,45],[0,4,10,19,57],[0,5,16,41,48],[0,13,26,39,52]]},
( 69, 3, 1):
  {(69,): [[0,1,3],[0,4,9],[0,6,13],[0,8,24],[0,10,38],[0,11,47],[0,12,32],
          [0,14,40],[0,15,50],[0,17,42],[0,18,39],[0,23,46]]},
( 75, 3, 1):
  {(75,): [[0,1,67],[0,2,47],[0,3,41],[0,4,69],[0,5,68],[0,11,55],[0,13,61],
          [0,15,33],[0,16,52],[0,17,43],[0,19,40],[0,22,51],[0,25,50]]},
( 76, 4, 1):
  {(76,): [[0,1,7,22],[0,2,11,45],[0,3,59,71],[0,4,32,50],
           [0,10,37,51],[0,13,36,60],[0,19,38,57]]},
( 81, 3, 1):
  {(81,): [[0,1,39],[0,2,58],[0,3,34],[0,4,21],[0,5,67],[0,6,15],[0,7,36],
           [0,8,59],[0,10,63],[0,11,37],[0,12,61],[0,13,48],[0,16,40],[0,27,54]]},
( 81, 5, 1):
  {(81,): [[0,1,5,12,26],[0,2,10,40,64],[0,3,18,47,53],[0,9,32,48,68]]},
( 85, 4, 1):
  {(85,): [[0,2,41,42],[0,17,32,38],[0,18,27,37],[0,13,29,36],
           [0,11,31,35],[0,12,26,34,],[0,5,30,33]]},
( 91, 6, 1):
  {(91,): [[0,1,3,7,25,38], [0,16,21,36,48,62], [0,30,40,63,74,82]]},
(121, 5, 1):
  {(121,): [[0,14,26,51,60],[0,15,31,55,59],[0,10,23,52,58],
            [0,3,36,56,57],[0,7,18,45,50],[0,8,30,47,49]]},
(121, 6, 1):
  {(11,11): [[(0,0),(0,3),(0,4),(1,1),(1,7),(4,6)],
             [(0,0),(0,2),(2,5),(4,7),(6,4),(8,0)],
             [(0,0),(1,5),(2,0),(4,1),(6,0),(7,2)],
             [(0,0),(1,0),(3,9),(4,8),(6,1),(9,5)]]},
(141, 5, 1):
  {(141,): [[0,33,60,92,97],[0,3,45,88,110],[0,18,39,68,139],[0,12,67,75,113],
            [0,1,15,84,94],[0,7,11,24,30],[0,36,90,116,125]]},
(161, 5, 1):
  {(161,): [[0,19,34,73,80],[0,16,44,71,79],[0,12,33,74,78],[0,13,30,72,77],
            [0,11,36,67,76],[0,18,32,69,75],[0,10,48,68,70],[0,3,29,52,53]]},
(175, 7, 1):
  {(7,5,5): [[(0,0,0),(1,0,0),(2,0,0),(3,0,0),(4,0,0),(5,0,0),(6,0,0)],
             [(0,0,0),(1,1,3),(1,4,2),(2,2,2),(2,3,3),(4,2,0),(4,3,0)],
             [(0,0,0),(1,3,4),(1,2,1),(2,2,3),(2,3,2),(4,0,2),(4,0,3)],
             [(0,0,0),(1,1,2),(1,4,3),(2,1,1),(2,4,4),(4,0,1),(4,0,4)],
             [(0,0,0),(1,3,1),(1,2,4),(2,4,1),(2,1,4),(4,1,0),(4,4,0)]]},
(201, 5, 1):
  {(201,): [[0,1,45,98,100],[0,3,32,65,89],[0,4,54,70,75],[0,6,49,69,91],[0,7,58,81,95],
            [0,8,34,72,90],[0,9,36,77,96],[0,10,35,83,94],[0,12,40,79,92],[0,15,46,76,93]]},
(217, 7, 1):
  {(217,): [[0,1,37,67,88,92,149],[0,15,18,65,78,121,137],[0,8,53,79,85,102,107],
            [0,11,86,100,120,144,190],[0,29,64,165,198,205,207],[0,31,62,93,124,155,186]]},
(221, 5, 1):
  {(221,): [[0,1,24,61,116],[0,3,46,65,113],[0,4,73,89,130],[0,5,77,122,124],
            [0,6,39,50,118],[0,7,66,81,94],[0,8,38,64,139],[0,9,29,80,107],
            [0,10,35,93,135],[0,12,34,52,88],[0,14,31,63,84]]},

(259, 7, 1): # the following one is lemma 2.2 in Abel "Some new BIBDs with block size 7"
  {(7,37): [[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)],
            [(0,0),(0,1),(0,6),(1,4),(2,19),(3,25),(6,26)],
            [(0,0),(0,10),(0,23),(2,3),(4,5),(5,1),(6,28)],
            [(0,0),(0,8),(0,26),(1,13),(3,10),(4,30),(5,21)],
            [(0,0),(0,4),(1,25),(1,34),(2,33),(2,35),(4,10)],
            [(0,0),(0,3),(1,26),(2,7),(2,28),(4,17),(4,34)],
            [(0,0),(0,30),(1,7),(1,22),(2,1),(4,21),(4,33)]]},

##############
# lambda = 2 #
##############
( 16, 3, 2):
  {(16,): [[0,1,2],[0,2,8],[0,3,7],[0,4,7],[0,5,10]]},
( 28, 3, 2):
  {(28,): [[0,1,12],[0,2,11],[0,2,12],[0,3,7],[0,3,13],
           [0,4,9],[0,5,13],[0,6,7],[0,6,14]]},
( 40, 3, 2):
  {(40,): [[0,1,4],[0,1,16],[0,2,7],[0,2,9],[0,3,17],[0,4,17],[0,5,19],
           [0,6,16],[0,6,18],[0,8,18],[0,8,19],[0,9,20],[0,12,25]]},
( 19, 4, 2):
  {(19,): [[0,1,3,12],[0,1,5,13],[0,4,6,9]]},
( 21, 4, 3):
  {(21,): [[0,2,3,7],[0,3,5,9],[0,1,7,11],[0,2,8,11],[0,1,9,14]]},
( 22, 4, 2):
  {(22,): [[0,4,16,17],[0,12,14,21],[0,14,16,19],[0,4,11,15]]},
( 31, 4, 2):
  {(31,): [[0,1,8,11],[0,1,13,17],[0,2,11,14],[0,5,7,13],[0,5,9,15]]},
( 34, 4, 2):
  {(34,): [[0,1,22,24],[0,1,19,25],[0,2,6,29],[0,4,7,20],[0,5,8,20],[0,8,17,25]]},
( 43, 4, 2):
  {(43,): [[0,1,6,36],[0,3,18,22],[0,9,11,23],[0,10,12,26],[0,26,27,33],
           [0,13,35,38],[0,19,28,39,]]},
( 46, 4, 2):
  {(46,): [[0,2,7,10],[0,4,19,32],[0,10,34,35],[0,5,8,24],[0,26,30,39],
           [0,17,26,32],[0,28,34,45],[0,2,23,25]]},
(31, 5, 2):
  {(31,): [[0,1,3,7,15],[0,3,9,14,21],[0,4,5,13,15,]]},
( 35, 5, 2):
  {(35,): [[0,2,8,12,13],[0,3,18,22,27],[0,17,23,32,33],
           [0,7,14,21,28],[0,7,14,21,28]]},
( 51, 5, 2):
  {(51,): [[0,1,14,31,35],[0,1,9,23,33],[0,11,16,18,42],
           [0,7,13,36,39],[0,4,10,12,15]]},
( 71, 5, 2):
  {(71,): [[1,5,25,54,57],[3,4,15,20,29],[9,12,16,45,60],[27,36,38,48,64],
           [2,10,37,43,50],[6,8,30,40,58],[18,19,24,32,49]]},
( 46, 6, 2):
  {(46,): [[0,1,3,11,31,35],[0,1,4,10,23,29],[0,2,7,15,32,41]]},
( 61, 6, 2):
  {(61,): [[12,15,28,34,35,59],[1,13,18,47,51,53],
           [8,10,11,21,29,43],[16,20,25,32,40,50]]},
( 43, 7, 2):
  {(43,): [[0,1,11,19,31,38,40],[0,2,10,16,25,38,42]]},
( 64, 7, 2):
  {(64,): [[0,1,2,4,7,28,52],[0,4,9,21,31,39,53],[0,6,15,23,34,41,54]]},
( 75, 5, 2):
  {(5,15): [[(0,0),(1,10),(1,8),(4,1),(4,2)],
            [(0,0),(2,5),(2,10),(3,7),(3,13)],
            [(0,0),(1,10),(1,2),(4,4),(4,8)],
            [(0,0),(2,5),(2,10),(3,14),(3,11)],
            [(0,0),(1,4),(1,5),(4,1),(4,8)],
            [(0,0),(1,1),(1,5),(4,4),(4,2)],
            [(0,0),(2,7),(2,13),(3,1),(3,4)],
            [(0,0),(1,0),(2,0),(3,0),(4,0)],
            [(0,0),(1,0),(2,0),(3,0),(4,0)]]},
( 85, 7, 2):
  {(85,): [[0,1,11,20,32,35,39],[0,2,6,16,29,50,65],
           [0,3,9,27,55,72,80],[0,5,7,30,47,48,59]]},
( 85, 8, 2):
  {(85,): [[24,31,39,50,67,68,70,82],[20,49,51,55,56,60,72,81],
           [9,19,29,37,43,56,59,81]]},
(153, 9, 2):
  {(3,3,17): [[(0,0,0),(0,1,0),(0,2,0),(1,0,0),(1,1,0),(1,2,0),(2,0,0),(2,1,0),(2,2,0)],
              [(0,0,0),(0,1,0),(0,2,0),(1,0,0),(1,1,0),(1,2,0),(2,0,0),(2,1,0),(2,2,0)],
              [(0,0,0),(0,1,1),(0,1,16),(0,2,4),(0,2,13),(1,0,3),(1,0,14),(2,0,5),(2,0,12)],
              [(0,0,0),(0,1,2),(0,1,15),(0,2,8),(0,2,9),(1,0,6),(1,0,11),(2,0,10),(2,0,7)],
              [(0,0,0),(0,1,3),(0,1,14),(0,2,12),(0,2,5),(1,0,9),(1,0,8),(2,0,15),(2,0,2)],
              [(0,0,0),(0,1,6),(0,1,11),(0,2,7),(0,2,10),(1,0,1),(1,0,16),(2,0,13),(2,0,4)]]},
(181,10, 2):
  {(181,): [[1,7,40,42,51,59,113,125,135,151],
            [19,22,31,35,36,64,74,133,154,156],
            [10,15,34,47,58,65,83,87,161,164],
            [12,18,32,52,77,78,142,157,165,172]]},

##############
# lambda = 3 #
##############

( 21, 6, 3):
  {(21,): [[0,2,10,15,19,20],[0,3,7,9,10,16]]},
( 41, 6, 3):
  {(41,): [[0,1,10,16,18,37],[0,6,14,17,19,26],
           [0,2,20,32,33,36],[0,11,12,28,34,38]]},
( 51, 6, 3):
  {(51,): [[15,17,18,27,34,48],[3,17,30,34,42,45],[9,17,24,33,34,39],
           [3,25,41,43,44,48],[3,5,25,29,43,48]]},
( 61, 6, 3):
  {(61,): [[0,1,9,20,58,34],[0,2,7,18,40,55],[0,4,14,19,36,49],
           [0,8,11,28,37,38],[0,13,15,16,22,56],[0,26,30,32,44,51]]},
( 29, 7, 3):
  {(29,): [[1,7,16,20,23,24,25],[2,3,11,14,17,19,21]]},
( 43, 7, 3):
  {(43,): [[1,4,11,16,21,35,41],[3,5,12,19,20,33,37],[9,13,14,15,17,25,36]]},
( 57, 7, 3):
  {(57,): [[0,1,11,12,15,35,53],[0,7,17,20,27,29,48],
           [0,5,18,26,32,49,51],[0,2,6,9,14,41,42]]},
( 61,10, 3):
  {(61,): [[1,4,18,20,32,35,36,41,42,54],[11,13,14,21,23,28,34,39,43,47]]},
( 71, 7, 3):
  {(71,): [[1,20,30,32,37,45,48],[2,3,19,25,40,60,64],[4,6,9,38,49,50,57],
           [5,8,12,18,27,29,43],[10,15,16,24,36,54,58]]},
( 85, 7, 3):
  {(85,): [[0,7,23,27,28,31,71],[0,12,22,41,61,74,79],
           [0,6,11,13,38,42,77],[0,1,7,16,19,27,49],
           [0,9,26,39,54,56,71],[0,2,3,12,37,53,63]]},
( 97, 9, 3):
  {(97,): [[1,2,25,35,46,58,61,70,90],[3,4,8,38,43,50,69,86,87],
           [6,12,16,32,53,55,57,75,82],[9,18,24,26,31,34,37,48,64]]},
( 49, 9, 3):
  {(49,): [[0,1,3,5,9,14,19,25,37],[0,2,12,13,16,19,34,41,42]]},
(121,10, 3):
  {(11,11): [[(0,1),(0,3),(0,4),(0,5),(0,9),(1,8),(3,2),(4,10),(5,7),(9,6)],
             [(1,2),(3,6),(4,8),(5,10),(9,7),(10,2),(8,6),(7,8),(6,10),(2,7)],
             [(1,7),(3,10),(4,6),(5,2),(9,8),(1,4),(3,1),(4,5),(5,9),(9,3)],
             [(10,10),(8,8),(7,7),(6,6),(2,2),(1,0),(3,0),(4,0),(5,0),(9,0)]]},

###############
# lambda = 4  #
###############

( 22, 7, 4):
  {(22,): [[0,2,6,8,9,10,13],[0,3,5,6,12,13,17]]},
( 29, 8, 4):
  {(29,): [[0,1,7,16,20,23,24,25],[0,2,3,11,14,17,19,21]]},
( 71, 8, 4):
  {(71,): [[0,1,20,30,32,37,45,48],[0,2,3,19,25,40,60,64],
           [0,4,6,9,38,49,50,57],[0,5,8,12,18,27,29,43],
           [0,10,15,16,24,36,54,58]]},
( 43, 8, 4):
  {(43,): [[0,1,4,11,16,21,35,41],[0,3,5,12,19,20,33,37],
           [0,9,13,14,15,17,25,36]]},
( 46,10, 4):
  {(46,): [[3,7,13,16,23,24,25,28,30,42],[2,10,12,18,25,34,40,43,44,45]]},
( 55, 9, 4):
  {(55,): [[0,4,21,25,26,42,45,53,54],[0,6,8,25,37,39,45,48,52],
           [2,5,6,13,15,20,25,39,45]]},
( 67,12, 4):
  {(67,): [[1,8,23,25,28,29,31,37,47,54,55,64],
           [3,20,25,32,36,39,44,45,54,55,57,59]]},

##############
# lambda = 5 #
##############

( 13, 5, 5):
  {(13,): [[0,1,2,4,8],[0,1,3,6,12],[0,2,5,6,10]]},
( 17, 5, 5):
  {(17,): [[0,1,4,13,16],[0,3,5,12,14],[0,2,8,9,15],[0,6,7,10,11]]},
( 21, 6, 5):
  {(21,): [[0,2,6,12,15,16],[0,3,6,7,11,19],
           [0,7,15,16,17,18],[0,2,7,9,14,16]]},
( 22, 6, 5):
  {(22,): [[0,1,2,5,10,13],[0,1,5,6,8,15],
           [0,2,3,6,16,18],[0,2,6,11,13,17]]},
( 28, 6, 5):
  {(28,): [[0,4,7,8,16,21],[5,7,8,9,14,20],[7,12,14,16,17,25],
           [1,4,7,13,14,24],[2,4,8,16,18,22]]},
( 33, 5, 5):
  {(33,): [[0,2,3,7,25],[0,3,13,14,29],[0,4,5,12,13],[0,2,12,16,26],
           [0,3,12,20,31],[3,9,12,15,27],[0,8,13,14,31],[0,2,7,13,29]]},
( 33, 6, 5):
  {(33,): [[0,3,12,17,18,28],[0,2,3,16,28,29],[0,16,20,26,28,30],
           [0,2,3,12,16,27],[0,6,20,21,28,30],[0,4,11,15,22,26]]},
( 37,10, 5):
  {(37,): [[0,1,7,9,10,12,16,26,33,34],[0,2,14,15,18,20,24,29,31,32]]},
( 39, 6,5):
  {(39,): [[0,3,4,17,19,32],[0,1,5,12,30,36],[0,3,8,9,25,27],[0,7,10,12,17,21],
           [0,16,18,19,27,35],[0,2,18,27,28,33],[0,6,13,19,26,32]]},
( 45,11, 5):
  {(45,): [[1,3,7,10,22,25,30,35,37,38,44],[0,2,3,14,22,26,27,28,31,32,38]]},
( 46,10, 5):
  {(46,): [[0,4,6,11,12,15,24,25,28,42],[0,2,5,7,8,9,14,24,34,35],
           [0,2,12,32,40,23,25,35,9,17]]},
( 55,10, 5):
  {(55,): [[0,5,11,15,20,22,25,33,44,45],[3,7,8,10,31,37,39,45,46,49],
           [3,7,8,10,31,37,39,45,46,49]]},
( 67,11, 5):
  {(67,): [[1,9,14,15,22,24,25,40,59,62,64],[2,13,18,28,30,44,48,50,51,57,61],
           [4,21,26,29,33,35,36,47,55,56,60]]},
( 73,10, 5):
  {(73,): [[0,1,2,4,8,16,32,37,55,64],[0,5,7,10,14,20,28,39,40,56],
           [0,25,27,35,49,50,54,61,67,70],[0,11,15,21,22,30,42,44,47,60]]},

###############
# lambda >= 6 #
###############

( 11, 4,6):
  {(11,): [[0,1,8,9],[0,2,5,7],[0,1,4,5],[0,2,3,5],[0,4,5,9]]},
( 15, 4,6):
  {(15,): [[0,1,2,3],[0,2,4,6],[0,4,8,12],[0,8,1,9],
           [3,6,9,12],[0,1,5,10],[0,2,5,10]]},
( 15, 5,6):
  {(15,): [[0,1,2,3,6],[0,2,4,7,8],[0,2,4,9,10],
           [0,3,6,10,11],[0,3,6,9,12]]},
( 21, 8,14):
  {(21,): [[0,9,10,13,14,15,18,19],[0,1,4,7,9,15,16,18],[0,1,2,4,6,14,15,16],
           [0,1,3,4,8,14,16,18],[0,1,4,9,11,12,14,16]]},
( 21, 10, 9):
  {(21,): [[0,1,2,3,4,7,8,11,14,16],[0,6,7,9,11,12,15,16,17,19]]},
( 22, 8, 8):
  {(22,): [[0,1,5,7,13,17,20,21],[0,2,7,11,13,14,16,17],[0,3,4,12,14,15,17,21]]},
( 22, 8,12):
  {(22,): [[1,2,3,5,6,9,15,18], [1,2,3,5,8,9,10,15],
           [1,3,4,9,13,18,19,21], [2,4,6,12,13,15,17,1],
           [2,4,8,12,13,15,19,1], [2,4,8,16,13,15,19,5]]},
( 25, 7, 7):
  {(5,5): [[(0,0),(0,1),(0,4),(1,1),(1,2),(4,3),(4,4)],
           [(0,0),(1,0),(1,3),(2,3),(3,2),(4,0),(4,2)],
           [(0,0),(0,2),(0,3),(2,2),(2,4),(3,1),(3,3)],
           [(0,0),(1,4),(2,0),(2,1),(3,0),(3,4),(4,1)]]},
( 29, 8,6):
  {(29,): [[0,5,10,11,12,13,16,20],[0,8,10,12,17,22,23,26],
           [0,4,5,11,13,23,25,26]]},
( 34,12, 8):
  {(34,): [[0,5,9,14,15,17,20,25,26,27,28,30],
           [0,6,7,10,13,17,18,20,22,24,25,26]]},
( 34,12,10):
  {(34,): [[0,2,3,4,8,9,11,13,14,24,27,30],
           [0,2,6,7,8,11,13,14,22,25,26,32],
           [0,2,10,18,22,32,17,19,27,1,5,15]]},
( 43,15,10):
  {(43,): [[1,3,6,13,18,21,22,25,26,27,33,35,36,38,40],
           [9,10,11,13,16,17,19,23,26,27,28,33,35,38,39]]},
( 46,10, 6):
  {(46,): [[0,2,11,13,21,22,30,33,34,40],[0,2,6,7,22,23,28,32,35,38],
           [0,2,4,7,8,9,12,23,26,41]]},
( 49,21,10):
  {(7,7): [[(0,1),(0,2),(0,4),(1,1),(1,2),(1,4),(2,1),(2,2),(2,4),(3,1),(3,2),
            (3,4),(4,1),(4,2),(4,4),(5,1),(5,2),(5,4),(6,1),(6,2),(6,4)],
           [(1,0),(1,1),(1,2),(1,4),(2,0),(2,1),(2,2),(2,4),(4,0),(4,1),(4,2),
            (4,4),(3,3),(3,5),(3,6),(5,3),(5,5),(5,6),(6,3),(6,5),(6,6)]]},
( 53,13, 6):
  {(53,): [[1,10,13,15,16,24,28,36,42,44,46,47,49],
           [2,3,19,20,26,30,31,32,35,39,41,45,48]]},
( 53,14, 7):
  {(53,): [[0,1,10,13,15,16,24,28,36,42,44,46,47,49],
           [0,2,3,19,20,26,30,31,32,35,39,41,45,48]]},
( 61,15, 7):
  {(61,): [[0,1,3,4,8,10,13,22,30,35,44,45,46,50,58],
           [0,1,3,5,13,18,29,34,35,37,41,43,44,51,55]]},
( 67,12, 6):
  {(67,): [[0,1,9,14,15,22,24,25,40,59,62,64],
           [0,2,13,18,28,30,44,48,50,51,57,61],
           [0,4,21,26,29,33,35,36,47,55,56,60]]},
}

# Create the list of DF for the documentation
_all_l = sorted(set(l for v,k,l in DF.keys()))
LIST_OF_DF = join(("    - `\lambda={}`:\n       ".format(l)+
                  join(("`({},{},{})`".format(v,k,l) for v,k,_ in sorted(DF.keys()) if _ == l),", ")
                  for l in _all_l), "\n")

def DM_12_6_1():
    r"""
    Return a `(12,6,1)`-difference matrix as built in [Hanani75]_.

    This design is Lemma 3.21 from [Hanani75]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_12_6_1
        sage: G,M = DM_12_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(12,6)

    REFERENCES:

    .. [Hanani75] Haim Hanani,
      Balanced incomplete block designs and related designs,
      http://dx.doi.org/10.1016/0012-365X(75)90040-0,
      Discrete Mathematics, Volume 11, Issue 3, 1975, Pages 255-369.
    """
    from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(2).cartesian_product(AdditiveCyclic(6))
    M = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,1),(1,0),(0,3),(1,2),(0,4)],
         [(0,0),(0,2),(1,2),(1,0),(0,1),(1,5)],
         [(0,0),(0,3),(0,2),(0,1),(1,5),(1,4)],
         [(0,0),(0,4),(1,1),(1,3),(0,5),(0,2)],
         [(0,0),(0,5),(0,1),(1,5),(1,3),(1,1)],
         [(0,0),(1,0),(1,3),(0,2),(0,3),(1,2)],
         [(0,0),(1,1),(1,5),(1,2),(1,4),(1,0)],
         [(0,0),(1,2),(0,4),(0,5),(0,2),(1,3)],
         [(0,0),(1,3),(1,4),(0,4),(1,1),(0,1)],
         [(0,0),(1,4),(0,5),(1,1),(1,0),(0,3)],
         [(0,0),(1,5),(0,3),(1,4),(0,4),(0,5)]]

    return G,M

def DM_21_6_1():
    r"""
    Return a `(21,6,1)`-difference matrix.

    As explained in the Handbook III.3.50 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_21_6_1
        sage: G,M = DM_21_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(21,6)
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    M = [[  8,  17,  20,   2],
         [  9,  16,   4,  15],
         [ 11,   5,  10,   6],
         [ 14,   1,   3,  13],
         [ 18,  19,  12,   7]]

    Mb = [[0,0,0,0,0,0]]
    for a,b,c,d,e in zip(*M):
        Mb.append([a,b,c,d,e,0])
        Mb.append([b,c,d,e,a,0])
        Mb.append([c,d,e,a,b,0])
        Mb.append([d,e,a,b,c,0])
        Mb.append([e,a,b,c,d,0])

    return AdditiveCyclic(21), Mb

def DM_24_8_1():
    r"""
    Return a `(24,8,1)`-difference matrix.

    As explained in the Handbook III.3.52 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_24_8_1
        sage: G,M = DM_24_8_1()
        sage: is_difference_matrix(M,G,8,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(24,8)
    """
    M = ("0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 "+
         "0000 0010 0100 0110 1000 1010 1100 1110 2000 2010 2100 2110 "+
         "0000 0011 1001 2110 0111 2011 2111 1000 0100 1100 1101 2010 "+
         "0000 1010 1011 2000 1101 2110 0001 0101 2100 2001 0111 1100 "+
         "0000 0001 2010 1111 2111 2100 1101 0011 1010 2101 1000 0110 "+
         "0000 1000 2001 1011 0100 1100 0110 2101 2111 0010 1111 2011 "+
         "0000 1001 0111 2100 2000 0010 1110 2011 1100 1011 0101 2111 "+
         "0000 1011 2101 0100 2110 1001 2000 0110 0101 1111 2011 1010 ")

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    from sage.categories.cartesian_product import cartesian_product
    G = cartesian_product(map(AdditiveCyclic,[2,2,6]))
    rlabel = {(x%2,x%3):x for x in range(6)}
    M = [G([int(c),int(d),rlabel[int(b),int(a)]]) for a,b,c,d in M.split()]
    M = [M[i*12:(i+1)*12] for i in range(8)]
    Mb = []
    for a,b,c,d,e,f,g,h in zip(*M):
        Mb.append([a,b,c,d,e,f,g,h])
        Mb.append([a + G([0,0,rlabel[0,0]]),
                   b + G([0,1,rlabel[0,0]]),
                   c + G([1,0,rlabel[0,0]]),
                   d + G([1,1,rlabel[0,0]]),
                   e + G([0,0,rlabel[1,0]]),
                   f + G([0,1,rlabel[1,0]]),
                   g + G([1,0,rlabel[1,0]]),
                   h + G([1,1,rlabel[1,0]])])

    return G, Mb

def DM_28_6_1():
    r"""
    Return a `(28,6,1)`-difference matrix.

    As explained in the Handbook III.3.54 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_28_6_1
        sage: G,M = DM_28_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(28,6)
    """
    z=2
    M = [
        [(0,0), (z+1,6),(1,1)  ,(1,1)  ,(1,3)  ,(1,4)  ,(0,0)  ,(1,4), (z,5)  ],
        [(z,2), (0,0)  ,(1,5)  ,(z,1)  ,(z,2)  ,(z,6)  ,(z+1,3),(0,0), (z,1)  ],
        [(z,3), (z+1,4),(0,0)  ,(z+1,5),(z+1,2),(z+1,4),(z+1,2),(1,6), (0,0)  ],
        [(0,5), (z,6)  ,(0,5)  ,(0,6)  ,(z,3)  ,(0,0)  ,(0,4)  ,(1,5), (z+1,4)],
        [(0,3), (0,3)  ,(z+1,5),(0,0)  ,(0,5)  ,(z+1,6),(1,1)  ,(0,1), (z,3)  ],
        [(1,3), (0,6)  ,(0,6)  ,(1,5)  ,(0,0)  ,(0,3)  ,(z+1,6),(z,2), (0,2)  ],
        ]

    from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
    from sage.modules.free_module_element import free_module_element as vector
    G = AdditiveAbelianGroup([2,2,7])
    M = [[G(vector([x//2,x%2,y])) for x,y in L] for L in M]

    Mb=[[0,0,0,0,0,0]]

    for R in zip(*M):
        a,b,c,d,e,f = R
        Mb.append([a,b,c,d,e,f])
        Mb.append([b,c,a,f,d,e])
        Mb.append([c,a,b,e,f,d])

    return G, Mb

def DM_33_6_1():
    r"""
    Return a `(33,6,1)`-difference matrix.

    As explained in the Handbook III.3.56 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_33_6_1
        sage: G,M = DM_33_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(33,6)
    """
    M = [
        [   0,   0,   0,   0,   0,   0],
        [  15,  11,  22,   4,  17,   8],
        [  19,   7,  14,  32,  22,  18],
        [  22,  19,   8,  24,  21,   6],
        [   9,  12,  15,   7,  26,  14],
        [  14,  28,  23,   2,  19,   3]
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(33)

    Mb = [[0, 0, 0, 0, 0, 0],
          [1, 4,16,31,25,22],
          [7,28,13,19,10, 0]]

    for R in zip(*M):
        a,b,c,d,e,f = R
        for i in range(5):
            Mb.append([a,b,c,d,e,f])
            a,b,c,d,e,f = 4*e,4*a,4*b,4*c,4*d,4*f

    return G, Mb

def DM_35_6_1():
    r"""
    Return a `(35,6,1)`-difference matrix.

    As explained in the Handbook III.3.58 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_35_6_1
        sage: G,M = DM_35_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(35,6)
    """
    M = [
        [  0, 15, 30, 10, 25,  1, 16, 31, 11, 26,  2, 17, 32, 12,  6,  3, 18, 33, 27, 21,  4, 19, 13,  7, 22,  5, 34, 28,  8, 23, 20, 14, 29,  9, 24],
        [  0, 22, 16,  3,  4,  9, 10, 32, 26, 13, 18,  5, 27, 14, 15, 20,  7,  1, 23, 31, 29,  2, 24, 11, 19, 17, 25, 12,  6, 28, 33, 34, 21,  8, 30],
        [  0, 29,  2, 31, 18, 10, 32, 26, 34, 28, 27, 21, 15,  9, 17, 30,  3,  4,  5, 20, 12,  6, 14, 22, 16,  8, 23, 24, 25, 33, 11, 19, 13,  7,  1],
        [  0,  8,  9, 17, 11, 25, 19, 27, 28,  1, 15, 23, 31,  4, 26, 12,  6, 14, 29, 16,  2,  3, 18, 33, 34, 20,  7, 22, 30, 24, 10, 32,  5, 13, 21],
        [  0,  1, 23, 24, 32, 33,  6,  7, 29, 30, 10, 11, 12, 13, 28,  8,  9, 31,  4,  5, 27, 14, 15, 16,  3, 25, 26, 34, 21, 22,  2, 17, 18, 19, 20],
        [0]*35
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(35)

    return G, zip(*M)

def DM_36_9_1():
    r"""
    Return a `(36,9,1)`-difference matrix.

    As explained in the Handbook III.3.59 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_36_9_1
        sage: G,M = DM_36_9_1()
        sage: is_difference_matrix(M,G,9,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(36,9)
    """
    M = [
        [(0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0)],
        [(0,0,0,0), (0,1,0,0), (1,0,0,0), (1,1,0,0), (0,0,0,1), (0,1,0,1), (1,0,0,1), (1,1,0,1), (0,0,0,2), (0,1,0,2), (1,0,0,2), (1,1,0,2)],
        [(0,0,0,0), (1,1,1,2), (0,0,2,1), (0,0,1,2), (0,1,2,0), (0,1,0,2), (1,1,1,1), (0,1,1,1), (1,1,1,0), (1,0,2,2), (1,0,0,1), (1,0,1,0)],
        [(0,0,0,0), (0,0,1,0), (1,0,1,0), (0,1,0,0), (1,1,0,0), (1,0,2,0), (1,0,0,0), (0,1,2,0), (1,1,2,0), (0,0,2,0), (1,1,1,0), (0,1,1,0)],
        [(0,0,0,0), (0,1,2,0), (0,0,1,0), (1,1,1,0), (1,0,2,0), (1,0,1,0), (0,1,0,0), (0,0,2,0), (0,1,1,0), (1,1,0,0), (1,1,2,0), (1,0,0,0)],
        [(0,0,0,0), (0,1,1,0), (0,1,2,0), (1,1,2,0), (1,1,0,2), (0,0,1,2), (1,1,2,2), (1,0,0,2), (1,0,0,1), (1,0,1,1), (0,0,2,1), (0,1,1,1)],
        [(0,0,0,0), (1,0,1,0), (1,1,0,1), (1,0,1,2), (1,0,2,2), (0,0,2,1), (0,1,0,1), (0,1,0,0), (1,1,2,2), (0,1,1,0), (0,0,1,2), (1,1,2,1)],
        [(0,0,0,0), (1,1,0,0), (0,1,1,0), (1,0,2,1), (0,1,0,2), (1,0,2,2), (0,0,2,2), (1,1,1,0), (1,0,1,1), (0,1,2,1), (1,1,1,1), (0,0,0,2)],
        [(0,0,0,0), (1,0,0,0), (1,1,1,0), (0,1,1,2), (1,1,2,1), (0,1,1,1), (0,0,1,1), (1,0,2,0), (0,1,2,2), (1,1,0,2), (1,0,2,2), (0,0,0,1)]
        ]

    from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
    from sage.modules.free_module_element import free_module_element as vector
    G = AdditiveAbelianGroup([2,2,3,3])
    M = [[G(vector(x)) for x in L] for L in M]

    Mb=[]

    for R in zip(*M):
        a,b,c,d,e,f,g,h,i = R
        for y in range(3):
            Mb.append([
                a+G(vector([0,0,0,0])),
                b+G(vector([0,0,y,0])),
                c+G(vector([0,0,2*y,0])),
                d+G(vector([0,0,0,y])),
                e+G(vector([0,0,0,2*y])),
                f+G(vector([0,0,y,y])),
                g+G(vector([0,0,2*y,2*y])),
                h+G(vector([0,0,y,2*y])),
                i+G(vector([0,0,2*y,y]))])

    return G, Mb

def DM_39_6_1():
    r"""
    Return a `(39,6,1)`-difference matrix.

    As explained in the Handbook III.3.61 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_39_6_1
        sage: G,M = DM_39_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    The design is available from the general constructor::

        sage: designs.difference_matrix(39,6,existence=True)
        True
    """
    M = [
        [   0,   0,   0,   0,   0,   0],
        [   4,  23,  13,   5,  12,  11],
        [  25,  11,  22,  34,  23,   6],
        [  13,   4,  20,  17,  15,  29],
        [  27,  21,   8,  16,  19,  26],
        [  16,  19,  34,  38,  26,  21]
        ]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(39)

    Mb=[[ 0,  0,  0,  0,  0,  0],
        [ 1, 16, 22, 17, 38, 23],
        [-1,-16,-22,-17,-38,-23]]

    for R in zip(*M):
        a,b,c,d,e,f = map(G,R)
        for i in range(3):
            Mb.append([ a, b, c, d, e, f])
            Mb.append([-a,-b,-c,-d,-e,-f])
            a,b,c,d,e,f = [16*x for x in [c,a,b,f,d,e]]

    return G,Mb

def DM_44_6_1():
    r"""
    Return a `(44,6,1)`-difference matrix.

    As explained in the Handbook III.3.64 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_44_6_1
        sage: G,M = DM_44_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(44,6)
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    from sage.categories.cartesian_product import cartesian_product

    G2 = AdditiveCyclic(2)
    G11 = AdditiveCyclic(11)
    G2211 = cartesian_product((G2,G2,G11))

    M = [
        [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)],
        [(1,1,4), (0,1,4), (1,1,7), (1,0,6), (1,1,9), (0,1,2), (0,1,5), (0,1,1)],
        [(1,0,6), (0,1,3), (1,0,0), (0,1,9), (1,1,1), (0,1,4), (1,1,9), (1,0,9)],
        [(1,1,6), (1,1,9), (0,1,2), (1,1,0), (0,1,0), (1,1,5), (0,0,4), (0,0,9)],
        [(1,0,9), (0,0,2), (0,0,1), (1,0,2), (0,0,7), (1,1,6), (1,1,0), (1,0,7)],
        [(1,0,1), (1,0,6), (1,1,3), (0,1,5), (0,0,5), (0,1,3), (0,1,0), (1,1,0)]
        ]

    M = [[G2211(x) for x in L] for L in M]

    Mb=[]

    for R in zip(*M):
        for c in range(5):
            (x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4),(x5,y5,z5),(x6,y6,z6) = R
            Mb.append(list(R))
            R = [(x5,y5,5*z5),
                 (x1,y1,5*z1),
                 (x2,y2,5*z2),
                 (x3,y3,5*z3),
                 (x4,y4,5*z4),
                 (x6,y6,5*z6)]

    for x,y,z in [(0,0,0), (1,0,1),(1,1,2),(0,0,8)]:
        Mb.append([(x,y,z),
                   (x,y,5*z),
                   (x,y,3*z),
                   (x,y,4*z),
                   (x,y,9*z),
                   (0,0,0)])

    return G2211, Mb

def DM_45_7_1():
    r"""
    Return a `(45,7,1)`-difference matrix.

    As explained in the Handbook III.3.65 [DesignHandbook]_.

    ... whose description contained a very deadly typo, kindly fixed by Julian
    R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_45_7_1
        sage: G,M = DM_45_7_1()
        sage: is_difference_matrix(M,G,7,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(45,7)
    """
    from sage.rings.finite_rings.constructor import FiniteField
    from sage.categories.cartesian_product import cartesian_product

    G533 = cartesian_product((FiniteField(5),FiniteField(3),FiniteField(3)))

    M = [
        [(0,0,0), (2,2,1), (3,1,1), (4,1,2), (4,0,1), (0,1,1), (0,2,1), (3,2,2)],
        [(0,0,0), (1,2,1), (4,2,2), (1,2,0), (4,1,0), (3,1,1), (3,0,0), (2,1,2)],
        [(0,0,0), (4,1,1), (2,2,1), (3,2,0), (1,2,0), (2,1,0), (1,0,0), (3,2,1)],
        [(0,0,0), (0,1,0), (2,1,1), (4,0,0), (0,0,2), (4,2,2), (3,2,2), (1,2,2)],
        [(0,0,0), (3,1,2), (2,1,0), (0,2,2), (4,2,1), (0,2,1), (2,0,1), (1,1,2)],
        [(0,0,0), (2,1,1), (1,2,2), (3,0,1), (2,0,1), (1,0,0), (4,2,1), (1,1,0)],
        [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]
        ]

    for i in range(6):
        M[i].extend(M[5-i][1:8])

    M[6].extend(M[6][1:8])

    Mb=[]

    for R in zip(*M):
        (x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4),(x5,y5,z5),(x6,y6,z6),(x7,y7,z7) = R
        for i in range(3):
            Mb.append([(x1, y1    , z1+i  ),
                       (x2, y2+2*i, z2    ),
                       (x3, y3+i  , z3+2*i),
                       (x4, y4+2*i, z4+i  ),
                       (x5, y5+i  , z5    ),
                       (x6, y6    , z6+2*i),
                       (x7, y7    , z7    )])

    return G533, Mb

def DM_48_9_1():
    r"""
    Return a `(48,9,1)`-difference matrix.

    As explained in the Handbook III.3.67 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_48_9_1
        sage: G,M = DM_48_9_1()
        sage: is_difference_matrix(M,G,9,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(48,9)
    """
    from sage.rings.finite_rings.constructor import FiniteField
    F16 = FiniteField(16,'x')
    F3 = FiniteField(3)
    F3F16 = F3.cartesian_product(F16)
    w = F16.primitive_element()
    assert w**4 == w+1

    A = [
        [ (0, 4), (2, 2),  (2,2), (0,13),  (0,4), (2,13),  (0,1),  (0,7), (1,7) , (2,2) ,  (0,6),  (2,9)],
        [ (2, 7), (0, 9),  (2,7), (2,3) ,  (0,3), (0,9) , (1,12),  (0,6), (0,12), (2,14),  (2,7), (0,11)],
        [ (2,12), (2,12), (0,14), (0,14),  (2,8), (0,8) ,  (0,2),  (1,2), (0,11), (0,1) ,  (2,4), (2,12)],
        [ (1, 3), (0, 2), (0,10), (0,14),  (0,9), (1,3) , (0,12), (2,13), (2,1) , (2,9) ,  (2,0),  (1,7)],
        [ (0, 0), (1, 8),  (0,7), (1,8) ,  (0,4), (0,14),  (2,6),  (0,2), (2,3) , (1,12), (2,14),  (2,5)],
        [ (0,12), (0, 5), (1,13), (0,4) , (1,13), (0,9) ,  (2,8), (2,11), (0,7) , (2,10),  (1,2),  (2,4)],
        [ (1,12), (2, 0), (1,14), (0,6) ,  (1,9), (0,14),  (1,4),  (0,5), (1,8) , (1,3) ,  (2,1),  (1,1)],
        [ (1, 4), (1, 2),  (2,5), (0,4) , (0,11), (1,14), (1,13),  (1,9), (0,10), (1,6) ,  (1,8),  (2,6)],
        [ (2,10), (1, 9),  (1,7), (1,4) ,  (0,9), (0,1) ,  (0,0),  (1,3), (1,14), (2,11), (1,11), (1,13)],
        ]

    A = [[F3F16((F3(a),w**b)) for a,b in L] for L in A]
    V = [12,2,7,0,5,10,3,8,13]

    Mb = []
    for L in zip(*A):
        Mb.append(L)

        for u in [0,1,4]:
            Mb.append([e+F3F16((0,w**(x+u))) for (e,x) in zip(L,V)])

    return F3F16, Mb

def DM_51_6_1():
    r"""
    Return a `(51,6,1)`-difference matrix.

    As explained in the Handbook III.3.69 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_51_6_1
        sage: G,M = DM_51_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(51,6)
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(51)

    M = [
        [   5,  33,  29,  30,   1],
        [   8,   3,  47,  10,  13],
        [  14,  27,   6,  12,  28],
        [   9,  16,  44,  49,  11],
        [  34,  32,  36,  26,  20]
        ]

    Mb=[[0,0,0,0,0]]

    for R in zip(*M):
        for i in range(5):
            for RR in [list(R), [-x for x in R]]:
                Mb.append(RR)
            R = cyclic_shift(R,1)

    for R in Mb:
        R.append(0)

    return G,Mb

def DM_52_6_1():
    r"""
    Return a `(52,6,1)`-difference matrix.

    As explained in the Handbook III.3.70 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_52_6_1
        sage: G,M = DM_52_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(52,6)
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    from sage.rings.finite_rings.constructor import FiniteField
    F4  = FiniteField(4,'z')
    G13 = FiniteField(13)
    G = F4.cartesian_product(G13)
    z = F4('z')
    assert z**2 == z+1

    M = [
        [    (0,0),    (0,0),    (0,0),    (0,0),   (0,0)],
        [(z**2,10),    (0,7),   (1,10),   (z,10),(z**2,3)],
        [   (z,10), (z**2,2),   (1,11),    (z,2),(z**2,7)],
        [    (z,8),(z**2,12),   (0,10),(z**2,11),(z**2,6)],
        [    (1,2),    (0,2), (z**2,8),    (z,3),   (z,7)],
        [    (1,6),   (z,12),    (0,7), (z**2,6),   (z,2)]
        ]

    M2 = [
        [    (1,1),(z**2,11)],
        [    (z,3),    (1,7)],
        [ (z**2,9),    (z,8)],
        [    (1,4), (z**2,3)],
        [   (z,12),    (1,9)],
        [(z**2,10),    (z,1)]
        ]

    M = [[G(x) for x in L] for L in M]
    M2= [[G(x) for x in L] for L in M2]

    Mb=[[(0,0)]*6]

    from itertools import product
    p = lambda x,y : G(tuple([x*yy for yy in G(y)]))

    def t1(i,R):
        if i > 1:
            return t1(1,t1(i-1,R))
        ((x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6)) = R
        return [(z*x3, 3*y3), (z*x1, 3*y1), (z*x2, 3*y2), (z*x6, 3*y6), (z*x4, 3*y4), (z*x5, 3*y5)]

    def t2(i,R):
        if i > 1:
            return t2(1,t2(i-1,R))
        ((x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6)) = R
        return [(  x3,   y3), (  x1,   y1), (  x2,   y2), (  x5,   y5), (  x6,   y6), (  x4,   y4)]

    for R in zip(*M):
        for c1,c2 in product([1,2,3],repeat=2):
            Mb.append(t2(c2,t1(c1,R)))

    for R in zip(*M2):
        for c2 in [1,2,3]:
            Mb.append(t2(c2,R))

    return G, Mb

def DM_55_7_1():
    r"""
    Return a `(55,7,1)`-difference matrix.

    As explained in the Handbook III.3.72 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_55_7_1
        sage: G,M = DM_55_7_1()
        sage: is_difference_matrix(M,G,7,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(55,7)
    """
    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(55)

    M = [
        [ 1  ,  7 , 14 , 19 , 28 , 33 , 40 , 46 , 50],
        [ 2  , 13 , 25 , 38 , 52 , 12 , 20 , 32 , 45],
        [ 39 , 6  ,  8 , 26 , 24 , 51 , 11 , 34 , 37],
        [ 54 , 48 , 41 , 36 , 27 , 22 , 15 , 9  ,  5],
        [ 53 , 42 , 30 , 17 , 3  , 43 , 35 , 23 , 10],
        [ 16 , 49 , 47 , 29 , 31 , 4  , 44 , 21 , 18]
        ]

    Mb=[[0,0,0,0,0,0,0]]

    for R in zip(*M):
        R = list(R)
        for c in range(6):
            Mb.append(cyclic_shift(R,c)+[0])

    return G, Mb

def DM_56_8_1():
    r"""
    Return a `(56,8,1)`-difference matrix.

    As explained in the Handbook III.3.73 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_56_8_1
        sage: G,M = DM_56_8_1()
        sage: is_difference_matrix(M,G,8,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(56,8)
    """
    from sage.rings.finite_rings.constructor import FiniteField
    F8  = FiniteField(8,'z')
    F7  = FiniteField(7)
    G   = F8.cartesian_product(F7)

    w = F8.primitive_element()
    assert w**3 == w+1

    M = [
        [(0,0), (w**0,0), (w**1,0), (w**2,0), (w**3,0), (w**4,0), (w**5,0), (w**6,0)],
        [(0,1), (w**1,6), (w**2,1), (w**3,1), (w**4,6), (w**5,1), (w**6,6), (w**0,6)],
        [(0,4), (w**2,3), (w**3,4), (w**4,4), (w**5,3), (w**6,4), (w**0,3), (w**1,3)],
        [(0,2), (w**3,5), (w**4,2), (w**5,2), (w**6,5), (w**0,2), (w**1,5), (w**2,5)],
        [(0,2), (w**4,5), (w**5,2), (w**6,2), (w**0,5), (w**1,2), (w**2,5), (w**3,5)],
        [(0,4), (w**5,3), (w**6,4), (w**0,4), (w**1,3), (w**2,4), (w**3,3), (w**4,3)],
        [(0,1), (w**6,6), (w**0,1), (w**1,1), (w**2,6), (w**3,1), (w**4,6), (w**5,6)],
        [(1,0), (   1,0), (   1,0), (   1,0), (   1,0), (   1,0), (   1,0), (   1,0)]
        ]

    Mb=[]

    for R in zip(*M):
        for _ in range(7):
            Mb.append(R)
            (x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8) = R
            R = [(w*x7,y7), (w*x1,y1), (w*x2,y2), (w*x3,y3), (w*x4,y4), (w*x5,y5), (w*x6,y6), (w*x8,y8)]

    return G, Mb

def DM_57_8_1():
    r"""
    Return a `(57,8,1)`-difference matrix.

    Given by Julian R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_57_8_1
        sage: G,M = DM_57_8_1()
        sage: is_difference_matrix(M,G,8,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(57,8)
    """
    M = orthogonal_array(8,8)
    M = [R for R in M if any(x!=R[0] for x in R)] # removing the 0..0, 1..1, 7..7 rows.
    B = (1,6,7,9,19,38,42,49) # base block of a (57,8,1) BIBD
    M = [[B[x] for x in R] for R in M]
    M.append([0]*8)

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(57)
    return G, M

def DM_60_6_1():
    r"""
    Return a `(60,6,1)`-difference matrix.

    As explained in [JulianAbel13]_.

    REFERENCES:

    .. [JulianAbel13] Existence of Five MOLS of Orders 18 and 60
      R. Julian R. Abel
      Journal of Combinatorial Designs
      2013

    http://onlinelibrary.wiley.com/doi/10.1002/jcd.21384/abstract


    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_60_6_1
        sage: G,M = DM_60_6_1()
        sage: is_difference_matrix(M,G,6,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(60,6)
    """
    M60 = [[(0,  0), (0, 0), (0,  0), (0,  0), (0,  0), (0,  0), (0,  0), (0,  0), (0,  0), (0,  0)],
           [(1, 10), (1, 6), (0, 17), (0,  7), (1,  5), (0,  9), (0,  3), (1, 13), (1, 17), (0, 13)],
           [(1, 22), (1, 1), (1,  8), (0,  9), (1, 21), (1, 29), (1,  0), (0,  2), (0, 12), (1, 15)],
           [(1, 24), (1, 1), (0, 14), (0,  0), (0, 16), (0, 18), (0,  8), (0, 28), (0, 17), (0,  7)],
           [(0, 17), (0, 7), (0, 20), (0,  1), (1,  4), (0, 26), (0, 19), (0, 28), (1, 21), (0,  6)],
           [(1, 14), (1, 9), (0, 10), (0, 27), (1, 20), (0, 11), (0, 13), (1, 12), (0, 28), (1, 18)]]

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    from sage.categories.cartesian_product import cartesian_product
    G = cartesian_product((AdditiveCyclic(2),AdditiveCyclic(30)))
    M60b=[]
    onezero = G((1,0))

    for R in zip(*M60):
        a,b,c,d,e,f = map(G,R)
        M60b.append([a,b,c,d,e,f])
        M60b.append([c,a,b,e,f,d])
        M60b.append([b,c,a,f,d,e])
        M60b.append([-d,-e,-f,-a+onezero,-b+onezero,-c+onezero])
        M60b.append([-e,-f,-d,-c+onezero,-a+onezero,-b+onezero])
        M60b.append([-f,-d,-e,-b+onezero,-c+onezero,-a+onezero])

    return G, M60b

def DM_75_8_1():
    r"""
    Return a `(75,8,1)`-difference matrix.

    As explained in the Handbook III.3.75 [DesignHandbook]_.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_75_8_1
        sage: G,M = DM_75_8_1()
        sage: is_difference_matrix(M,G,8,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(75,8)
    """
    from sage.rings.finite_rings.constructor import FiniteField
    from sage.categories.cartesian_product import cartesian_product

    F3 = FiniteField(3)
    F5 = FiniteField(5)
    G  = cartesian_product((F3,F5,F5))

    M = [
        [(2,0,0), (0,0,0), (0,0,0), (1,0,0), (0,0,0), (1,0,0), (1,0,0), (0,0,0)],
        [(0,2,3), (1,4,4), (1,1,3), (1,0,4), (2,4,3), (0,0,3), (1,4,4), (0,0,0)],
        [(1,3,2), (2,1,1), (1,4,0), (0,3,0), (1,0,4), (2,4,1), (0,1,2), (0,0,0)],
        [(0,2,4), (1,3,1), (2,0,2), (0,0,1), (2,4,0), (1,2,2), (0,0,0), (0,0,0)],
        [(1,1,2), (2,2,3), (0,3,1), (1,4,2), (2,1,0), (1,4,3), (2,4,4), (0,0,0)],
        [(0,1,4), (0,4,4), (2,4,1), (1,3,0), (1,3,1), (2,0,0), (2,4,0), (0,0,0)],
        [(0,4,4), (2,0,1), (2,3,3), (2,3,2), (0,0,2), (2,1,2), (1,4,2), (0,0,0)],
        [(2,4,2), (2,4,1), (2,3,1), (1,2,2), (1,3,0), (0,0,2), (2,4,2), (0,0,0)]
        ]

    for i in range(8):
        M[i].extend(M[7-i][:7])

    Mb=[]

    for R in zip(*M):
        for x in range(5):
            V = [(0,0,x), (0,x,0), (0,x,2*x),(0,2*x,2*x), (0,3*x,3*x), (0,4*x,3*x), (0,4*x,0), (0,0,4*x)]
            Mb.append([G(e)+G(ee) for e,ee in zip(R,V)])

    return G, Mb

def DM_273_17_1():
    r"""
    Return a `(273,17,1)`-difference matrix.

    Given by Julian R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_273_17_1
        sage: G,M = DM_273_17_1()
        sage: is_difference_matrix(M,G,17,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(273,17)
    """
    M = orthogonal_array(17,17)
    M = [R for R in M if any(x!=R[0] for x in R)] # removing the 0..0, 1..1, ... rows.
    B = (1,2,4,8,16,32,64,91,117,128,137,182,195,205,234,239,256) # (273,17,1) difference set
    M = [[B[x] for x in R] for R in M]
    M.append([0]*17)

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(273)
    return G, M

def DM_993_32_1():
    r"""
    Return a `(993,32,1)`-difference matrix.

    Given by Julian R. Abel.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_difference_matrix
        sage: from sage.combinat.designs.database import DM_993_32_1
        sage: G,M = DM_993_32_1()
        sage: is_difference_matrix(M,G,32,1)
        True

    Can be obtained from the constructor::

        sage: _ = designs.difference_matrix(993,32)
    """
    M = orthogonal_array(32,32)
    M = [R for R in M if any(x!=R[0] for x in R)] # removing the 0..0, 1..1, ... rows.
    B = (0,74,81,126,254,282,308,331,344,375,387,409,525,563, # (993,32,1) difference set
         572,611,631,661,694,702,734,763,798,809,814,851,906,
         908,909,923,927,933)
    M = [[B[x] for x in R] for R in M]
    M.append([0]*32)

    from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
    G = AdditiveCyclic(993)
    return G, M

DM = {
    (12 ,1) : (6 ,DM_12_6_1),
    (21 ,1) : (6 ,DM_21_6_1),
    (24 ,1) : (8 ,DM_24_8_1),
    (28 ,1) : (6 ,DM_28_6_1),
    (33 ,1) : (6 ,DM_33_6_1),
    (35 ,1) : (6 ,DM_35_6_1),
    (36 ,1) : (9 ,DM_36_9_1),
    (39 ,1) : (6 ,DM_39_6_1),
    (44 ,1) : (6 ,DM_44_6_1),
    (45 ,1) : (7 ,DM_45_7_1),
    (48 ,1) : (9 ,DM_48_9_1),
    (51 ,1) : (6 ,DM_51_6_1),
    (52 ,1) : (6 ,DM_52_6_1),
    (55 ,1) : (7 ,DM_55_7_1),
    (56 ,1) : (8 ,DM_56_8_1),
    (57 ,1) : (8 ,DM_57_8_1),
    (60 ,1) : (6 ,DM_60_6_1),
    (75 ,1) : (8 ,DM_75_8_1),
    (273,1) : (17,DM_273_17_1),
    (993,1) : (32,DM_993_32_1),
    }

# Create the list of DM for the documentation
_all_l = sorted(set(l for v,l in DM.keys()))
LIST_OF_DM = join(("    - `\lambda={}`:\n       ".format(l)+
                   join(("`({},{},{})`".format(v,k,l) for (v,l),(k,_) in sorted(DM.items()) if _ == l),", ")
                   for l in _all_l), "\n")

def RBIBD_120_8_1():
    r"""
    Return a resolvable `BIBD(120,8,1)`

    This function output a list ``L`` of `17\times 15` blocks such that
    ``L[i*15:(i+1)*15]`` is a partition of `120`.

    Construction shared by Julian R. Abel:

        Seiden's method: Start with a cyclic `(273,17,1)-BIBD` and let `B` be an
        hyperoval, i.e. a set which intersects any block of the BIBD in either 0
        (153 blocks) or 2 points (120 blocks). Dualise this design and take
        these last 120 blocks as points in the design; blocks in the design will
        correspond to the `273-18=255` non-hyperoval points.

        The design is also resolvable.  In the original `PG(2,16)` take any
        point `T` in the hyperoval and consider a block `B1` containing `T`.
        The `15` points in `B1` that do not belong to the hyperoval correspond
        to `15` blocks forming a parallel class in the dualised design. The
        other `16` parallel classes come in a similar way, by using point `T`
        and the other `16` blocks containing `T`.

    .. SEEALSO::

        :func:`OA_9_120`

    EXAMPLES::

        sage: from sage.combinat.designs.database import RBIBD_120_8_1
        sage: from sage.combinat.designs.bibd import is_pairwise_balanced_design
        sage: RBIBD = RBIBD_120_8_1()
        sage: is_pairwise_balanced_design(RBIBD,120,[8])
        True

    It is indeed resolvable, and the parallel classes are given by 17 slices of
    consecutive 15 blocks::

        sage: for i in range(17):
        ....:     assert len(set(sum(RBIBD[i*15:(i+1)*15],[]))) == 120

    The BIBD is available from the constructor::

        sage: _ = designs.balanced_incomplete_block_design(120,8)
    """
    from incidence_structures import IncidenceStructure
    n=273

    # Base block of a cyclic BIBD(273,16,1)
    B = [1,2,4,8,16,32,64,91,117,128,137,182,195,205,234,239,256]
    BIBD = [[(x+c)%n for x in B] for c in range(n)]

    # A (precomputed) set that every block of the BIBD intersects on 0 or 2 points
    hyperoval = [128, 192, 194, 4, 262, 140, 175, 48, 81, 180, 245, 271, 119, 212, 249, 189, 62, 255]
    #for B in BIBD:
    #    len_trace = sum(x in hyperoval for x in B)
    #    assert len_trace == 0 or len_trace == 2

    # Equivalence classes
    p = hyperoval[0]
    equiv = []
    new_BIBD = []
    for B in BIBD:
        if any(x in hyperoval for x in B):
            if p in B:
                equiv.append([x for x in B if x not in hyperoval])
        else:
            new_BIBD.append([x for x in B])

    BIBD = new_BIBD

    r = {v:i for i,v in enumerate(x for x in range(n) if x not in hyperoval)}
    BIBD  = [[r[x] for x in B] for B in BIBD ]
    equiv = [[r[x] for x in B] for B in equiv]

    BIBD = IncidenceStructure(range(255),BIBD)
    M = BIBD.incidence_matrix()

    equiv = [[M.nonzero_positions_in_row(x) for x in S] for S in equiv]
    return [B for S in equiv for B in S]

# Index of the BIBD constructions
#
# Associates to triple (v,k,lambda) a function that return a
# (n,k,lambda)-BIBD family.
#
# This dictionary is used by designs.BalancedIncompleteBlockDesign

BIBD_constructions = {
    (120,8,1): RBIBD_120_8_1,
}


__doc__ = __doc__.format(
    LIST_OF_OA_CONSTRUCTIONS   = LIST_OF_OA_CONSTRUCTIONS,
    LIST_OF_MOLS_CONSTRUCTIONS = LIST_OF_MOLS_CONSTRUCTIONS,
    LIST_OF_VMT_VECTORS        = LIST_OF_VMT_VECTORS,
    LIST_OF_DF                 = LIST_OF_DF,
    LIST_OF_DM                 = LIST_OF_DM)
del LIST_OF_OA_CONSTRUCTIONS, LIST_OF_MOLS_CONSTRUCTIONS, LIST_OF_VMT_VECTORS, LIST_OF_DF, LIST_OF_DM
