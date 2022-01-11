#coding: utf-8
a = input()
b = input()
a = str(a)
b = str(b)
contador = 0
x = 0
while ( contador < len(b)):	
	if( a == b[contador]):
		x = x + 1
	contador = contador + 1
if( x == 0):
	print 0
else:
	print x 
