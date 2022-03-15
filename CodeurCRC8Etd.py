from Binaire603 import *
from Texte603 import Texte603
from CodeurCA import CodeurCA
from PolF2Etd import *


class CodeurCRC8(CodeurCA):
    """CodeurCRC codant en 40bits des blocs 32bits avec CRC sur 8bits"""

    def __init__(self, Pg=PolF2(0b110011011)):
        super().__init__()
        assert Pg.degre() <= 8
        self.Pg = Pg

    def __str__(self):
        return f'CodeurCRC avec {self.Pg=}'

    def __repr__(self):
        return f"CodeurCRC8(Pg=PolF2(0b{int(self.Pg):b}))"

    def blocCode(self, M, verbose=False):
        '''Renvoie M codé en CRC avec un octet de plus"
        >>> print(f"0x{CodeurCRC8().blocCode(0xab345678):x}")
        0xab34567821
        '''
        PnXr = PolF2(M).mulMonome(self.Pg.degre())  # deg 32
        Pc = PnXr + PnXr % self.Pg  # deg 40

        return int(Pc)

    def estBlocValide(self, valc):
        """
        >>> CodeurCRC8().estBlocValide(0xab34567821)
        True
        >>> CodeurCRC8().estBlocValide(0xab34567820)
        False
        """
        ...

    def blocValideLePlusProche(self, valc, verbose=False):
        """
        >>> print(f"0x{CodeurCRC8().blocValideLePlusProche(0xab34567821):x}")
        0xab34567821
        >>> print(f"0x{CodeurCRC8().blocValideLePlusProche(0xab35567821):x}")
        0xab34567821
        """
        pass

    def blocDecode(self, valc):
        """
        >>> print(f"0x{CodeurCRC8().blocDecode(0xab34567821):x}")
        0xab345678
        >>> print(f"0x{CodeurCRC8().blocDecode(0xbb34567821):x}")
        0xab345678
        """
        p = PolF2(valc)
        if p % self.Pg != 0:
            # erreur
            for i in range(31):
                mcor = xor(valc, 2**i)
                if estBlocValide(mcor):
                    return True
        else:
            # pas d'erreur
            ...

    def blocAvecErreur(val, nbBits=32, nbErreurs=1):
        """Renvoie le bloc val avec nbErreurs bits changés"""
        res = val
        for _ in range(nbErreurs):
            res = res ^ (1 << randint(0, nbBits - 1))
        return res

    def binCode(self, monBinD, verbose=True, nbErreurs=0):

        # Ajouter nbErreurs au à chaque bloc
        # berr=CodeurCRC8.blocAvecErreur(bloc,nbBits=32,nbErreurs=nbErreurs)
        ...

    def testDistance(self, nmax=0x21):
        min = 1000
        for b1 in range(nmax):

            P1 = PolF2(self.blocCode(b1))
            for b2 in range(b1 + 1, nmax):

                P2 = PolF2(self.blocCode(b2))
                d = PolF2.distanceHamming(P1, P2)
                if d < min:
                    print(f"{b1:b} et {b2:b} ont pour PolCRC {P1} et {P2} dont la distance est {d}")
                    min = d
        print(f"La distance de Hamming minimale avec {(self)} pour deux blocs inférieurs à {nmax} est {min}")

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        pass

    def testDecodageDesErreurs(self, nbErreurs=1):
        """Renvoie la distance minimales entre les codage des blocs 0 ) nmax"""
        for k1 in range(1, 3):
            for k2 in range(3):
                m = 0x21000000 * k2 + 1001 * k1
                blocA = self.blocCode(m)
                blocB = CodeurCRC8.blocAvecErreur(blocA, nbBits=32, nbErreurs=nbErreurs)
                blocC = self.blocValideLePlusProche(blocB)
                blocD = self.blocDecode(blocC)

                print(f"{m=:x},{blocA=:x},{blocB=:x},{blocC=:x},{blocD=:x},{blocD == m}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    monCodeur = CodeurCRC8()
    monCodeur.testDecodageDesErreurs()
    monBin = Texte603("Bonjour les copains !!!").toBinaire603()
    # monBin=Binaire603([7,10,19,67])
    for nbE in range(3):
        print(f"Test avec {nbE} erreurs ajoutées")
        monBinC = monCodeur.binCode(monBin, nbErreurs=nbE)
        monBinD = monCodeur.binDecode(monBinC)
        print("Bin Codée:", monBinC)
        print("Bin décodé : ", Texte603(monBinD))
    monCodeur.testDistance()
