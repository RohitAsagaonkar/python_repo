n=5 
i=0

max=float('-inf')
min=float('inf')
x=0

while n>i:
    i=i+1
    x=int(input("enter numbers "))
    if x>max:
        max=x
    if x<min:
        min=x

print("max   number is :",max)
print("min  number is :",min)