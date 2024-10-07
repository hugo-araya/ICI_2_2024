def A(m, n):
    if m == 0 and n != 0:
        return n + 1
    elif m !=0 and n == 0:
        return A(m-1, n)
    else:
        return A(m-1, A(m, n-1))


if __name__ == '__main__':
    m = 0
    n = 0
    resultado = A(m, n)
    print(resultado)
