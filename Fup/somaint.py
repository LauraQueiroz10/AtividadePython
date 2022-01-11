x = raw_input()
soma = 0
for i in range(len(x)):
   if(ord(x[i]) >= ord('0') and ord(x[i]) <= ord('9')):
      soma = soma + int(x[i])
print soma
