kw = int(input('Tieu thu='))

if kw >= 1 and kw <= 100 :
    price = 550
elif kw >= 101 and kw <= 150 :
    price = 750 
elif kw >= 151 and kw <= 200 :
    price = 950
else :
    price = 1350

vat = kw*price*0.1
print('Phai tra=', kw*price + vat)