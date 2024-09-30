import sys

def facto_i(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

def facto_r(n):
    if n == 0:
        return 1
    else:
        return n * facto_r(n-1)

if __name__ == '__main__':
    print(sys.getrecursionlimit())
    n = int(input('N: '))
    sys.setrecursionlimit(1100)
    factorial = facto_r(n)
    print(factorial)
    print(sys.getrecursionlimit())