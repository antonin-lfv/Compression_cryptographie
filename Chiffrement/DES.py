"""Algorithme DES"""
import binascii
from DES_matrix import *
from operator import xor

message = '0110100101011011001001101010100001011110100011010111100101011011'


def cle_hexa_to_bin(cle_hex='133457799BBCDFF1') -> str:
    """
    >>> cle_hexa_to_bin(cle_hex='133457799BBCDFF1')
    '0001001100110100010101110111100110011011101111001101111111110001'
    """
    int_value = int(cle_hex, base=16)
    binary_value = str(bin(int_value))[2:].zfill(64)
    return binary_value


def apply_permutation_init_final(message, mode='init') -> list:
    """On fait permutation au début et à la fin avec PI et PIinverse"""
    PI, PIinverse = sum(DES()['PI'], []), sum(DES()['PIinverse'], [])  # flatten
    resultat = []
    if mode == 'init':
        for i in PI:
            resultat += [message[i-1]]
    else:
        for i in PIinverse:
            resultat += [message[i-1]]
    return resultat


def fonction_developpement(R='01101001010110110010011010101000') -> list:
    """Developpe le message R pour passer de 32 à 48 bits"""
    res = []
    E = sum(DES()['E'], [])
    for i in E:
        res += [R[i-1]]
    return res


def xor_on_2_lists(l1, l2) -> list:
    """Effectue le calcul XOR sur 2 listes de bits, bit à bit"""
    res = []
    for i, j in zip(l1, l2):
        res += [xor(i, j)]
    return res


def fonction_f_DES(R, K):
    """Fonction f du DES"""
    # calcul de E(R) pour avoir 48 bits
    R = fonction_developpement(R)
    B = xor_on_2_lists(R, K)
    pass















