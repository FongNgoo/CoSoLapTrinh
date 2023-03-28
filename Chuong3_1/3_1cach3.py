a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if(a >= b and a >= c) :
    max = a 
elif(b >= a and b >= c ) :
    max = b
elif(c >= a and c >= b ) :
    max = c
    
if(a <= b and a <= c) :
    min = a 
elif( b <= a and b <= c ) :
    min = b
elif(c <= a and c <= b ) :
    min = c
    
print('SLN=' + str(max))
print('SNN=' + str(min))