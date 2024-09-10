# Autor: Hugo Araya Carrasco
# Fecha: 06/08/2024
# Version: 0.1

import matplotlib.pyplot as plt

def collatz(numero):
    lista_col = []
    lista_col.append(numero)
    while numero != 1:
        if numero%2 == 0:
            numero = numero // 2
        else:
            numero = numero * 3 + 1
        lista_col.append(numero)
    return lista_col

def es_primo(numero):
    inicio = 2
    fin = numero//2
    es_primo = True
    while inicio <= fin:
        if numero%inicio == 0:
            es_primo = False
        inicio = inicio + 1
    return es_primo

def primos(lista_col):
    lista_primo = []
    for nume in lista_col:
        if es_primo(nume) == True:
            lista_primo.append(nume)
    return lista_primo

def primos1(lista_col):
    lista_primo = []
    largo = len(lista_col)
    i = 1
    while i < largo-1:
        if es_primo(lista_col[i]) == True:
            lista_primo.append(lista_col[i])
        i = i + 1
    return lista_primo




def grafica(lista_col, lista_primo):
    total = len(lista_col)
    primo = len(lista_primo)
    todos = "Total ("+str(total)+")"
    solos = "Primos ("+str(primo)+")"
    valores = [primo, total]
    etiquetas = [solos, todos]
    separacion = [0.2, 0]
    colores = ['Blue', 'Green']
    plt.pie(valores, labels = etiquetas, explode = separacion, shadow = True, colors = colores)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    numero = int(input('Numero: '))
    lista_col = collatz(numero)
    primo = es_primo(numero)
    lista_primo = primos(lista_col)
    grafica(lista_col, lista_primo)


