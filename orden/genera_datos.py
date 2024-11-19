import random

def menor_mayor(N):
    sal = open('men_may.txt', 'w')
    for i in range(N):
        sal.write(str(i+1)+'\n')
    sal.close()

def mayor_menor(N):
    sal = open('may_men.txt', 'w')
    for i in range(N):
        sal.write(str(N - i)+'\n')
    sal.close()

def aleatorio(N):
    sal = open('aleatorio.txt', 'w')
    for i in range(N):
        sal.write(str(random.randint(1, N))+'\n')
    sal.close()

if __name__ == '__main__':
    N = 1000000
    menor_mayor(N)
    mayor_menor(N)
    aleatorio(N)
