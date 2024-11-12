def inicializa():
    lista = [1,2,3,4,5,6,7,8,9]
    ini = 0
    fin = len(lista) - 1
    elemento = 5
    return ini, fin, lista, elemento

def calcula_pivote(ini, fin):
    return (ini + fin) // 2

def binaria(ini, fin, lista, elemento):
    ok = False
    pivote = calcula_pivote(ini, fin)
    while ini <= fin and lista[pivote] != elemento:
        pivote = calcula_pivote(ini, fin)
        if lista[pivote] == elemento:
            ok = True
        elif elemento < lista[pivote]:
            fin = pivote - 1
        else:
            ini = pivote + 1
    return ok

if __name__ == '__main__':
    ini, fin, lista, elemento = inicializa()
    resultado = binaria(ini, fin, lista, elemento)
    if resultado == True:
        print('Elemento esta en la lista')
    else:
        print ('Elemento no existe en la lista')

