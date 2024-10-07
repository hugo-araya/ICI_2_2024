
def fib(n):
    global cont
    cont = cont + 1
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib_i(n):
    global cont
    cont = cont + 1
    i = 2
    pri = 0
    seg = 1
    while i <= n:
        ter = pri + seg
        pri = seg
        seg = ter
        i = i + 1
    return ter

if __name__=='__main__':
    cont = 0
    termino = int(input('Termino: '))
    valor = fib_i(termino)
    print('Iterativo: ', valor)
    print('Llamadas: ', cont)
    print('--------------------------')
    valor = fib(termino)
    print('Recursivo: ', valor)
    print('Llamadas: ', cont)
