from Binaire603 import *
from CodeurCA import *


class Chiffrement_par_decalage(object):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

    def __init__(self, decalage):
        self.decalage = decalage

    def __str__(self):
        return 'Chiffrement par décalage'

    def __repr__(self):
        return 'Chiffrement_par_decalage()'

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        """ Exemple :
        >>> Chiffrement_par_decalage(2).binCode(Binaire603([1,2,3,4,25]))
        Binaire603([ 0x03, 0x04, 0x05, 0x06, 0x1b])
        """
        return Binaire603(list(map(lambda x: (x + self.decalage) % 255, monBinD)))

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        """ Exemple :
        >>> Chiffrement_par_decalage(2).binDecode(Binaire603([1,2,3,4,25]))
        Binaire603([ 0xfe, 0x00, 0x01, 0x02, 0x17])
        """
        return Binaire603(list(map(lambda x: (x - self.decalage) % 255, monBinC)))

    def demo(self):
        print("Source : Binaire603([1, 2, 3, 4, 25])")
        code = Chiffrement_par_decalage(2).binCode(Binaire603([1, 2, 3, 4, 25]))
        print("Codage : ", code)
        decode = Chiffrement_par_decalage(2).binDecode(code)
        print("Decodage : ", decode)
        print("Final : ", list(map(int, decode)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    Chiffrement_par_decalage(2).demo()