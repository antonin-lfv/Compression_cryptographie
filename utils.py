import math


def eDiviseurs(a):
    """
    renvoie l'ensemble des diviseurs positifs de A
    >>> eDiviseurs(60)==[1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
    True
    >>> eDiviseurs(1)==list(set([1])) and eDiviseurs(13)==list(set([1, 13]))
    True
    """
    if a == 1:
        return [a]
    resultat = []
    deuxieme_partie = []
    for i in range(1, math.isqrt(a) + 1):
        if a % i == 0:
            resultat.append(i)
            deuxieme_partie.insert(0, a // i)
    return resultat + deuxieme_partie


def demoVitesse():
    for p in range(5, 20):
        for k in range(100):
            ld = eDiviseurs(10 ** p + k)
            if len(ld) <= 3 or len(ld) > 20:
                print(f"{p}:eDiviseurs(10**p+k)=={eDiviseurs(10 ** p + k)}")


def PGCD(a, b):
    """
    >>> PGCD(360,304)
    8
    >>> PGCD(517,513)==1 and PGCD(513,517)==1
    True
    """
    while b != 0:
        a, b = b, a % b
    return a


def bezout(a, b):
    """
    Renvoie (u,v,d) tel que a.u+b.v=d avec d=PGCD(a,b)
    >>> bezout(360,304)
    (11, -13, 8)
    >>> bezout(1254,493)
    (-149, 379, 1)
    >>> bezout(513,517)
    (129, -128, 1)
    """
    s, t, u, v = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, s, t, b, u, v = b, u, v, a - q * b, s - q * u, t - q * v
    # return u0, v0, PGCD
    return (s, t, a) if a > 0 else (-s, -t, -a)


def chFacteursPremiers(n):
    """renvoie une chaine de caractère donnant la décomposition en
    facteurs premiers de n
    >>> chFacteursPremiers(120)
    [2, 2, 2, 3, 5]
    >>> chFacteursPremiers(3600)
    [2, 2, 2, 2, 3, 3, 5, 5]
    >>> chFacteursPremiers(1)
    [1]
    >>> chFacteursPremiers(2)
    [2]
    >>> chFacteursPremiers(21)
    [3, 7]
    """
    if n == 1:
        return [1]
    elif n < 1:
        return []
    else:
        resultat = []
        nombre_actuel = n
        for i in [2] + [j for j in range(3, n // 2 + 1, 2)]:
            while nombre_actuel % i == 0:
                resultat.append(i)
                nombre_actuel /= i
    if not resultat:
        resultat.append(n)
    return resultat


def lDecompoPGCDetPPCM(a, b):
    """
    Renvoie le couple de listes de la décomposition en facteurs
    premiers du PGCD et du PPCM de a et b
    en utilisant la décomposition en facteurs premier de a et b
    >>> lDecompoPGCDetPPCM(60,700)
    [[2, 2, 5], [2, 2, 3, 5, 5, 7]]
    """
    resultat = []
    pgcd = PGCD(a, b)
    ppcm = a * b // pgcd
    resultat.append(chFacteursPremiers(pgcd))
    resultat.append(chFacteursPremiers(ppcm))
    return resultat


def occurence(elem, liste):
    occur = 0
    for i in liste:
        if i == elem:
            occur += 1
    return occur
# if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
