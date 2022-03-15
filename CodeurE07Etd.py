
from Binaire603 import Binaire603
from Texte603 import Texte603

from arithmetiqueDansZ import *
from ElemtE07 import ElemtE07
from math import log

class CodeurE0765537(object):
    """Codeur à partir de la courbe elliptique sur F65537"""
    def __init__(self,a,B,G=ElemtE07(47106,21934,65537),p =65537):
        """Dans les valeurs par défaut B=54321*G
        """
        assert log(p,2)>16
        self.a=12345
        self.A=self.a*G
        self.G=G
        self.B=B
        self.p=p

    def getClePublique(): return self.A

    def __str__(self):
        return f"CodeurE0765537 avec la clé privé {self.a=} et sa clé publique {self.A=}, la clé publique d'un tier {self.B=}, avec comme point générateur {self.G=} sur F{self.p}"
    def __repr__(self):
        return f"CodeurE0765537({self.a},{self.B},{self.G},{self.p})"

    def binCode(self,monBinD:Binaire603)->Binaire603:
        """ """
        monBinC=Binaire603()
        for b in monBinD:
            m=b*256
            M=ElemtE07.elemtE07APartirDeX(ElmtZnZ(m,self.p))
            MP=M+a*B
            monBinC.ajouteMot40b(MP.__hash__())
        return monBinC
    def binDecode(self,monBinC:Binaire603)->Binaire603:
        pos=0
        monBinD=Binaire603()
        while pos<len(monBinC):
            h,pos=monBinC.lisMot(5,pos)
            MP=ElemtE07.ElemtE07DepuisHash(h,self.p)
            M=MP-a*B
            monBinD.ajouteOctet(M.x.a//256)
        return monBinD

G=ElemtE07(47106,21934,65537)
a,b=12345,54321
A,B=a*G,b*G
ca=CodeurE0765537(a,B)
cb=CodeurE0765537(b,A)
mes=Texte603("Bonjour les amis !")
print(f"Message à coder :{mes}")
binc=ca.binCode(mes.toBinaire603())
print(f"Message codé avec la clé secrète de {a=} et la clé publique {B=} :{Texte603(binc)}")
bind=cb.binDecode(binc)
print(f"Message décodé avec la clé secrète de {b=} et la clé publique {A=} :{Texte603(bind)}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()