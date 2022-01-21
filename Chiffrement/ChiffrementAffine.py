from Binaire603 import *
from CodeurCA import *
from Texte603 import *
from arithmetiquedansZnZ import *


class Chiffrement_affine(CodeurCA):
    def __init__(self, a, b):
        super().__init__()
        self.a = ElmtZnZ(a, 256).element
        assert ElmtZnZ(a, 256).estInversible()
        self.b = ElmtZnZ(b, 256).element

    def __str__(self):
        return 'Chiffrement affine'

    def __repr__(self):
        return f'Chiffrement_affine({self.a},{self.b})'

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        """ Codage par la fonction ax+b dans Z/256Z
        >>> monBin = Binaire603([1, 2, 3, 4, 25])
        >>> Chiffrement_affine(3, 1).binCode(monBin)
        Binaire603([ 0x04, 0x07, 0x0a, 0x0d, 0x4c])
        """
        return Binaire603(list(map(lambda x: ElmtZnZ(element=self.a * x + self.b, n=256).element, monBinD)))

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        """ Décodage par la fonction (x-b)*a^(-1) dans Z/256Z
        >>> monBin = Binaire603([1, 2, 3, 4, 25])
        >>> code = Chiffrement_affine(3, 1).binCode(monBin)
        >>> Chiffrement_affine(3, 1).binDecode(code)
        Binaire603([ 0x01, 0x02, 0x03, 0x04, 0x19])
        """
        # Cast en int pour qu'il soit accepté par Binaire603
        return Binaire603(list(map(lambda x: int(((x-self.b)*ElmtZnZ(element=self.a, n=256).inverse()).element), monBinC)))

    def demo(self):
        print("\n<--------- A partir d'un Binaire 603 --------->")
        print("Source : Binaire603([1, 2, 3, 4, 25])")
        code = Chiffrement_affine(self.a, self.b).binCode(Binaire603([1, 2, 3, 4, 25]))
        print(f"Codage avec {self.a}x+{self.b}: ", code)
        decode = Chiffrement_affine(self.a, self.b).binDecode(code)
        print("Decodage : ", decode)
        print("Final : ", list(map(int, decode)))
        print("\n<--------- A partir d'un Text 603 ------------>")
        print("Source Text603('Ceci est un texte')")
        code = Chiffrement_affine(self.a, self.b).binCode(Texte603("Ceci est un texte").toBinaire603())
        print(f"Codage avec {self.a}x+{self.b}: ", code)
        decode = Chiffrement_affine(self.a, self.b).binDecode(code)
        print("Decodage : ", decode)
        print("Final : ", Texte603(decode))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    Chiffrement_affine(3, 1).demo()
