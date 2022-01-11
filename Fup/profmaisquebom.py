def maior(a, b, c):
    maior = a
    if (b > maior and b > c):
        maior = b
        return maior
    elif(c > maior and c > a):
        maior = c
        return maior
    else:
        return a
def mSimples(ap1,ap2,ap3):
    return (ap1+ap2+ap3)/3.0
    
def mPond1 (ap1,ap2,ap3):
    return (ap1+2+ap2+3+ap3)/6.0
    
def mPond2 (ap1,ap2,ap3):
    return (3+ap1+2+ap2+ap3)/6.0
def main():
    ap1 = input()
    ap2 = input()
    ap3 = input()
    Simples = mSimples(ap1,ap2,ap3)
    mPonderada1 = mPond1(ap1,ap2,ap3)
    mPonderada2 = mPond2(ap1,ap2,ap3)
    print maior(Simples,mPonderada1,mPonderada2)
main()
