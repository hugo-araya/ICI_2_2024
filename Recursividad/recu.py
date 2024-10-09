
def recur(n,p,acumulado):
  while n>0 :
    acumulado+=n*p
    n-=1
    recur(n,p,acumulado)
  return acumulado

p=int(input('Ingrese un numero: '))
n=int(input('Ingrese otro numero: '))
print(recur(n,p,0))