def fatorial(x):
  fatorial = 1
  while (x > 0):
    fatorial = fatorial * x
    x -= 1
  return fatorial

def combinacao(x,y):
   comb = fatorial(x) / (fatorial(y) * fatorial(x-y))
   return comb

def main():
    m = int(input())
    n = int(input())
    print combinacao(m,n)
    
main()
