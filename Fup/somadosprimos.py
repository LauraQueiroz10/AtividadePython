def ehPrimo(n):
    cont = 1
    primo = 0 
    while (cont <= n):
        primo +=1
    cont +=1
    if (primo==2):
        return 1
    else:
        return 0
    
def somaPrimos(n):
  i = 2
  soma = 0
  while(i <= n):
      if(ehPrimo(i)==1):
          soma = soma + i
          return soma 
      i += 1      
def main():
     x = input() 
     print somaPrimos(x)

main()



