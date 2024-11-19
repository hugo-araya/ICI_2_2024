def inicializa():
    lista1 = [3, 5, 6, 9]
    lista2 = [1, 2, 4, 10, 34]
    return lista1, lista2

def fusion(l1, l2):
    largo1 = len(l1)
    largo2 = len(l2)
    i1 = 0
    i2 = 0
    l3 = []
    while i1 < largo1:
        if l1[i1] < l2[i2]:
            l3.append(l1[i1])
            i1 = i1 + 1
            if i1 >= largo1:
                while i2 < largo2:
                    l3.append(l2[i2])
                    i2 = i2 + 1
        else:
            l3.append(l2[i2])
            i2 = i2 + 1
            if i2 >= largo2:
                while i1 < largo1:
                    l3.append(l1[i1])
                    i1 = i1 + 1
    return l3

if __name__ == '__main__':
    l1, l2 = inicializa()
    l3 = fusion(l1, l2)
    print(l3)
