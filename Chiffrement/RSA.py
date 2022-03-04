from arithmetiquedansZnZ import *
from CodeurCA import *
from math import isqrt
from tqdm import tqdm


def est_premier(n) -> bool:
    """Test de primalité de n"""
    if n < 2:
        return False
    else:
        for i in [2] + [j for j in range(3, isqrt(n), 2)]:
            if n % i == 0:
                return False
    return True


class RSA(CodeurCA):
    def __init__(self):
        super().__init__()
        ...

    def binCode(self, monBin):
        ...

    def binDecode(self, monBin):
        ...

    def estPremierOuPseudoDansLaBase(self, n, a):
        compt = 0
        k = n - 1
        if n % 2 == 0:
            return n == 2

        while k % 2 == 0:
            k = k // 2
            compt += 1
        # print('while fini : k =', k)
        a_puiss_k = ElmtZnZ(exponentiation_rapide(a, k, n), n)
        if (a_puiss_k - 1).element == 0:
            return True

        while (1 + a_puiss_k).element != 0:
            a_puiss_k = a_puiss_k ** 2
            if compt == 0:
                return False
            compt -= 1
        return True

    def lNombresDePoulet(self, nbits=16):
        """
        >>> lNombresDePoulet(10)
        [341, 561, 645]
        """
        poulet = []
        for i in range(3, 2 ** nbits, 2):
            if self.estPremierOuPseudoDansLaBase(i, 11) != est_premier(i):
                poulet.append(i)
        return poulet

    def demo(self):
        nombre = int(input('Entrez un nombre à tester : '))
        nombre_immense_premier = 437212001701879637766091976066257388544571841825536058979465855736280833480029807855483835507842022082185642501603395212475014204294781564593885165916571682367465153926064731225315581926491958119496723813429196076222167401614084965382977216114596978781389301174770679647014435214817593689457872635541156086100802908752710858557000998408438544807285497495407540913523607129038001300117679268731405211861644475965918435145719474677294951685917276454383880871710224211242044307245268691845169450191268320612053586467525092953457720055152483289223848523920777378403568047383859403096102630757632670407588914774752488493618615090974520666446008199518057884604105480883125088709277279427351853504986152934251320824363771487740252811140921716702639745005555654797949738461690847313595719547433379951656816499713560821978132748412239857063210088907400741732087124880276250609875093475790304674267859529934984319869324927360205144241115828277369372884700694318402310994189557166402270230230812974491808157330433985995663645004901826747452579772965488267757150189765991530293302933916785966289496906612249954618754042368036920472516786504058314372159389121160715137357026185760486087982154209471867816725439331
        if self.estPremierOuPseudoDansLaBase(nombre, a=2):
            print(nombre, "est premier")
        else:
            print(nombre, "n'est pas premier")

        print("Les poulets inferieurs à 2**nbits : ", self.lNombresDePoulet(10))


if __name__ == "__main__":
    # RSA().demo()

    from tqdm import tqdm
    def estPremierOuPseudoDansLaBase(n, a):
        compt = 0
        k = n - 1
        if n % 2 == 0:
            return n == 2

        while k % 2 == 0:
            k = k // 2
            compt += 1
        # print('while fini : k =', k)
        a_puiss_k = ElmtZnZ(exponentiation_rapide(a, k, n), n)
        if (a_puiss_k - 1).element == 0:
            return True

        while (1 + a_puiss_k).element != 0:
            a_puiss_k = a_puiss_k ** 2
            if compt == 0:
                return False
            compt -= 1
        return True


    compteur = 0
    tot = 0
    bonnes_reponses = 0
    mauvaises_reponses = 0
    import plotly.graph_objects as go
    from plotly.offline import plot
    fig=go.Figure()
    for i in tqdm(range(2, 10000, 1)):
        if estPremierOuPseudoDansLaBase(i, 2):
            compteur += 1
            fig.add_scatter(x=[i], y=[compteur], marker=dict(color='red', size=2))
        if est_premier(i):
            tot += 1
            fig.add_scatter(x=[i], y=[tot], marker=dict(color='blue', size=2))
        if est_premier(i) and estPremierOuPseudoDansLaBase(i, 2):
            bonnes_reponses+=1
        elif ( est_premier(i) and not estPremierOuPseudoDansLaBase(i, 2)) or ( not est_premier(i) and estPremierOuPseudoDansLaBase(i, 2)) :
            mauvaises_reponses+=1
            fig.add_scatter(x=[i], y=[mauvaises_reponses], marker=dict(color='green', size=2))
    fig.update_layout(showlegend=False)
    plot(fig)
    print("Bonnes réponses de Fermat : ", bonnes_reponses)
    print("Mauvaises réponses de Fermat : ", mauvaises_reponses)
    print("Nombre totale de nombres premiers : ", tot)