def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Sum(lis,num):
	sum=0
	for i in range(num):
		sum=sum+lis[i]
	return sum

def main():
	num =int(input("Enter number of elements : "))
	lis=[]
	print("Enter the elements")
	lis=GetElements(num)
	sum=Sum(lis,num)	
	print("Sum is : ",sum)

if (__name__=="__main__"):
	main()
