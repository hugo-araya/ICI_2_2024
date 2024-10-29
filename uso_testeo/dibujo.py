def evalua(movi):
    if len(movi) >= 1 and len(movi)<= 5:
        return True
    else:
        return False

def mod_limites(movi, fi, ff, ci, cf):
    df = (ff - fi + 1)//2
    dc = (cf - ci + 1)//2
    if movi == '1':
        ff = ff - df
        cf = cf - df
    elif movi == '2':
        ff = ff - df
        ci = ci + dc
    elif movi == '3':
        fi = fi + df
        ci = ci + dc
    else:
        fi = fi + df
        cf = cf - dc
    return [fi, ff, ci, cf]

if __name__ == '__main__':
    movimientos = lee_archivo('dibu1.dat')
    salida = proceso(movimientos)
    genera_archivo('dibu1.out')
