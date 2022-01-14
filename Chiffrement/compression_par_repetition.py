from Binaire603 import *
from CodeurCA import *


class Compression_par_repetition(object):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

    def __init__(self):
        pass

    def __str__(self):
        return 'Compresseur par répétition'

    def __repr__(self):
        return 'Compression_par_repetition()'

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        """ Exemple :
        >>> Compression_par_repetition().binCode(Binaire603([7,7,7,8,6,6,7,7,9]))
        Binaire603([ 0x03, 0x07, 0x01, 0x08, 0x02, 0x06, 0x02, 0x07, 0x01, 0x09])
        """
        # TODO : gérer le cas si on a plus de 255 fois la même lettre
        tabComp = []
        elm = monBinD[0]
        nelm = 1
        for i in range(1, len(monBinD)):
            if monBinD[i] == elm:
                nelm += 1
            else:
                tabComp.append(nelm)
                tabComp.append(elm)
                elm = monBinD[i]
                nelm = 1
        tabComp.append(nelm)
        tabComp.append(elm)
        return Binaire603(tabComp)

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        """ Exemple :
        >>> Compression_par_repetition().binDecode(Binaire603([3,7,1,8,2,6,2,7,1,9]))
        Binaire603([ 0x07, 0x07, 0x07, 0x08, 0x06, 0x06, 0x07, 0x07, 0x09])
        """
        # TODO : gérer le cas si on a plus de 255 fois la même lettre
        res = []
        for i in range(0, int(len(monBinC)), 2):
            res += (monBinC[i] * [monBinC[i + 1]])
        return Binaire603(res)

    def demo(self):
        print("Source : Binaire603([7, 7, 7, 8, 6, 6, 7, 7, 9, 7, 9, 10, 2, 89, 255])")
        code = Compression_par_repetition().binCode(Binaire603([7, 7, 7, 8, 6, 6, 7, 7, 9, 7, 9, 10, 2, 89, 255]))
        print("Codage : ", code)
        decode = Compression_par_repetition().binDecode(code)
        print("Decodage : ", decode)
        print("Final : ", list(map(int, decode)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    Compression_par_repetition().demo()
