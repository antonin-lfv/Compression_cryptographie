def all_info_(n: (int, 'Value of n')):
    ZnZ = Z_sur_nZ(n)

    print("\nTable addition : ")
    ZnZ.afficher_table_add()

    print("\nTable multiplication : ")
    ZnZ.afficher_table_mult()

    print("\nPhi(" + str(ZnZ.n) + ") = " + str(ZnZ.indicatrice))
    print("\nElements inversibles : ")
    ZnZ.afficher_inverses()

    print("\n7*12 = " + str(ZnZ.multiplication(7, 12)))
    print("\n18+190 = " + str(ZnZ.somme(18, 190)))

if __name__ == '__main__':
    from ZsurNZ import Z_sur_nZ
    from Arithmetique import *
    all_info_(10)