def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Max(lis,num):
	max=lis[0]
	for i in range(num):
		if(lis[i]>max):
			max=lis[i]
	return max

def main():
	num =int(input("Enter number of elements : "))
	lis=[]
	print("Enter the elements")
	lis=GetElements(num)
	max=Max(lis,num)	
	print("Max is : ",max)

if (__name__=="__main__"):
	main()
