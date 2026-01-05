def maxOf3(a,b,c):
    if (a>b and a>c):
        return a

    elif(a<b and b>c):
    
        return b
    elif(a<c and c>b):
        return c
    

print(maxOf3(1,43,44))
