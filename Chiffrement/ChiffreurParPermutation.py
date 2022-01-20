from Binaire603 import *
from CodeurCA import *
from Texte603 import *
from arithmetiquedansZnZ import *


class ChiffreurParPermutation(CodeurCA):
    def __init__(self, lPermutation=[]):
        super().__init__()
        self.lPermutation = lPermutation

    def __str__(self):
        return f'ChiffreurParPermutation({self.lPermutation})'

    def __repr__(self):
        return f'ChiffreurParPermutation({self.lPermutation})'

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        """"
        >>> mc = ChiffreurParPermutation(102 * [0x51])
        >>> mc.binCode(Binaire603([1, 2, 3, 4, 5]))
        Binaire603([0x51, 0xa2, 0xf3, 0x44, 0x95])
        """
        raise NotImplementedError

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        """
        >>> mc = ChiffreurParPermutation(102 * [0x51])
        >>> mc.binDecode(mc.binCode(Binaire603([1,2,3,4,5])))
        Binaire603([ 0x01, 0x02, 0x03, 0x04, 0x05])
        """
        raise NotImplementedError

    def demo(self):
        pass


if __name__ == "__main__":
    import doctest

    # doctest.testmod()