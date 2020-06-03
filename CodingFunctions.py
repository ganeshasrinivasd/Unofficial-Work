def list():
    list1=[]
    list2=[]

    while True:
        a=input("enter l1 to add element in l1,l2 to add in l2,press any other key to exit")
        if a=='l1':
           inp=(input("enter number:"))
           list1.append(int(inp))
        elif a=='l2':
           inp=(input("enter number:"))
           list2.append(int(inp))
        else:
           break
    print(list1)
    print(list2)
#if u want to assign elements to list remove hastag from in next line
#list()
def tup():
    tple=('ganesha','srinivas','damaraju',29,2002,'june')
    a=input('for accessing tuple,enter which index postion you want\n #note index starts at 0\nif you want to quit press quit')
    while True:
        if a=='quit':
            break
        else:
            print(tple[int(a)])
            break
#if u want to access elements in tuple remove hastag from in next line
#tup()
def dictionary():
    D1={1:"bad",3:"good",2:"99"}
    print("THERE ARE 3 ELEMENTS IN THE DICTIONARY")
    print(D1)
    while True:
        inp=input("ENTER THE number  which you want to delete \n  ,FOR ENDING THIS PROCESS ENTER QUIT: ")
        if inp=='QUIT':
            break
        else:
            del D1[int(inp)]  
            print(D1)
#if u want to delete the word in the dictionary remove # in next line
#dictionary()
            
        

    

		
		

