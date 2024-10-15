def lee_datos(nombre):
    ent = open(nombre)
    numero = int(ent.readline().rstrip())
    ent.close()
    return numero

def genera_lista(numero):
    lista = []
    i = 1
    while i < numero:
        j = 2
        while j <= numero:

            dato =[i, j]
            lista.append(dato)
            j = j + 1
        i = i + 1
    return lista

def genera_salida(nombre, lista):
    sal = open(nombre, 'w')
    for dato in lista:
        nume = dato[0]
        deno = dato[1]
        sal.write(str(nume)+' '+str(deno)+'\n')
    sal.close()

if __name__ == '__main__':
    numero = lee_datos('FRAC.DAT')
    lista = genera_lista(numero)
    genera_salida('FRAC.OUT', lista)