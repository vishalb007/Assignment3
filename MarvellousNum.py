def ChkPrime(num):
	for i in range(2,num):
		if(num%i==0):
			return 1
			break
		else:
			return 0
			break	