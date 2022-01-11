x = int(input("Digite o tamanho do vetor: "))
numeros = []
i = 0
while ( i < x):
    z = input()
    numeros += [z]
    i += 1 


inversos = []
tamanho = len(numeros)
while( tamanho > 0 ):
     inversos += [numeros[tamanho-1]]
     tamanho = tamanho-1
     
print inversos







