x = int(input())
i = 0
a = x/10
b = x%10
while( i == 0):
    a = str(a)
    b = str(b)
    print b+a
    i = i+1
c = b+a
if(c != x):
   print 0
elif( c == x):
   print 1    
    


	
