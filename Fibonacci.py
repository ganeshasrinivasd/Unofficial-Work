a = int(input("Till which term you want the Fibonacci series:"))
t1=0 
t2=1
counter = 0
if a <= 0:
   print("Hey Man,Enter a positive number")
elif a == 1:
   print(t1)
else:
   while counter < a:
       print(t1)
       nextTerm = t1 + t2
       t1 = t2
       t2 = nextTerm
       counter += 1