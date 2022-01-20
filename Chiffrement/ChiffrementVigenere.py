from Binaire603 import *
from CodeurCA import *
from Texte603 import *
from arithmetiquedansZnZ import *

class ChiffreurVigenere(CodeurCA):
    def __init__(self, cle):
        super().__init__()
        self.cle = Texte603(cle).toBinaire603()

    def __str__(self):
        return f'ChiffreurVigenere({self.lPermutation})'

    def __repr__(self):
        return f'ChiffreurVigenere({self.lPermutation})'

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        """
        >>> monBin = Texte603("Une autruche").toBinaire603()
        >>> ChiffreurVigenere(cle="Bonjour les amis").binCode(monBin)
        Binaire603([ 0x97, 0xdd, 0xd3, 0x8a, 0xd0, 0xea, 0xe6, 0x92, 0xe1, 0xc8, 0xdb, 0x85])
        """
        res = []
        for i in range(len(monBinD)):
            res += [ElmtZnZ(element=monBinD[i]+self.cle[i % len(self.cle)], n=256).element]
        return Binaire603(res)

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        """
        >>> monBin = Texte603("Une autruche").toBinaire603()
        >>> code = ChiffreurVigenere(cle="Bonjour les amis").binCode(monBin)
        >>> ChiffreurVigenere(cle="Bonjour les amis").binDecode(code)
        Binaire603([ 0x55, 0x6e, 0x65, 0x20, 0x61, 0x75, 0x74, 0x72, 0x75, 0x63, 0x68, 0x65])
        """
        res = []
        for i in range(len(monBinC)):
            res += [ElmtZnZ(element=monBinC[i] - self.cle[i % len(self.cle)], n=256).element]
        return Binaire603(res)

    def demo(self, texte):
        print("<------------------------------ Début Codage ------------------------------>\n")
        monBin = Texte603(texte).toBinaire603()
        codage_vigenere = self.binCode(monBin)
        print(f"codage de la phrase : {texte}")
        print("Par -> ", codage_vigenere)
        print("Affichage avec Text603 : ", Texte603(codage_vigenere))

        print("\n<------------------------------ Début Décodage ------------------------------>\n")
        monBinC = Texte603(codage_vigenere).toBinaire603()
        decodage_vigenere = self.binDecode(monBinC)
        print(f"décodage de la phrase : {Texte603(codage_vigenere)}")
        print("Par -> ", decodage_vigenere)
        print("Affichage avec Text603 : ", Texte603(decodage_vigenere))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    texte = "Une autruche qui met la tête dans le sable, la couleur rouge qui énerve les taureaux"
    ChiffreurVigenere(cle="Bonjour les amis").demo("une autruche")