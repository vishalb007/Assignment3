from MarvellousNum import *

def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Sum(ListPrime):
	sum=0
	for i in range(len(ListPrime)):
		sum=sum+ListPrime[i]
	return sum

def main():
	num =int(input("Enter number of elements : "))
	lis=[]
	ListPrime=[]
	print("Enter the elements")
	lis=GetElements(num)
	for i in range(num):
		IsPrime=ChkPrime(lis[i])
		if IsPrime == 0:
			ListPrime.append(lis[i])			
	sum=Sum(ListPrime)	
	print("Sum is : ",sum)

if (__name__=="__main__"):
	main()
