def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Min(lis,num):
	min=lis[0]
	for i in range(num):
		if(lis[i]<min):
			min=lis[i]
	return min

def main():
	num =int(input("Enter number of elements : "))
	lis=[]
	print("Enter the elements")
	lis=GetElements(num)
	min=Min(lis,num)	
	print("Min is : ",min)

if (__name__=="__main__"):
	main()
