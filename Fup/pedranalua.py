jogador = input()
pedraa = 0
pedrab = 0
cont = 0
ganhador = 0
while (cont < jogador):
  pedraa = input()
  pedrab = input()
  if (pedraa < 10) or (pedrab < 10):
    ganhador += 0 
  if (pedraa >= 10) and (pedrab >= 10):
    ganhador = cont
  cont += 1
if (ganhador == 0):
    print "sem ganhador"
elif (ganhador != 0):
    print ganhador
            
