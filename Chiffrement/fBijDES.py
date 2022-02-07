from CodeurDES import *
from Binaire603 import *
from operator import xor
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import plot
from DES import *


class fBijDES(CodeurDES):

    def __init__(self, cle, f, nbTours):
        super().__init__()
        self.cle = cle
        self.f = f
        self.nbTours = nbTours

    def __str__(self):
        return "Fonction Feistel/DES"

    def __repr__(self):
        return f'fBijDES({self.cle},{self.f},{self.nbTours})'

    def __call__(self, octet):
        cle_hexa_to_bin(cle_hex='133457799BBCDFF1')
        raise NotImplementedError

    def affiche(self):
        fig = go.Figure()
        lx = [k for k in range(256)]
        ly = [self(k) for k in lx]
        fig.add_scatter(x=lx, y=ly, mode='markers', marker_symbol='star')
        plot(fig)


def fDES(R, K):
    R_developpe = fonction_developpement(R=R)
    RxorK = xor_on_2_lists(R_developpe, K)
    B_decoupe = decoupe_en_n_octets(6, RxorK)
    C = apply_SBox_on_list(B_decoupe)
    C_decoupe = decoupe_en_n_octets(4, C)
    return C_decoupe


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # monBin = Binaire603([0x00, 0x01, 0x02, 0x010, 0x20, 0x40, 0x80])
    fBij = fBijDES('133457799BBCDFF1', fDES, 16)
    fBij.affiche()