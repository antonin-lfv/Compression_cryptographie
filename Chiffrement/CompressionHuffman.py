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
        return self.left is None and self.right is None

    def recherche(self, label_cherche):
        if self.label == label_cherche:
            return self
        if label_cherche in self.right.label:
            return self.right.recherche(label_cherche)
        elif label_cherche in self.left.label:
            return self.left.recherche(label_cherche)
        else:
            return "valeur non trouvé"

    def parcours_prefixe(self, l):
        """Retourne au final le parcours préfixe de l'arbre, dans la liste l"""
        l.append(str(self.label))
        if self.left:
            l.append('0')
            self.left.parcours_prefixe(l)
        if self.right:
            l.append('1')
            self.right.parcours_prefixe(l)
        return l

    def __add__(self, other):
        return TreeHuffman(str(self.label) + str(other.label), round(other.frq + self.frq, 3), self, other)


class CompresseurHuffman(CodeurCA):
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
        super().__init__()

    def __str__(self):
        return 'Compresseur par répétition'

    def __repr__(self):
        return 'CompressionHuffman()'

    def dicoHuffmanDepuisArbre(arbre):
        """A parir du parcours prefixe, on retrouve le codage de huffman"""
        parcours_prefx = arbre.parcours_prefixe(l=[])
        etiquette_code, code_etiquette = {}, {}
        for lettre in parcours_prefx[0]:
            path_lettre = ""
            for j in range(2, len(parcours_prefx), 2):
                if lettre in parcours_prefx[j]:
                    path_lettre += parcours_prefx[j-1]
            etiquette_code[lettre] = path_lettre
            code_etiquette[path_lettre] = lettre
        return etiquette_code, code_etiquette


    def arbreDepuisListePonderee(lp) -> TreeHuffman:
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

    def codageHuffman(monBin, verbose=False):
        """
        >>> CompresseurHuffman.codageHuffman(Binaire603([5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 9]))
        ({'9': '000', '7': '001', '6': '01', '5': '1'}, {'000': '9', '001': '7', '01': '6', '1': '5'})
        """
        freq = monBin.dFrequences()
        liste_pondere = list({x: y for x, y in freq.items() if y != 0}.items())
        a = CompresseurHuffman.arbreDepuisListePonderee(liste_pondere)
        return CompresseurHuffman.dicoHuffmanDepuisArbre(a)

    def binCode(self, monBin, verbose=False):
        "renvoie une chaine Binaire codée par Huffman"
        dico = CompresseurHuffman.codageHuffman(monBin)
        codage=""
        for element in monBin:
            codage+=dico[0][str(element)]
        return codage


    def binDecode(self, binC, dico, verbose=False):
        """renvoie une chaine Binaire decodée par Huffman
        >>> monCodeur=CompresseurHuffman()
        >>> monBin=Binaire603([6,6,6,6,6,5,5,5,5,6,6,6,7,8,9,8,8])
        >>> monBinC=monCodeur.binCode(monBin)
        >>> monCodeur.binDecode(monBinC, dico=CompresseurHuffman.dicoHuffmanDepuisArbre(CompresseurHuffman.arbreDepuisListePonderee(list({x: y for x, y in monBin.dFrequences().items() if y != 0}.items())))[1])
        Binaire603([ 0x06, 0x06, 0x06, 0x06, 0x06, 0x05, 0x05, 0x05, 0x05, 0x06, 0x06, 0x06, 0x07, 0x08, 0x09, 0x08, 0x08])
        """
        decodage= []
        while binC!="":
            i=0
            while i!=len(binC) and binC[:len(binC)-i] not in dico.keys():
                i+=1
            decodage.append(int(dico[binC[:len(binC)-i]]))
            binC=binC[len(binC)-i:]
        return Binaire603(decodage)

    def demo(self):
        print("\n-------------------------------------- Zone de test et affichage ---------------------------------------------")
        liste_pond = [('A', 0.2), ('B', 0.3), ('C', 0.3), ('D', 0.1), ('E', 0.1)]
        a = CompresseurHuffman.arbreDepuisListePonderee(liste_pond)
        print("Arbre de départ : ", a)
        print("Parcours prefixe : ", a.parcours_prefixe(l=[]))
        # print("Codage Huffman : ", CompresseurHuffman.dicoHuffmanDepuisArbre(a))
        # CompresseurHuffman.dico_Huff(a)
        print("recherche de ADE : ", a.recherche('ADE'))
        print("Dico Huffman : ", CompresseurHuffman.dicoHuffmanDepuisArbre(a))
        print("\n-------------------------------------- Exemple du TP ---------------------------------------------------------")
        print("Exemple avec Binaire603([5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 9]) ")
        monBinaire = Binaire603([5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 9])
        print("Codage par Huffman : ", CompresseurHuffman().binCode(monBinaire))
        dico = CompresseurHuffman.dicoHuffmanDepuisArbre(CompresseurHuffman.arbreDepuisListePonderee(list({x: y for x, y in monBinaire.dFrequences().items() if y != 0}.items())))
        print("Avec le dictionnaire : ", dico)
        print("Decodage : ", CompresseurHuffman().binDecode(CompresseurHuffman().binCode(monBinaire), dico=dico[1]))
        return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    arbre = CompresseurHuffman().demo()