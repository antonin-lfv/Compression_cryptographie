from Binaire603 import *
from CodeurCA import *
from Texte603 import *
from arithmetiquedansZnZ import *

class Chiffrement_par_decalage(CodeurCA):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

    def __init__(self, decalage):
        super().__init__()
        self.decalage = decalage

    def __str__(self):
        return 'Chiffrement par décalage'

    def __repr__(self):
        return f'Chiffrement_par_decalage({self.decalage})'

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
        print("\n<--------- A partir d'un Binaire 603 --------->")
        print("Source : Binaire603([1, 2, 3, 4, 25])")
        code = Chiffrement_par_decalage(2).binCode(Binaire603([1, 2, 3, 4, 25]))
        print("Codage : ", code)
        decode = Chiffrement_par_decalage(2).binDecode(code)
        print("Decodage : ", decode)
        print("Final : ", list(map(int, decode)))
        print("\n<--------- A partir d'un Text 603 ------------>")
        print("Source Text603('Ceci est un texte')")
        code = Chiffrement_par_decalage(2).binCode(Texte603("Ceci est un texte").toBinaire603())
        print("Codage : ", code)
        decode = Chiffrement_par_decalage(2).binDecode(code)
        print("Decodage : ", decode)
        print("Final : ", Texte603(decode))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    Chiffrement_par_decalage(2).demo()