def funcion(var1):
    var1 = var1 + [1]
    return var1

if __name__ == '__main__':
    var1 = [2]
    print(var1)
    var1 = funcion(var1)
    print(var1)
