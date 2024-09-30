import matplotlib.pyplot as plt
x1 = []
y1 = []
x2 = []
y2 = []
ent1 = open('log1.txt')
ent2 = open('log.txt')
for linea in ent1:
    lista = linea.rstrip('\n').split(';')
    x1.append(int(lista[0]))
    y1.append(float(lista[1]))
ent1.close()

for linea in ent2:
    lista = linea.rstrip('\n').split(';')
    x2.append(int(lista[0]))
    y2.append(float(lista[1]))
ent2.close()

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()

