#coding: utf-8
x = input()
aux = 0
aux2 = x 
while ( aux2 != 0):
	aux *= 10
	aux += aux % 10
	aux2 /= 10
if ( x == aux):
	print 1
else: 
	 print 0
