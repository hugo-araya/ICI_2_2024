def lee_numero():
    numero = '12345'
    return numero

def da_vuelta(numero):
    cadena = []
    for elem in numero:
        cadena = [elem] + cadena
    return cadena

def may_men(nume_or):
    numero = []
    for digito in nume_or:
        numero.append(digito)
    numero.sort(reverse = True)
    nume_may_men = numero[0]+ numero[1]+ numero[2]+ numero[3]+ numero[4]
    return nume_may_men

def men_may(nume_or):
    numero = list(nume_or)
    numero.sort()
    nume_men_may = numero[0]+ numero[1]+ numero[2]+ numero[3]+ numero[4]
    return nume_men_may

def diferencia (nume_1, nume_2):
    dife = int(nume_1) - int(nume_2)
    dife = str(dife)
    while len(dife) < 5:
        dife = '0' + dife
    return dife

def ciclo_kaprekar(nume_or):
    ciclo = []
    anterior = ''
    nume_calculado = nume_or
    while anterior != nume_calculado:
        ciclo.append(nume_calculado)
        nume_1 = may_men(nume_calculado)
        nume_2 = men_may(nume_calculado)
        nume_1_2 = diferencia(nume_1, nume_2)
        anterior = nume_calculado
        nume_calculado = nume_1_2
    return nume_calculado, ciclo

def mostrar_constante(constante, ciclo):
    print(constante,'-', ciclo)

if __name__ == '__main__':
    nume_or = lee_numero()
    constante, ciclo = ciclo_kaprekar(nume_or)
    mostrar_constante(constante, ciclo)

