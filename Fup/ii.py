#coding: utf-8
num = input()
div = 0
i = 1
while (i <= num):
        if (num % i == 0):
            div = div + 1
        i = i + 1
if (div == 2):
        print "Número primo"
else:
        print "Número não primo"

