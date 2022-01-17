from Binaire603 import *
from CodeurCA import *
from Image603 import *


class CompressionPCX(object):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

    def __init__(self):
        pass

    def __str__(self):
        return 'Compresseur PCX'

    def __repr__(self):
        return 'CompressionPCX()'

    def binCode(self, monImD: Image603):
        # Affichage image
        # monImD.affiche()
        # Tri des couleurs par séquence
        palette = monImD.dPalette()
        print("\nNombre de couleurs : ", len(palette), "\n")
        couleur_trie = sorted(palette.items(), key=lambda item: item[1][1], reverse=True)
        print("Couleurs triées : ", *couleur_trie)

    def binDecode(self, monBinC) -> Image603:
        pass

    def demo(self):
        CompressionPCX().binCode(monImD=Image603.exImage603())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    CompressionPCX().demo()