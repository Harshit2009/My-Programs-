def MultiplicativeInverse(a, m) : 
	a = a % m; 
	for x in range(1, m) : 
		if ((a * x) % m == 1) : 
			return x 
	return 1


a = 132
m = 180
print(MultiplicativeInverse(a, m)) 

