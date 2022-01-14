from Binaire603 import *
from CodeurCA import *


class TreeHuffman(object):
    """Chaque noeud et chaque feuille à une fréquence"""

    def __init__(self, frq, label="", left=None, right=None):
        """
        >>> TreeHuffman(0.2, "A")
        >>> TreeHuffman(0.2 , A, None, None)
        >>> TreeHuffman(0.4, "AB",TreeHuffman(0.2, "A"), TreeHuffman(0.2, "B"))
        TreeHuffman(0.4 , AB, TreeHuffman(0.2 , A, None, None), TreeHuffman(0.2 , B, None, None))
        """
        self.frq = frq
        self.left = left
        self.right = right
        self.label = label

    def __repr__(self):
        return f"TreeHuffman({self.frq} , {self.label}, {self.left}, {self.right})"

    def isFeuille(self):
        return self.left == NONE and self.right == NONE

    def __add__(self, other):
        return TreeHuffman(other.frq + self.frq, self.label + other.label, self, other)


class CompressionHuffman(object):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

    # ODO créer classe arbre
    """    
    recevoir la liste trier par freq
    transfo vers arbre
    huffman -> 2 derniers puis fusion tant qu'il n'y a pas qu'un seul element
    """

    def __init__(self):
        pass

    def __str__(self):
        return 'Compresseur par répétition'

    def __repr__(self):
        return 'CompressionHuffman()'

    def dicoHuffmanDepuisArbre(arbre):
        """Renvoie les dictionnaires associant les étiquettes à leur codage d’Huffman (format txt)
        >>> a=CompresseurHuffman.arbreDepuisListePonderee([("B",0.3),("L",0.2),("E",0.2),("I",0.1),("A",0.1)])
        >>> CompresseurHuffman.dicoHuffmanDepuisArbre(a) ({'000': 'E', '0010': 'S', '0011': 'N',
        ’0100’: ’A’, ’0101’: ’T’, ’011’: ’I’, ’10’: ’B’, ’11’: ’L’}, {’E’: ’000’, ’S’: ’0010’, ’N’:
        ’0011’, ’A’: ’0100’, ’T’: ’0101’, ’I’: ’011’, ’B’: ’10’, ’L’: ’11’})
        >>> CompresseurHuffman.construireDicoH(arbre1,d)
        >>> print(d)
        '0': 'A', '10': 'B', '11': 'C'
        """

    def arbreDepuisListePonderee(lp):
        """Transforme la liste de couple (Etiquette,Entropie) en un tuple modélisant un arbre. Un arbre pondéré est un tuple de la forme (Etiquette,pondération) ou (Arbre,pondération)
        >>> CompresseurHuffman.arbreDepuisListePonderee([("A",0.2),("B",0.3),("C",0.4)])
        (((((’B’, 0.3), (’A’, 0.2)), 0.5), (’C’, 0.4)), 0.9)
        """
        pass

    def codageHuffman(monBin, verbose=False):
        """Renvoie les dictionnaire associant les clés d’Huffman aux valeurs d’octets"
        >>> CompresseurHuffman.codageHuffman(Binaire603([5,5,5,5,5,5,5,5,6,6,6,7,7,9]))
        (’00’: 6, ’01’: 5, ’10’: 7, ’11’: 9, 6: ’00’, 5: ’01’, 7: ’10’, 9: ’11’)
        """
        pass

    def binCode(self, monBin, verbose=False):
        "renvoie une chaine Binaire codée par Huffman"
        pass

    def binDecode(self, binC, verbose=False):
        """renvoie une chaine Binaire decodée par Huffman
        >>> monCodeur=CompresseurHuffman()
        >>> monBin=Binaire603([6,6,6,6,6,5,5,5,5,6,6,6,7,8,9,8,8]) »> monBinC=monCodeur.binCode(monBin)
        >>> monBin==monCodeur.binDecode(monBinC)
        True
        """
        pass



if __name__ == "__main__":
    import doctest

    doctest.testmod()