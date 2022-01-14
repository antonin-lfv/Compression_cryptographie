import numpy as np
from archive.Arithmetique import *

def table_addition(n):
    tab = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            tab[i, j] = (i + j) % n
    return tab

def table_multiplication(n):
    tab = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            tab[i, j] = (i * j) % n
    return tab

def phi(n):
    facteurs = facteurs_premiers(n)
    resultat = 1
    for i in facteurs:
        resultat *= i - 1
    return resultat

class Z_sur_nZ:
    def __init__(self, n):
        self.n = n
        self.table_add = table_addition(self.n)
        self.table_mult = table_multiplication(self.n)
        self.indicatrice = phi(self.n)

    def afficher_inverses(self):
        """Affche tous les inverses"""
        for (i, j) in zip(np.where(self.table_mult == 1)[0], np.where(self.table_mult == 1)[1]):
            print("Inverse de " + str(i) + " = " + str(j))

    def inverse(self, m):
        """Renvoie l'inverse de m dans Z/nZ"""
        ligne = self.table_multiplication[m]
        return np.where(ligne == 1)[0][0]

    def afficher_table_mult(self):
        """Affiche la table de multiplication dans Z/nZ"""
        print(self.table_mult)

    def afficher_table_add(self):
        """Affiche la table d'addition dans Z/nZ"""
        print(self.table_add)

    def somme(self, a, b):
        """Somme de a et b dans Z/nZ"""
        return (a + b) % self.n

    def multiplication(self, a, b):
        """Multiplication de a et b dans Z/nZ"""
        return (a * b) % self.n