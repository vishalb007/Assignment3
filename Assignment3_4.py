def GetElements(num):
	lis=[]
	for i in range(num):
		print("Enter element : ",i+1)
		n=int(input())
		lis.append(n)
	return lis

def Search(lis,num,element):
	frequency=0
	for i in range(num):
		if(lis[i]==element):
			frequency=frequency+1
	return frequency

def main():
	num =int(input("Enter number of elements : "))
	lis=[]
	print("Enter the elements")
	lis=GetElements(num)
	print("Enter element to be searched : ")
	element=int(input())
	frequency=Search(lis,num,element)	
	print("Frequency is : ",frequency)

if (__name__=="__main__"):
	main()
