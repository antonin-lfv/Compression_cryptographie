from abc import ABC

import Binaire603
from Permutation603 import *
from CodeurCA import *
from Binaire603 import *
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from tqdm import tqdm  # progress bar
from math import log


class Hacheur_somme_carree(CodeurCA, ABC):

    def __init__(self):
        super().__init__()

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        return sum(list(map(lambda x: x ** 2 + np.exp(x), monBinD)))

    def demo(self):
        monBinD1 = Binaire603([1, 0, 2, 3, 4])
        print(f"Hache de {monBinD1} -> {Hacheur_somme_carree().binCode(monBinD1)}")
        monBinD2 = Binaire603(monBinD1[::-1])
        print(f"Hache de {monBinD2} -> {Hacheur_somme_carree().binCode(monBinD2)}")

    def trouver_collision(self, taille=20):
        table, compt, flag = {}, 0, True
        while flag:
            valeurs = Binaire603.exBin603(taille=taille, num=2)
            h = Hacheur_somme_carree().binCode(valeurs)
            if h in table.keys():
                flag = False
            else:
                table[h] = valeurs
            compt += 1
        # print(f'Collision trouvée à l\'itération {compt}')
        return compt

    def afficher_collision(self, mode):  # mode = boxplot ou points
        fig = go.Figure()
        a = 10
        b = a + 35
        for i in tqdm(range(a, b, 2)):
            data = []
            for j in range(15):
                h = Hacheur_somme_carree().trouver_collision(taille=i)
                data.append(log(h, 10))
            if mode == "boxplot":
                fig.add_box(y=data, name=i, showlegend=False)
            else:
                fig.add_scatter(x=[i], y=[np.mean(data)], mode='markers', showlegend=False)
        fig.update_layout(
            xaxis_title="Taille en octet",
            yaxis_title="Itérations avant première collision (plusieurs tests)"
        )
        plot(fig)


if __name__ == '__main__':
    # Hacheur_somme_carree().demo()
    # Hacheur_somme_carree().trouver_collision(taille=100)
    Hacheur_somme_carree().afficher_collision(mode="boxplot")
