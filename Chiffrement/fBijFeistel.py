from fBijOctetsCA import *
from Binaire603 import *
from operator import xor
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import plot
from DES import *


class fBijFeistel(fBijOctetsCA):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

    def __init__(self, cle, f, nbTours):
        super().__init__()
        self.cle = cle
        self.f = f
        self.nbTours = nbTours

    def __str__(self):
        return "Fonction Feistel"

    def __repr__(self):
        return f'fBijFeistel({self.cle},{self.f},{self.nbTours})'

    def __call__(self, octet):
        l, r = octet // 16, octet % 16
        random.seed(self.cle)
        for tour in range(self.nbTours):
            l, r = r, l ^ self.f(r, randint(0, 15))
        return l + r

    def affiche(self):
        fig = go.Figure()
        lx = [k for k in range(256)]
        ly = [self(k) for k in lx]
        fig.add_scatter(x=lx, y=ly, mode='markers', marker_symbol='star')
        plot(fig)


def F4B1(v4b, k):
    """k la clé, v4b la partie du message"""
    return (v4b * v4b + k) % 16


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # monBin = Binaire603([0x00, 0x01, 0x02, 0x010, 0x20, 0x40, 0x80])
    fBij = fBijFeistel(15783, F4B1, 4)
    fBij.affiche()