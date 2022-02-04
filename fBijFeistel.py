from fBijOctetsCA import *
from Binaire603 import *
from operator import xor
import random
import matplotlib.pyplot as plt
class fBijFeistel(fBijOctetsCA):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""
    def __init__(self, cle, f, nbTours):
        self.cle = cle
        self.f = f
        self.nbTours = nbTours

    def __str__(self):
        return "Fonction Feistel"

    def __repr__(self):
        return f'fBijFeistel({self.cle},{self.f},{self.nbTours})'

    def __call__(self,octet):
        l,r = octet//16, octet%16
        random.seed(self.cle)
        for tour in range(self.nbTours):
            l, r = r, l ^ self.f(r,randint(0,15))
        return l+r

    def affiche(self):
        lx = [k for k in range(256)]
        ly = [self(k) for k in lx]
        plt.plot(lx, ly, "*")  # où "." pour un graphique point par point plt.title("La fonction carré")
        plt.title(self)
        plt.show()


def F4B1(v4b,k):
    return (v4b*v4b+k)%16

fBij = fBijFeistel(15783,F4B1,4)
fBij.affiche()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    monBin = Binaire603([0x00, 0x01, 0x02, 0x010, 0x20, 0x40, 0x80])
