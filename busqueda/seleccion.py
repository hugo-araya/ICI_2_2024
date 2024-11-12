def inicializar():
    lista = [40, 21, 4, 9, 10, 35]
    return lista

def swap(lista, i,j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def seleccion(lista):
    i = 0
    while i < len(lista):
        minimo = i
        j = i + 1
        while j < len(lista):
            if lista[j] < lista[minimo]:
                minimo = j
            j = j + 1
        swap(lista, i, minimo)
        i = i + 1

if __name__ == '__main__':
    lista = inicializar()
    print(lista)
    seleccion(lista)
    print(lista)