n = int(input('n='))
m = 0
for i in range(1,n+1) :
    if n % i == 0 :
        m += 1
    
if m == 2 :
    print(n,' là SNT')
else :
    print(n,' không là SNT')

    