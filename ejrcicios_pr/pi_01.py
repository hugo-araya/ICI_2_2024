
import math

def pi_4(fin):
    n = 0
    suma = 0
    while n < fin:
        suma = suma + (-1)**n / (2*n + 1)
        n = n + 1
    return suma

def pi_2(fin):
    n = 1
    prod = 1
    while n < fin:
        prod = prod * (2*n/(2*n-1))*(2*n/(2*n+1))
        n = n + 1
    return prod

def calcula_pi(valor, numero):
    return valor * numero


if __name__ == '__main__':
    fin = 100000000
    p_4 = pi_4(fin)
    pipi = calcula_pi(p_4, 4)
    print(pipi)
    p_2 = pi_2(fin)
    pipi = calcula_pi(p_2, 2)
    print(pipi)
    print(math.pi)
