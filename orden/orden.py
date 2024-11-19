import time

def inicializa1():
    lista = [40, 21, 4, 9, 10, 35]
    return lista

def inicializa(nombre, cantidad):
    lista = []
    ent = open(nombre)
    i = 0
    while i < cantidad:
        lista.append(int(ent.readline().rstrip('\n')))
        i = i + 1
    ent.close()
    return lista

def intercambia(lista, menor, i):
    aux = lista[menor]
    lista[menor] = lista[i]
    lista[i] = aux

def ord_seleccion(lista):
    global contador
    for i in range(len(lista) - 1): 
        menor = i
        for j in range(i + 1, len(lista)):
            contador = contador + 1
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            intercambia(lista, menor, i)

def ord_burbuja(lista):
    global contador
    n = len(lista)
    for i in range(n-1): 
        for j in range(n-1-i): 
            contador = contador + 1
            if lista[j] > lista[j+1]:
                intercambia(lista, j, j+1)

def ord_insercion(lista):
    global contador
    for i in range(1, len (lista)) :
        elemento = lista[i]
        j = i - 1
        while j >= 0 and elemento < lista[j]:
            contador = contador + 1
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento

def ord_shell(lista):
    global contador
    n = len(lista)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j-gap] > temp:
                contador = contador + 1
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
    global contador
    contador = contador + 1
    if izquierda < derecha:
        indiceParticion = particion(lista, izquierda, derecha)
        ord_quick(lista, izquierda, indiceParticion)
        ord_quick(lista, indiceParticion + 1, derecha)

if __name__ == '__main__':
    archivo = 'may_men.txt'
    cantidad = 1000
    contador = 0
    lista = inicializa(archivo, cantidad)
    #print(lista)
    tiempo_inicial = time.time()
    ord_seleccion(lista)
    #ord_burbuja(lista)
    #ord_insercion(lista)
    #ord_shell(lista)
    #ord_quick(lista, 0, len(lista) - 1)
    #print(lista)
    tiempo_final = time.time()
    total = tiempo_final - tiempo_inicial
    print(contador, "--", total)

