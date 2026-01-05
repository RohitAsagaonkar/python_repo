l1=[1,2,3,4,5,6,7,8,9]

#rev= list(reversed(l1))
rev=l1[ : :-1]
print ( rev)
if l1==rev:
     print("its palidrome list")
else:
     print("its not palidrome list")