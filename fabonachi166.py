def fabo(num):
    a,b=0,1 
    for i in range(num+1):
        yield a
        a,b=b,a+b
        
number=int(input("enter numbe which you want fabonachi  :"))
    
for term in fabo(number):
    print(term)
    
    