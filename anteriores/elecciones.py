def lee_datos(nombre):
    ent = open(nombre)
    coaliciones = []
    linea1 = ent.readline().rstrip('\n')
    linea2 = ent.readline().rstrip('\n')
    paso1 = linea1.split(';')
    for elem in paso1:
        paso2 = elem.split(':')
        paso3 = paso2[1].split('-')
        coaliciones.append([paso2[0],paso3])
    votos = linea2.split('$')
    return coaliciones, votos

if __name__ == '__main__':
    coaliciones, votos = lee_datos('elecciones.txt')
    print(coaliciones)
    print(votos)