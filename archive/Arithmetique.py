from math import isqrt

def bezout(a, b) -> int:
    """Trouver la relation de bezout tq au+bv=pgcd(a,b)"""
    s, t, u, v = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, s, t, b, u, v = b, u, v, a - q * b, s - q * u, t - q * v
    # return u0, v0, PGCD
    return (s, t, a) if a > 0 else (-s, -t, -a)

def est_premier(n) -> bool:
    """Test de primalité de n"""
    if n < 2:
        return False
    else:
        for i in [2] + [j for j in range(3, isqrt(n), 2)]:
            if n % i == 0:
                return False
    return True

def pgcd(a,b) -> int:
    """PGCD de a et b"""
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)

def ppcm(a,b) -> int:
    """ppcm de a et b"""
    (a*b)/pgcd(a, b)

def decomposition_puissance_2(a):
    resultat = []
    while a != 0:
        puissance = int(math.log2(a))
        resultat.insert(0, puissance)
        a -= 2 ** puissance
        if a != 0:
            puissance = int(math.log2(a))
    return resultat


def exponentiation_rapide(a, p, m):
    tempo = []
    indice = 0
    decomposition = decomposition_puissance_2(p)
    for i in range(decomposition[-1] + 1):
        # "decomposition" contient l'indice de la puissance, je regarde donc quand j'arrive au bon moment
        # pour récupérer mon "a" (a = a**2 % m => a = a**2 % m ...)
        if decomposition[indice] == i:
            tempo.append(a)
            indice += 1
        a = a ** 2 % m
    resultat = tempo[0]
    for i in range(len(tempo) - 1):
        resultat = resultat * tempo[i + 1] % m
    return resultat

def facteurs_premiers(a):
    if a < 2:
        return []
    else:
        resultat = []
        nombre_actuel = a
        for i in [2] + [j for j in range(3, a // 2 + 1, 2)]:
            while nombre_actuel % i == 0:
                resultat.append(i)
                nombre_actuel /= i
    if not resultat:
        resultat.append(a)
    return resultat


def diviseurs(a):
    resultat = []
    deuxieme_partie = []
    for i in range(1, isqrt(a) + 1):
        if a % i == 0:
            resultat.append(i)
            deuxieme_partie.insert(0, a // i)
    return resultat + deuxieme_partie


def diophantienne(a, b, c):
    u0, v0, pgcd_a_b = bezout(a, b)
    if c % pgcd_a_b != 0:
        print("Pas de solutions")
    else:
        coeff = c // pgcd_a_b
        print(f"Les solutions de l'équation {a}u" + [" + ", " - "][b < 0] + f"{abs(b)}v = {c} sont:")
        print(f"(u, v) = ({coeff * u0}" + [" + ", " - "][b < 0] + f"{abs(b) // pgcd_a_b}k , {coeff * v0}" +
              [" - ", " + "][a < 0] + f"{abs(a) // pgcd_a_b}k)")