from Binaire603 import *
from CodeurCA import *
from Texte603 import *
from arithmetiquedansZnZ import *


class Chiffrement_affine(object):
    def __init__(self, a, b):
        self.a = a
        assert ElmtZnZ(self.a, 256).estInversible()
        self.b = b

    def __str__(self):
        return 'Chiffrement affine'

    def __repr__(self):
        return f'Chiffrement_affine({self.a},{self.b})'

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        return Binaire603(list(map(lambda x: (self.a * x + self.b) % 256, monBinD)))

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        return Binaire603(list(map(lambda x: 1, monBinC)))

    def demo(self):
        print("\n<--------- A partir d'un Binaire 603 --------->")
        print("Source : Binaire603([1, 2, 3, 4, 1])")
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
