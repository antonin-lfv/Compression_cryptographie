import numpy as np
from utils import *
import math

def table_addition(n):
    tab = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            tab[i, j] = (i + j) % n
    return tab
def table_multiplication(n):
    tab = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            tab[i, j] = (i * j) % n
    return tab
def decomposition_puissance_2(a):
    """
    renvoie les puissances de 2 à effectuer pour obtenir 'a' (ex : 2^2 + 2^3 = 12)
    >>> print(decomposition_puissance_2(12))
    [2, 3]
    """
    resultat = []
    while a != 0:
        puissance = int(math.log2(a))
        resultat.insert(0, puissance)
        a -= 2 ** puissance
        if a != 0:
            puissance = int(math.log2(a))
    return resultat
def exponentiation_rapide(a, p, m):
    """
    renvoie le resultat de (a^p) % m
    >>> print(exponentiation_rapide(12, 784, 47))
    3
    """
    tempo = []
    indice = 0
    decomposition = decomposition_puissance_2(p)
    for i in range(decomposition[-1] + 1):
        # "decomposition" contient l'indice de la puissance, je regarde donc quand j'arrive au bon moment
        # pour récupérer mon "a" (a = a**2 % m => a = a**2 % m ...)
        if decomposition[indice] == i:
            tempo.append(a)
            indice += 1
        a = a ** 2 % m
    resultat = tempo[0]
    for i in range(len(tempo) - 1):
        resultat = resultat * tempo[i + 1] % m
    return resultat

class ElmtZnZ:
    def __init__(self, element, n):
        self.n = n
        self.element = element % n
        self.table_multiplication = table_multiplication(self.n)
        self.table_addition = table_addition(self.n)

    def __str__(self):
        """Affichage d'un objet"""
        return f'{self.element} modulo {self.n}'

    def __repr__(self):
        """
        Donne la commande pour recréer un objet
        exemple :
        >>> ElmtZnZ(element=10, n=11).__repr__()
        'ElmtZnZ(10, 11)'
        """
        return f'ElmtZnZ({self.element}, {self.n})'

    def __eq__(self, other):
        """
        Retourne si deux éléments sont égaux dans Z/nZ
        >>> ElmtZnZ(element=18, n=9) == ElmtZnZ(element=9, n=9)
        True
        """
        return self.n == other.n and self.element == other.element % self.n
        # return f'{self.element}={other.element} dans ℤ/{self.n}ℤ' if (self.n == other.n and self.element == other.element) else f'{self.element}!={other.element} dans ℤ/{self.n}ℤ'

    def __add__(self, other):
        """
        Somme de deux éléments dans Z/nZ
        exemple : dans Z/9Z
        >>> ElmtZnZ(element=9, n=10) + ElmtZnZ(element=9, n=10)
        ElmtZnZ(8, 10)
        """
        if isinstance(other, ElmtZnZ):
            return ElmtZnZ(element=(self.element + other.element) % self.n, n=self.n)
            # return f'La somme de {other.element} et {self.element} est {(self.element + other.element) % self.n} dans ℤ/{self.n}ℤ '

    def __radd__(self, other):
        """
        Addition de deux élements différents
        >>> 1 + ElmtZnZ(element=10,n=11)
        ElmtZnZ(0, 11)
        """
        return ElmtZnZ(element=(self.element + other) % self.n, n=self.n)

    def __pow__(self, power, modulo=None):
        """
        Donne l'élément puissance power dans Z/nZ
        exemple dans Z/10Z
        >>> ElmtZnZ(element=9, n=10)**2
        ElmtZnZ(1, 10)
        """
        return ElmtZnZ(element=exponentiation_rapide(self.element, power, self.n), n=self.n)
        # return f'{self.element} à la puissance {power} est {(self.element ** power) % self.n} dans ℤ/{self.n}ℤ'

    def __mul__(self, other):
        """
        Produit de deux objets dans Z/nZ
        >>> ElmtZnZ(element=9, n=10) * ElmtZnZ(element=2, n=10)
        ElmtZnZ(8, 10)
        """
        if isinstance(other, ElmtZnZ):
            return ElmtZnZ(element=(other.element * self.element) % self.n, n=self.n)
        else:
            return ElmtZnZ(element=(self.element * other) % self.n, n=self.n)

    def __rmul__(self, other):
        """
        Retourne a*b dans Z/nZ
        >>> 10 * ElmtZnZ(element=2, n=5)
        ElmtZnZ(0, 5)
        """
        return ElmtZnZ(element=(self.element * other) % self.n, n=self.n)

    def __floordiv__(self, other):
        """
        Retourne a//b dans Z/nZ
        >>> ElmtZnZ(element=8, n=10) // ElmtZnZ(element=2, n=10)
        ElmtZnZ(4, 10)
        """
        if isinstance(other, ElmtZnZ):
            return ElmtZnZ(element=(self.element // other.element) % self.n, n=self.n)
        else:
            return ElmtZnZ(element=(self.element // other) % self.n, n=self.n)

    def __rfloordiv__(self, other):
        """
        Retourne a//b dans Z/nZ
        >>> ElmtZnZ(element=2, n=10) // 2
        ElmtZnZ(1, 10)
        """
        return ElmtZnZ(element=(self.element // other) % self.n, n=self.n)

    def __neg__(self):
        """
        Retourne l'opposé d'un nombre dans Z/nZ
        >>> -ElmtZnZ(element=2, n=10)
        ElmtZnZ(8, 10)
        """
        compt = -self.element
        while compt < 0:
            compt += self.n
        return ElmtZnZ(element=compt, n=self.n)

    def __sub__(self, other):
        """
        Soustraction de deux élements dans Z/nZ
        >>> ElmtZnZ(element=2, n=10) - ElmtZnZ(element=7, n=10)
        ElmtZnZ(5, 10)
        """
        if isinstance(other, ElmtZnZ):
            return ElmtZnZ(element=(self.element - other.element) % self.n, n=self.n)
        else:
            return ElmtZnZ(element=(self.element - other) % self.n, n=self.n)

    def __rsub__(self, other):
        """
        >>> 2 - ElmtZnZ(element=7, n=10)
        ElmtZnZ(5, 10)
        """
        return ElmtZnZ(element=(self.element - other) % self.n, n=self.n)

    def estInversible(self):
        """
        Retourne True si l'élément est inversible dans Z/nZ
        >>> ElmtZnZ(element=10, n=11).estInversible()
        True
        """
        if 1 in self.table_multiplication[self.element]:
            return True
        else:
            return False

    def inverse(self):
        """
        Retourne l'inverse de m dans Z/nZ
        >>> ElmtZnZ(element=10, n=11).inverse()
        ElmtZnZ(10, 11)
        """
        ligne = self.table_multiplication[self.element]
        resultat = np.where(ligne == 1)[0]
        return ElmtZnZ(element=resultat[0], n=self.n)
        # return f"L'inverse de {self.element} est {resultat[0]}" if resultat else f"{self.element} n'a pas d'inverse dans ℤ/{self.n}ℤ"

    def valThChinois(self, other):
        """
        Théorème chinois
        >>> ElmtZnZ(2,7).valThChinois(ElmtZnZ(3,10))
        ElmtZnZ(23, 70)
        """
        u, v, pgcd = bezout(self.n, other.n)
        c = other.element * u * self.n + self.element * v * other.n
        m = self.n * other.n
        while c < 0:
            c += m
        return ElmtZnZ(element=c, n=m)

    def logDiscret(self, b):
        """Renvoie x tel que self.a**x==b(self.n) n doit être premier
        pour garantir l'existence
        >>> ElmtZnZ(2,13).logDiscret(8)
        3
        >>> ElmtZnZ(2,13).logDiscret(3)
        4
        """
        if len(eDiviseurs(self.n)) != 2:
            return 'Le modulo n\'est pas un nombre premier'
        else:
            x = 1
            while (b % self.n) != exponentiation_rapide(self.element, x, self.n):
                x += 1
            return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    e1 = ElmtZnZ(element=10, n=7)
    e2 = ElmtZnZ(element=1, n=7)
    e3 = ElmtZnZ(element=2, n=13)

    print(f'e1 : {e1}')
    print(f'e2 : {e2}')
    print(f'e2 : {e3}')
    print(f'égalité entre e1 et e2 : {e1 == e2}')
    print(f'Somme de e1 et e2 : {e1 + e2}')
    print(f'Somme de 24 et e2 : {4 + e2}')
    print(f'e1 puissance 3 : {e1 ** 3}')
    print(f'Produit de e1 et e2 : {e1 * e2}')
    print(f'Produit de 4 et e1 : {4 * e1}')
    print(f'Division entière de e1 par e2 : {e1 // e2}')
    print(f'Division entière de 4 par e1 : {4 // e1}')
    print(f'Opposé de e1 : {-e1}')
    print(f'Soustraction de e2 et e1 : {e2 - e1}')
    print(f'Soustraction de 5 et e2 : {5 - e2}')
    print(f'e1 est inversible : {e1.estInversible()}')
    print(f'L\'inverse de e1 : {e1.inverse()}')
    print(f'logDiscret avec e3 et 8 : {e3.logDiscret(8)}')
