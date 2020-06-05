def ExtendedAlgorithm(a, b, x, y): 
	
	if a == 0 : 
		x = 0
		y = 1
		return b 
		
	x1 = 1
	y1 = 1 
	gcd = ExtendedAlgorithm(b%a, a, x1, y1) 

	x = y1 - (b/a) * x1 
	y = x1 

	return gcd 


x = 1
y = 1
a = 35
b = 15
g = ExtendedAlgorithm(a, b, x, y) 
print("gcd(", a , "," , b, ") = ", g) 


