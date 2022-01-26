from abc import ABC

from arithmetiquedansZnZ import *
from CodeurCA import *


class Chiffreur_Feistel(CodeurCA, ABC, ABC):
    def __init__(self, cle):
        super().__init__()
        self.cle = cle
        self.nb_tour = len(self.cle)

    def chiffrement(self):
        raise NotImplementedError

    def dechiffrement(self):
        raise NotImplementedError

    def demo(self, message):
        pass


if __name__ == "__main__":
    Chiffreur_Feistel(cle="oui").demo("Le message")
