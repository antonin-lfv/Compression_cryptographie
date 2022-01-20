import random
from arithmetiquedansZnZ import *

class Permutation603:
    def __init__(self, liste):
        self.liste = liste

    def __str__(self):
        return f"{self.liste}"

    def __repr__(self):
        return f"Permutation603({self.liste})"

    def __pow__(self, power, modulo=None):
        """
        >>> Permutation603([1, 2, 3, 0])**2
        Permutation603([2, 3, 0, 1])
        >>> Permutation603([1, 2, 3, 0])**4
        Permutation603([0, 1, 2, 3])
        >>> Permutation603([1, 2, 3, 0])**(-1)
        Permutation603([3, 0, 1, 2])
        """
        return Permutation603(liste=list(map(lambda x: ElmtZnZ(element=x + (power - 1), n=len(self.liste)).element, self.liste)))

    def ordre(self):
        """Renvoie l’ordre de la permutation
        >>> Permutation603([1,2,3,0]).ordre()
        4
        >>> Permutation603([1,0,2,3]).ordre()
        2
        """
        return self.liste.index(0) + 1

    def permuAlea(self):
        """Renvoie une permutation aléatoire avec randint"""
        return self**(random.randint(1, len(self.liste)+1))

    def permuKieme(k, n=6):
        raise NotImplementedError

    def numPermutation(self):
        raise NotImplementedError

    def demo(self):
        print("<---------- Début ---------->\n")
        perm = self
        print("Ordre de Permutation603([1, 2, 3, 0]) : ", perm.ordre())
        perm2 = self ** 2
        print("Permutation à l'ordre 2 de Permutation603([1, 2, 3, 0]) : ", perm2)
        permAlea = self.permuAlea()
        print("Permutation aléatoire de Permutation603([1, 2, 3, 0]) : ", permAlea)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    Permutation603([1, 2, 3, 0]).demo()
