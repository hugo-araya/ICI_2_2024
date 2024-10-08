
def recursion(n,p,exp=1):
    if  n == 0:
        k = p - p
    else:
        k = (p * exp) +  recursion(n-1,p,exp + 1)
    return k

if __name__ == '__main__':
    p=int(input('Ingrese un factor:  '))
    n=int(input('Ingrese número:  '))
    print(recursion(p,n))