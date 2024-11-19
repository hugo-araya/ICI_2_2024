import time

def inicializa1():
    lista = [40, 21, 4, 9, 10, 35]
    return lista

def inicializa(nombre):
    lista = []
    ent = open(nombre)
    for elemento in ent:
        lista.append(int(elemento))
    ent.close()
    return lista

def intercambia(lista, menor, i):
    aux = lista[menor]
    lista[menor] = lista[i]
    lista[i] = aux

def ord_seleccion(lista):
    for i in range(len(lista) - 1): 
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            intercambia(lista, menor, i)

def ord_burbuja(lista):
    n = len(lista)
    for i in range(n-1): 
        for j in range(n-1-i): 
            if lista[j] > lista[j+1]:
                intercambia(lista, j, j+1)

def ord_insercion(lista):
    for i in range(1, len (lista)) :
        elemento = lista[i]
        j = i - 1
        while j >= 0 and elemento < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento

def ord_shell(lista):
    n = len(lista)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j-gap] > temp:
                lista[j] = lista[j-gap]
                j -= gap
            lista[j] = temp
        gap //= 2


def particion(lista, izquierda, derecha):
    pivote = lista[izquierda]
    while True:
        while lista[izquierda] < pivote:
            izquierda += 1
        while lista[derecha] > pivote:
            derecha -= 1
        if izquierda >= derecha:
            return derecha
        else:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            izquierda += 1
            derecha -= 1

def ord_quick(lista, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(lista, izquierda, derecha)
        ord_quick(lista, izquierda, indiceParticion)
        ord_quick(lista, indiceParticion + 1, derecha)

if __name__ == '__main__':
    archivo = 'aleatorio.txt'
    lista = inicializa(archivo)
    #print(lista)
    tiempo_inicial = time.time()
    ord_seleccion(lista)
    #ord_burbuja(lista)
    #ord_insercion(lista)
    #ord_shell(lista)
    #ord_quick(lista, 0, len(lista) - 1)
    tiempo_final = time.time()
    print('Tiempo:', tiempo_final - tiempo_inicial)
    #print(lista)
