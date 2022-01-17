from Binaire603 import *
from CodeurCA import *


class TreeHuffman(object):
    """Chaque noeud et chaque feuille à une fréquence"""

    def __init__(self, label="", frq=0, left=None, right=None):
        self.left = left
        self.frq = frq
        self.right = right
        self.label = label
        self.parcours_prefixe_liste = []

    def __repr__(self):
        return f"TreeHuffman({self.label}, {self.frq}, {self.left}, {self.right})"

    def isFeuille(self):
        return self.left == NONE and self.right == NONE

    def parcours_prefixe(self, l):
        """Retourne au final le parcours préfixe de l'arbre, dans la liste l"""
        l.append(self.label)
        if self.left:
            l.append('0')
            self.left.parcours_prefixe(l)
        if self.right:
            l.append('1')
            self.right.parcours_prefixe(l)
        return l

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
        """A parir du parcours prefixe, on retrouve le codage de huffman
        >>> arbre = CompresseurHuffman.arbreDepuisListePonderee([('A', 0.2), ('B', 0.3), ('C', 0.4), ('D', 0.1)])
        >>> CompresseurHuffman.dicoHuffmanDepuisArbre(arbre)
        {'C': '0', 'B': '10', 'D': '110', 'A': '111'}
        """
        parcours_prefx = arbre.parcours_prefixe(l=[])
        print(parcours_prefx)
        dico = {}
        last=""
        for i in range(1, len(parcours_prefx)-1, 4):
            if len(parcours_prefx[i+1]) == 1:
                dico[parcours_prefx[i+1]] = last+parcours_prefx[i]
            if len(parcours_prefx[i+3]) == 1:
                dico[parcours_prefx[i+3]] = last+parcours_prefx[i+2]
            last += parcours_prefx[i + 2]
        return dico

    def arbreDepuisListePonderee(lp)->TreeHuffman:
        """Transforme la liste de couple (Etiquette,Entropie) en un tuple modélisant un arbre. Un arbre pondéré est un tuple de la forme (Etiquette,pondération) ou (Arbre,pondération)
        >>> CompresseurHuffman.arbreDepuisListePonderee( [('A', 0.2), ('B', 0.3), ('C', 0.4)])
        TreeHuffman(CAB, 0.9, TreeHuffman(C, 0.4, None, None), TreeHuffman(AB, 0.5, TreeHuffman(A, 0.2, None, None), TreeHuffman(B, 0.3, None, None)))
        """
        # [((('C', 0.4), ((('A', 0.2), ('B', 0.3)), 0.5)), 0.9)]
        larbre = list(map(lambda x: TreeHuffman(x[0], x[1]), lp))
        while len(larbre) > 1:
            larbre = sorted(larbre, key=lambda x: x.frq)
            a = larbre.pop(0)
            b = larbre.pop(0)
            larbre.append(a + b)
        return larbre[0]

    def demo(self):
        a = CompresseurHuffman.arbreDepuisListePonderee([('A', 0.2), ('B', 0.3), ('C', 0.3), ('D', 0.1), ('E', 0.1)])
        print("Arbre de départ : ", a)
        print("Codage Huffman : ", CompresseurHuffman.dicoHuffmanDepuisArbre(a))
        return a

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    arbre = CompresseurHuffman().demo()

"""def codageHuffman(monBin, verbose=False):
Renvoie les dictionnaire associant les clés d’Huffman aux valeurs d’octets"
>>> CompresseurHuffman.codageHuffman(Binaire603([5,5,5,5,5,5,5,5,6,6,6,7,7,9]))
('00': 6, '01': 5, '10': 7, '11': 9, 6: '00', 5: '01', 7: '10', 9: '11')

pass

def binCode(self, monBin, verbose=False):
"renvoie une chaine Binaire codée par Huffman"
pass

def binDecode(self, binC, verbose=False):
renvoie une chaine Binaire decodée par Huffman
>>> monCodeur=CompresseurHuffman()
>>> monBin=Binaire603([6,6,6,6,6,5,5,5,5,6,6,6,7,8,9,8,8])
>>> monBinC=monCodeur.binCode(monBin)
>>> monBin==monCodeur.binDecode(monBinC)
True
pass"""