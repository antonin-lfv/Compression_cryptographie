from Binaire603 import *
from CodeurCA import *


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

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        # Tri des couleurs par séquence
        pass

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        pass

    def demo(self):
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()