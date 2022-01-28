import random
from arithmetiquedansZnZ import *
from utils import *


class Permutation603:
    def __init__(self, lp, indices=None):
        self.lp = lp
        if not indices:
            self.indices = [i for i in range(len(lp))]
        else:
            self.indices = indices

    def __str__(self):
        return f"{self.lp}"

    def __repr__(self):
        return f"Permutation603({self.lp})"

    def __eq__(self, other):
        return self.lp == other.lp and self.indices == other.indices

    def __len__(self):
        return len(self.lp)

    def __pow__(self, power, modulo=None):
        """ Permutation à droite
        >>> Permutation603([2, 3, 1, 0])**4
        Permutation603([3, 2, 0, 1])
        """
        power = ElmtZnZ(element=power, n=len(self) + 1).element
        ma_perm = self
        for j in range(power - 1):
            res = []
            for i in range(len(ma_perm.lp)):
                res += [ma_perm.lp[ma_perm.indices.index(ma_perm.lp[i])]]
            ma_perm.indices = ma_perm.lp
            ma_perm.lp = res
        return ma_perm

    def ordre(self):
        """Renvoie l’ordre de la permutation
        >>> Permutation603([1,2,3,0]).ordre()
        4
        >>> Permutation603([1,0,2,3]).ordre()
        2
        """
        init = sorted(self.lp)
        i = 0
        while (self ** (i)).lp != init:
            i += 1
        return i

    def permuAlea(self):
        """Renvoie une permutation aléatoire avec randint"""
        return self ** (random.randint(1, len(self.lp) + 1))

    def permuKieme(k, n=6):
        raise NotImplementedError

    def numPermutation(self):
        raise NotImplementedError

    def demo(self):
        print("<---------- Début ---------->\n")
        perm = Permutation603([2, 3, 1, 0])
        print(f"Ordre de Permutation603([2, 3, 1, 0]) : ", perm.ordre())
        perm2 = self ** 2
        print(f"Permutation à l'ordre 2 de Permutation603({self.lp}) : ", perm2)
        permAlea = self.permuAlea()
        print(f"Permutation aléatoire de Permutation603({self.lp}) : ", permAlea)


if __name__ == "__main__":
    print(Permutation603(lp=[2, 3, 1, 0]) ** 3)
    print(Permutation603(lp=[2, 3, 1, 0]).ordre())
    # print(Permutation603(lp=[1, 0, 2, 3]).ordre())
    """
    import doctest

    # doctest.testmod()
    """
    # Permutation603([3, 0, 1, 2]).demo()