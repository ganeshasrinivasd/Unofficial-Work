a=int(input("Enter the number of elements you want in the list: "))
List=[]
i=1
while(i<=a):
	b=int(input())
	List.append(b)
	i+=1
print('your list is\n ',List)
for y in range(0,a):
	if List[y]>0:
		print(List[y])
