def numNaturales(n,m):
	if(n<=m):
		print(n)
		numNaturales(n+1,m)
		
numNaturales(5,14)
