# coding: utf-8
n1 = input()
n2 = input()
n3 = input ()
tb = input ()
if (n1 < n2) and (n1 < n3):
    m = (n2+n3+tb)/3
elif (n2 < n1) and (n2 < n3):
    m = (n1+n3+tb)/3
elif (n3 < n1) and (n3 < n2):
    m = (n1+n2+tb)/3
elif (n1 == n2) or ( n1 == n3):
    m = (n2+n3+tb)/3
elif ( n2 == n3):
    m = (n1+n3+tb)/3
elif (n1 == n2) and (n1 == n3):
    m = (n2+n3+tb)/3 
if ( m >= 7):
    print "Aprovado(a) com" , m
elif ( m >= 4) and (m < 7):
    print "Final com" , m
elif( m < 4):
    print "Reprovado(a) com" , m 


