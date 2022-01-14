# Créé par vala0004, le 02/12/2021 en Python 3.7
import unicodedata
from Binaire603 import Binaire603
import re
import  numpy as np
import matplotlib.pyplot as plt
from math import *
from random import *
from CompresseurHuffman import CompresseurHuffman
#z=re.compile(r"[a-zA-Z]*") #
#w=re.compile(r"[\w]+") # mots d'au moins une lettre de \w toutes

class Texte603(object):
    """Texte603 n'hérite pas de str car c'est un type immutable
    ce qui complique l'initialisation
    Un Texte603 est formé de 256 caractères affichable directement sur l'écran'
    cad Que les caractères de contrôles ont été convertis en caractères affichables
    """
    #Construction de la liste et du dictionnaire de transcription en Ascii<>Binaire
    #Texte603.dbin["a"]==97 et  Texte603.lchr[97]== 'a'

    lchr=[chr(k) for k in range(256)]
    for k in range(32):
        lchr[k]=chr(k+256)
    lchr[0xad]=chr(k+256)
    for k in range(0x7f,0xa1):
        lchr[k]=chr(k+256)
    dbin=dict()
    for k in range(256):
        dbin[lchr[k]]=k


    def __init__(self, param):
        assert isinstance(param,Texte603) or isinstance(param,Binaire603) or isinstance(param,str)
        ch=""
        if isinstance(param,Texte603):
            ch=param.texte
        elif isinstance(param,Binaire603):
            for b in param:
                ch+=Texte603.lchr[b]
        elif isinstance(param,str):
           #param est assumé comme une chaine de caractère
           for c in param:
                ch+=Texte603.lchr[ord(c)%256]
        else:
            assert False,"Erreur impossible"
        self.texte= ch


    def __len__(self):return len(self.texte)

    def __str__(self):
        #ch=super().str()
        intro=(f'Phrase de {len(self)} caractères :"')
        txt=self.texte
        if len(txt)<140:
            res=intro+txt
        else:
            res=intro+txt[:80]+"..."+txt[-60:]
        return res+'"'
    def __repr__(self):
        return f"Texte603({self.texte})"
    def __eq__(self,other):
        if isinstance(other,Texte603):
            return self.texte==other.texte
        else:
            return self.texte==other
    def exTexte603(num=1):
        if num==0: res="aababcbbdaababcbbdbaaacabdebf"
        elif num==1:
            res = "Une autruche qui met la tête dans le sable, la couleur rouge qui énerve les taureaux… Il existe beaucoup d’idées reçues sur les animaux et le lapin n’échappe pas à la règle. L’une des plus connues à son sujet est qu’il raffolerait de carottes. Et bien, c’est faux !Même s'il est souvent représenté en train de manger ce légume orangé, le lapin domestique a une alimentation plus variée, en accord avec son système digestif fragile. Autrement dit, son menu est essentiellement constitué de foin, d’herbes et de graines. Les carottes, si nutritives soient-elles, lui sont données en complément d’autres légumes qu’il aime tout autant comme le brocoli, le chou ou encore les endives. Il mange également en très petites quantités des fruits, car ils sont souvent trop sucrés pour lui."
            res = res+"Un gourmand exigeant"
            res = res+  "Comme tout être vivant, le lapin a son petit caractère auquel s’ajoutent un goût et un odorat développés, ce qui le rend très sélectif. Si vous le regardez manger, vous pourrez voir qu’il trie ses aliments en fonction de ce qu’il aime ou non. Et s’il n’aime pas, il vous le fera savoir en boudant. C’est-à-dire soit en arrêtant de manger, soit en renversant sa mangeoire. Il n’aime pas non plus les repas routiniers et vous le signalera en s’arrachant les poils et en rongeant différents objets. C’est pourquoi, il est donc nécessaire de faire attention à ses goûts tout en lui donnant les aliments dont il a besoin."
        elif num==2:
            with open('Les miserables UTF8.txt', 'r') as f:
                res = f.read()
                #f est correctement libéré à la fin de ce bloc
                #une exception est cependant envoyé s'il y a un problème de chargement
        elif num==3:
            with open('GuerreEtPaix UTF8.txt', 'r')as f:
                res = f.read()
        else:
           res = "Le renard mange le lapin qui mange la carotte."
        return Texte603(res)
    def toBinaire603(self):
        """
        >>> Texte603(Texte603("azeéàçè").toBinaire603())
        Texte603(azeéàçè)
        """
        lb=[Texte603.dbin[c] for c in self.texte]
        return Binaire603(lb)

    def afficheCompressionParDico(self):
        print("Démo de la compression par Dictionnaire")
        w=re.compile(r"[\w]+") # mots d'au moins une lettre de \w toutes
        lm=(w.findall(self.texte))
        lmots=[m.lower() for m in lm]
        ldico=np.unique(lmots)
        print(f"Liste des {len(lmots)} mots d'un dico de {len(ldico)}:") # on cherche tous les w dans self et renvoie une liste de ceux-ci
        print("lmots:",lmots[:20])
        print("ldico:",ldico[:10])
        dico={}
        for m in lmots:
            if dico.get(m):
                dico[m]+=1
            else:
                dico[m]=1
        for m in ["lapin","et","cheval","boulet","boulets"]:
            if dico.get(m):
                print(f"{m} : {dico[m]} occurences.")
            else:
                print(f"{m} : pas d'occurences.")
        ldicoTrie= sorted(dico.items(), key=lambda x:x[1],reverse=True)
        print(ldicoTrie[:10])
        #loiMots.sort(key=lambda x : x[1],reverse=True)
        #print(loiMots[:10])
        print("lmots:",lmots[:20])
        lx=[k for k in range(len(ldicoTrie))]
        ly=[n for (m,n) in ldicoTrie]
        plt.plot(lx,ly)
        plt.show()
        s,ls=0,[]
        for y in ly:
            s+=y
            ls+=[s]
        plt.bar(lx,ls)
        plt.show()

        ldico=[m for m in dico.keys()]
        lindex=[ldico.index(m) for m in lmots]
        nbcar=0
        for m in ldico:
            nbcar+=len(m)
        print(f"On peut enregistrer ce texte de {len(self)} caractères dans ")
        print(f"une liste de {len(ldico)} mots pour un total de {nbcar} caractères")
        print(f"et une liste de {len(lindex)} entiers.")
        print(f"Soit {len(lindex)*2+nbcar*4} au lieu de {len(self)*4} octets")

        ch=""
        for k in range(100):
            ch+=ldico[lindex[k]]+" "
        print(ch)
        print()
        print("----------------------------")


    def distributionProbaLettre(self):
        "Renvoie la distribution de probabilité de chaque caractère sous la forme d'un dictionnaire ex : dP['a']=0.1 à partir de la chaine self"
        "Ainsi que la liste de ses clés avec leurs probas triées dans l'ordre décroissant de ses probabilités et son entropie"
        #https://www.delftstack.com/fr/howto/python/python-dictionary-find-key-by-value/
        n=len(self.texte)
        dDistProba={}
        for c in self.texte:
            if c in dDistProba:
                dDistProba[c]+=1/n
            else:
                dDistProba[c]=1/n

        lClesTriees= sorted(dDistProba.items(), key=lambda x:x[1],reverse=True)
        return dDistProba,lClesTriees
##
##    def entropie(dDistProba):
##        s=0
##        h=0
##        for p in dDistProba.values():
##
##            h+=- p*log(p, 2)
##
##        return h
##    def printLonguePhrase(phrase,intro="Phrase : "):
##        if len(phrase)<140:
##            print(intro+phrase)
##        else:
##            print(intro+phrase[:80]+"..."+phrase[-60:])
##
##    def afficheDistribProba(self):
##        printLonguePhrase(self)
##        dDp,lct=distributionProbaLettre(self)
##        ch=""
##        for c,p in lct:
##            ch+=(f" P({c})={p:0.3f} , ")
##        print(ch)
##        h=entropie(dDp)
##        print()
##        print(f"Entropie={h}")
##        print()
##    def test1():
##        for phrase in [pAlpha,phraseLapin,phraseAlea(),phraseGP]:
##            afficheDistribProba(phrase)
##
##    def indiceMediane(lcp):
##        "la somme peut être inférieure à 1"
##        sp=0
##        for c,p in lcp:
##            sp+=p
##        pp,k=0,0
##        while pp<0.5*sp:
##            pp+=lcp[k][1]
##            k+=1
##        return k-1
##
##    def dicoArbre(lcp):
##        "Renvoie le dico avec l'écriture binaire de chaque lettre"
##        dico={}
##        if len(lcp)==0: return {}
##        elif len(lcp)==1:
##            dico['0']=lcp[0][0]
##            return dico
##        elif len(lcp)==2:
##            dico['0']=lcp[0][0]
##            dico['1']=lcp[1][0]
##            return dico
##        kmed=indiceMediane(lcp)
##        dico0=dicoArbre(lcp[0:kmed+1])
##        dico1=dicoArbre(lcp[kmed+1:])
##        for code,caractere in dico0.items():
##            dico['0'+code]=caractere
##        for code,caractere in dico1.items():
##            dico['1'+code]=caractere
##        return dico
##
##    def dicoArbreInv(dicoA):
##        dicoAi={}
##        for code,caractere in dicoA.items():
##            dicoAi[caractere]=code
##        return dicoAi
##
##    def chaineCodee(phrase,dicoInv):
##        chc=""
##        for c in phrase:
##            chc+=dicoInv[c]
##        return chc
##
##    def chDecode(chcode,dicoA):
##        chdc=""
##        codeEnCours=""
##        for c in chcode:
##            codeEnCours+=c
##            if codeEnCours in dicoA:
##                chdc+=dicoA[codeEnCours]
##                codeEnCours=""
##        return chdc
##
##    def demoCodageFichierTexte(nomFic):
##        f = open('Les miserables.txt', 'r')
##        phraseM = f.read()
##        f.close
##        print(phraseM[:10])
##        ch=""
##        for c in phraseM:
##            ch+=f"{ord(c)}"
##        print(ch)
##    def demoCodageEntropique(self):
##        afficheDistribProba(self)
##        dDp,lcp=distributionProbaLettre(self)
##        dicoA=dicoArbre(lcp)
##        afficheDistribProba(self)
##        print(dicoA)
##        dicoAi=dicoArbreInv(dicoA)
##        chcode=chaineCodee(self,dicoAi)
##        printLonguePhrase(self)
##        printLonguePhrase(chcode, "Chaine codée : ")
##        print(f"  Soit une écriture d'une phrase de {len(self.phrase)} caractères en :")
##        print(f"{len(chcode)} bits soit {len(chcode)//8+1} octets auquel on peut ajouter la taille du dictionnaire à {len(dicoA)}")
##        chDec=chDecode(chcode,dicoA)
##        printLonguePhrase(chDec,"La chaine décodée :")
##
##    #test1()
##    #phrase=phraseLapin
##    #demoCodageEntropique(phrase)
##    f = open('Les miserables.txt', 'r')
##    phraseM = f.read()
##    f.close
##    nfin=67
##    print(phraseM[:nfin])
##    ch=""
##    for c in phraseM[:nfin]:
##        ch+=f"{ord(c):x}"
##
##    ch=""
##    for c in phraseM[:nfin]:
##        ch+=f"{ord(c):8b}."
##    print(ch)
##print()
    def demo(verbose = False):
        k=3
        t=Texte603.exTexte603(k)
        print(t)
        b=t.toBinaire603()
        if verbose:print(b)
        co1=CompresseurHuffman()
        bc=co1.binCode(b)
        if verbose:print(bc)
        print(f" Compression Huffman : {len(b)}->{len(bc)} octets")
        bc.sauvegardeDansFichier(f"Texte{k}.SVH")
        t.afficheCompressionParDico()



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    Texte603.demo()
