def affiche_permutations(table, fin=''):
    """
    >>> permutations("abc")
    abc
    acb
    bac
    bca
    cab
    cba
    """
    if len(table) == 0:
        print(fin)
    else:
        for i in range(len(table)):
            affiche_permutations(table[:i] + table[i + 1:], fin + table[i])
        print(f"\nTotal = {arithmetique.factoriel(len(table))}")




