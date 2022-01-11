def bonificacao(x):
	vendas = 0 
	if(x <= 10.000):
	  vendas = vendas + ((x*1)/100)
	return vendas
	if( x > 10.000):
	  vendas = vendas + ((x*5)/100)
	return vendas

def bonificacao(y):
	vendas = 0 
	if(x <= 10.000):
	  vendas = vendas + ((x*1)/100)
	return vendas
	if( x > 10.000):
	  vendas = vendas + ((x*5)/100)
	return vendas

def bonificacao(z):
	vendas = 0 
	if(x <= 10.000):
	  vendas = vendas + ((x*1)/100)
	return vendas
	if( x > 10.000):
	  vendas = vendas + ((x*5)/100)
	return vendas

def soma (x,y,z):
	somaSal = (954 + bonificacao(x)) + (954 + (bonificacao(y)) + (954 + (bonificacao(z)) 
	return somaSal

def main():
      a = input() 
      b = input()
      c = input()
      print soma(a,b,c)
main()
