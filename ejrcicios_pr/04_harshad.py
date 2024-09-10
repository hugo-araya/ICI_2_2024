def suma_digitos(numero):
    suma = 0
    nume = list(str(numero))
    for digito in nume:
        suma = suma + int(digito)
    return suma

def busca_numeros(inicio, fin):
    lista = []
    for nume in range(inicio, fin):
        suma_dig = suma_digitos(nume)
        if (nume % suma_dig) == 0:
            lista.append(nume)
    return lista 

def mostrar_numeros(lista_numeros):
    print(lista_numeros, '-', len(lista_numeros))

if __name__ == '__main__':
    lista_numeros = busca_numeros(10, 15)
    mostrar_numeros(lista_numeros)