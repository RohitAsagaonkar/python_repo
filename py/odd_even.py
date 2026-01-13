num=[ ]
while(len(num) <8):

  num.append(int (input (f"Enter {len(num)+1}Number  :")))

even=[x for x in num if x % 2 ==0]
odd=[x for x in num if x % 2!=0]
print (even,"this is even numbers ")
print(odd,"this is odd numbers") 


