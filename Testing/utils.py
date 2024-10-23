import math

def es_primo(n):
    if n < 0:
        return 'Los números negativos no están permitidos'
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True

def cubico(a):
    return a * a * a

def decir_hola(nombre):
    return "Hola, "+nombre