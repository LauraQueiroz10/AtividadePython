x = raw_input()
soma = 0 
for i in range(len(x)):
  soma = soma + ord(x[i])
print soma%50
