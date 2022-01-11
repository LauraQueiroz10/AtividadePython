x = int(input())
numeros = []
i = 0
while ( i < x):
    z = input()
    numeros += [z]
    i += 1

pares = []
impares = []
i = 0
while(i < x):
   if(numeros[i] % 2 == 0):
      pares = pares + [numeros[i]]
   elif( numeros[i] % 2 == 1):
     impares = impares + [numeros[i]]
   i = i + 1
print numeros
print pares
print impares
   
