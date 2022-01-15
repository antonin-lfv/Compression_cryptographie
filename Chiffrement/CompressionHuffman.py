from Binaire603 import *
from CodeurCA import *


class TreeHuffman(object):
    """Chaque noeud et chaque feuille à une fréquence"""

    def __init__(self, label="", frq=0, left=None, right=None):
        """
        >>> TreeHuffman("A", 0.2)
        >>> TreeHuffman("B" , 0.2, None, None)
        >>> TreeHuffman("AB", 0.4,TreeHuffman("A" , 0.2), TreeHuffman("B" , 0.2))
        """
        self.left = left
        self.frq = frq
        self.right = right
        self.label = label

    def __repr__(self):
        return f"TreeHuffman({self.label}, {self.frq}, {self.left}, {self.right})"

    def isFeuille(self):
        return self.left == NONE and self.right == NONE

    def __add__(self, other):
        return TreeHuffman(self.label + other.label, round(other.frq + self.frq, 3), self, other)


class CompresseurHuffman(object):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un Binaire603
    C'est une forme de classe abstraites"""

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
        pass

    def arbreDepuisListePonderee(lp):
        """Transforme la liste de couple (Etiquette,Entropie) en un tuple modélisant un arbre. Un arbre pondéré est un tuple de la forme (Etiquette,pondération) ou (Arbre,pondération)
        >>> CompresseurHuffman.arbreDepuisListePonderee( [('A', 0.2), ('B', 0.3), ('C', 0.4)])
        [((('C', 0.4), ((('A', 0.2), ('B', 0.3)), 0.5)), 0.9)]
        """
        larbre = list(map(lambda x: TreeHuffman(x[0], x[1]), lp))
        while len(larbre) > 1:
            larbre = sorted(larbre, key=lambda x: x.frq)
            a = larbre.pop(0)
            b = larbre.pop(0)
            larbre.append(a + b)
        return larbre[0]

    def codageHuffman(monBin, verbose=False):
        """Renvoie les dictionnaire associant les clés d’Huffman aux valeurs d’octets"
        >>> CompresseurHuffman.codageHuffman(Binaire603([5,5,5,5,5,5,5,5,6,6,6,7,7,9]))
        ('00': 6, '01': 5, '10': 7, '11': 9, 6: '00', 5: '01', 7: '10', 9: '11')
        """
        pass

    def binCode(self, monBin, verbose=False):
        "renvoie une chaine Binaire codée par Huffman"
        pass

    def binDecode(self, binC, verbose=False):
        """renvoie une chaine Binaire decodée par Huffman
        >>> monCodeur=CompresseurHuffman()
        >>> monBin=Binaire603([6,6,6,6,6,5,5,5,5,6,6,6,7,8,9,8,8])
        >>> monBinC=monCodeur.binCode(monBin)
        >>> monBin==monCodeur.binDecode(monBinC)
        True
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()