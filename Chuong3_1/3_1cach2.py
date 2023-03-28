def nhap() :
	a = float(input("Hãy nhập số a ="))
	b = float(input("Hãy nhập số b ="))
	c = float(input("Hãy nhập số c ="))
	maxnumber = max(a,b,c)
	inkq(maxnumber)

def max(y,x,z) :
	if y - x >= 0 :
		if y - z >= 0 :
			return y
		else :
			return z 
	else :
		if x - z >= 0 :
			return x 
		else :
			return z 

def inkq(n) :
	print("số lớn nhất là " + str(n))

nhap()