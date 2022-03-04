from arithmetiquedansZnZ import *
import copy
from random import *
from math import sqrt, log
from sympy import isprime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Les méthodes magiques : https://blog.finxter.com/python-dunder-methods-cheat-sheet/
# Voir Au coeur du Bitcoin - Programmer la Blockchain ouverte - collection O'Reilly
# Voir https://www.johndcook.com/blog/2018/08/14/bitcoin-elliptic-curves/

class ElemtE07(object):
    "Ensemble des solutions de Y²=X^3+7 dans Fp Courbe secp256k1"

    def __init__(self, x, y=None, p=None):
        """
        Défini par deux ElmntZnZ mais seul le modulo de x est utilisé . Celui de y doit donc lui être égal.
        Avec l'élément neutre ayant self.y='Inf'
        ElemtE07(7,6,11) doit renvoyer une erreur
        >>> ElemtE07(ElmtZnZ(7,11),ElmtZnZ(8,11))
        ElemtE07(7,8,11)
        >>>
        >>> ElemtE07(1,"Inf",11)
        ElemtE07(1,"INF",11)
        """
        if isinstance(x, ElemtE07):
            self.x, self.y = x.x, x.y
        else:
            self.x = ElmtZnZ(x) if isinstance(x, ElmtZnZ) else ElmtZnZ(x, p)
            if type(y) in [type(None), str]:  # Elément neutre à l'infini
                self.y = "INF"
            else:
                self.y = ElmtZnZ(y) if isinstance(y, ElmtZnZ) else ElmtZnZ(y, self.x.n)
            assert isinstance(self.y, str) or (self.y ** 2 == self.x ** 3 + 7), f"{self=} ne vérifie pas l'équation"

    def lDesElements(p=47):
        """
        >>> ElemtE07.lDesElements(5)
        [ElemtE07(0,"INF",5), ElemtE07(2,0,5), ElemtE07(3,2,5), ElemtE07(3,3,5), ElemtE07(4,1,5), ElemtE07(4,4,5)]
        >>> len(ElemtE07.lDesElements(11))
        12
        >>> ElemtE07(6,5,11) in (ElemtE07.lDesElements(11))
        True
        """
        assert sontPremiersEntreEux(7, p) and p > 2 and estPremier(
            p), " Ne rentrons pas dans les complications et gardons (0,0) comme élément neutre"
        ...

    def __hash__(self):
        """On fera une fonction injective afin de l'utiliser également dans binCode"""
        pass

    def ElemtE07DepuisHash(h, p):
        """
        >>> h=ElemtE07(6,5,11).__hash__()
        >>> ElemtE07.ElemtE07DepuisHash(h,11)
        ElemtE07(6,5,11)
        """
        pass

    def eDesElements(p=47, verbose=False):
        """
        >>> ElemtE07.eDesElements(5)==set(ElemtE07.lDesElements(5))
        True
        >>> ElemtE07(8,3,17) in (ElemtE07.eDesElements(17))
        True
        """
        assert sontPremiersEntreEux(7, p) and p > 2 and estPremier(
            p), " Ne rentrons pas dans les complications et gardons (0,0) comme élément neutre"
        el = set([ElemtE07(0, "INF", p)])
        for x in range(0, p):
            y2 = ElmtZnZ(x ** 3 + 7, p)
            if y2.estUnCarre():
                e37 = ElemtE07(ElmtZnZ(x, p), y2.racineCarree())
                if verbose: print(f"Ajout {len(el)} de eDesElements {e37}")
                el.add(e37)
                el.add(-e37)
        return el

    def __str__(self):
        """
        >>> print(ElemtE07(ElmtZnZ(3,47),ElmtZnZ(9,47)))
        (3,9)[47]
        """
        if self == 0:
            return "O(à l'infini)"
        else:
            return f"({self.x.element},{self.y.element})[{self.x.n}]"

    def __repr__(self):
        """
        """
        if isinstance(self.y, ElmtZnZ):
            valy = self.y.element
        elif isinstance(self.y, str):
            valy = f'"{self.y}"'
        else:
            valy = self.y
        return f"ElemtE07({self.x.element},{valy},{self.x.n})"

    def __add__(self, other):
        """
        >>> ElemtE07(2,2,11)+ElemtE07(3,1,11)
        ElemtE07(7,3,11)
        >>> (ElemtE07(3,"INF",47)+ElemtE07(3,9,47))+ElemtE07(3,"INF",47)
        ElemtE07(3,9,47)
        """
        lambd = (other.y - self.y).element // (other.x - self.x).element
        print("lambda : ", lambd)
        print(self.x, other.x)
        x = lambd ** 2 - self.x - other.x
        print("x=", ElmtZnZ(x))
        print("y=", -lambd * (x - self.x) - self.y)
        return ElemtE07(ElmtZnZ(x), ElmtZnZ(-lambd * (x - self.x) - self.y))

    def double(self):
        """
        >>> ElemtE07(2,2,11).double()
        ElemtE07(5,0,11)
        """
        pass

    def lOrbite(self):
        """
        >>> ElemtE07(2,2,11).lOrbite()
        [ElemtE07(2,2,11), ElemtE07(5,0,11), ElemtE07(2,9,11), ElemtE07(0,"INF",11)]
        """
        pass

    def __mul__(self, other):
        """
        >>> ElemtE07(6,5,11)*3
        ElemtE07(5,0,11)
        >>> ElemtE07(15,13,17)*0
        ElemtE07(0,"INF",17)
        """
        pass

    def __rmul__(self, other):
        """
        >>> 2*ElmtZnZ(3,10)
        ElmtZnZ(6,10)
        >>> 2*(ElemtE07(3,"INF",47)+3*ElemtE07(3,9,47))+ElemtE07(3,"INF",47)
        ElemtE07(43,32,47)
        """
        pass

    def __eq__(self, other):
        """
        >>> 3*ElemtE07(6,5,11)==ElemtE07(5,0,11)
        True
        >>> ElemtE07(0,"Inf",47)==0
        True
        >>> ElemtE07(3,9,47)==ElemtE07(3,"Inf",47) or ElemtE07(3,"Inf",47)==ElemtE07(3,9,47)
        False
        """
        pass

    def __neg__(self):
        """
        >>> -ElemtE07(7,3,11)
        ElemtE07(7,8,11)
        """
        pass

    def __sub__(self, other):
        """
        >>> ElemtE07(3,10,11)-ElemtE07(7,3,11)
        ElemtE07(4,7,11)
        >>> ElemtE07(3,9,47)-ElemtE07(3,9,47)==0
        True
        """
        pass

    def ordreCourbe(p=17):
        """
        >>> ElemtE07.ordreCourbe(11)
        12
        """
        return len(ElemtE07.lDesElements(p))

    def ordrePoint(self):
        """
        >>> ElemtE07(3,10,11).ordrePoint()
        3
        >>> ElemtE07(7,3,11).ordrePoint()
        12
        """
        return len(self.lOrbite())

    def estGenerateur(self):
        """
        >>> ElemtE07(7,3,11).estGenerateur()
        True
        >>> ElemtE07(3,10,11).estGenerateur()
        False
        """
        return ElemtE07.ordreCourbe(self.x.n) == self.ordrePoint()

    def lDesElementsGenerateurs(p=47):
        """
        >>> ElemtE07.lDesElementsGenerateurs(11)
        [ElemtE07(4,4,11), ElemtE07(4,7,11), ElemtE07(7,3,11), ElemtE07(7,8,11)]
        """
        return [e for e in ElemtE07.lDesElements(p) if e.estGenerateur()]

    def lDesElementsDOrdrePremier(p=47):
        """
        >>> ElemtE07.lDesElementsDOrdrePremier(11)
        [ElemtE07(3,1,11), ElemtE07(3,10,11), ElemtE07(5,0,11)]
        """
        return [e for e in ElemtE07.lDesElements(p) if estPremier(e.ordrePoint())]

    def elemtE07APartirDeX(x: ElmtZnZ):
        """
        Renvoie un point avec x ou une valeur proche de x comme abscisse
        >>> ElemtE07.elemtE07APartirDeX(ElmtZnZ(2,11))
        ElemtE07(2,2,11)
        """
        xx, p = ElmtZnZ(x), x.n
        assert p % 2 == 1
        y2 = xx ** 3 + 7
        while not (y2.estUnCarre()):  # yy est une racine carré
            xx = xx + 1
            y2 = xx ** 3 + 7
        # print(xx,y2)
        return ElemtE07(xx, y2.racineCarree())

    def randElemtE07(p):
        """Renvoie un élément non nul au hasard"""
        return ElemtE07.elemtE07APartirDeX(ElmtZnZ(randint(0, p - 1), p))

    def randGenerateurE07(p=47):
        """Renvoie un élément non nul au hasard
        >>> ElemtE07.randGenerateurE07(47).estGenerateur()
        True
        """
        el = ElemtE07.eDesElements(p)
        lel = list(el)
        r = choice(lel)
        while r.ordrePoint() != len(lel):
            r = choice(lel)
        return r

    def affichePointMaxDOrdresPremier(self):
        p = 7
        while p < 1000:
            p = nbPremierSuivant(p)
            le = ElemtE07.lDesElementsDOrdrePremier(p)
            GMax, omax = None, -1
            for e in le:
                ord = e.ordrePoint()
                if ord > omax:
                    GMax, omax = ElemtE07(e), ord
            print(f"Avec F{p} l'ordre premier max est atteint avec {GMax} et vaut : {omax}")

    def afficheGraphique1(p):
        pass


if __name__ == "__main__":
    import doctest

    # doctest.testmod()
    # p = 11  # p=65537
    # x = ElmtZnZ(2, p)
    # M = ElemtE07.elemtE07APartirDeX(x)
    # print(M)
    # e = ElemtE07.randElemtE07(p)
    # print(f"{e=}")
    # el=ElemtE07.eDesElements(p)
    # print(el)
    # g = ElemtE07.randGenerateurE07(p)
    # print(f"{g=}")
    # afficheGraphique1(17)

    # demoVitesse()
    # ElmtZnZ.demo1()
    # ElmtZnZ(8,60).demoDiv()

    test1 = ElemtE07(ElmtZnZ(2, 11), ElmtZnZ(2, 11))
    test2 = ElemtE07(ElmtZnZ(3, 11), ElmtZnZ(1, 11))
    test1 + test2