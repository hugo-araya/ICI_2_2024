def inicializa():
    lista = [1,2,3,4,5,6,7,8,9]
    elemento = 15
    ini = 0
    fin = len(lista) - 1
    return ini, fin, lista, elemento

def calculo_pivote(ini, fin):
    return (ini + fin) // 2

def busqueda_binaria(lista, elemento, ini, fin):
    ok = False
    while ini <= fin and ok == False:
        pivote = calculo_pivote(ini, fin)
        if lista[pivote] == elemento:
            ok = True
        elif lista[pivote] < elemento:
            ini = pivote + 1
        else:
            fin = pivote - 1
    return ok

def salida(resultado):
    if resultado:
        return (f'El elemento {elemento} se encuentra en la lista')
    else:
        return (f'El elemento {elemento} no se encuentra en la lista')

if __name__ == '__main__':
    ini, fin, lista, elemento = inicializa()
    resultado = busqueda_binaria(lista, elemento, ini, fin)
    print (salida(resultado))
