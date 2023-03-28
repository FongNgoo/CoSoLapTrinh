niemyet = float(input('nhap gia niem yet: '))
chietkhau = float(input('nhap gia chiet khau: '))
vat = (niemyet - chietkhau) * 0.01
print('Gia ban: ', niemyet - chietkhau + vat)