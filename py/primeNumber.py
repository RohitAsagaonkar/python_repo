sum=0
for n in range(1,101):
        count=0
        for i in range(1,n+1):

            if n%i==0:
             count=count+1 
        if count==2:
           sum=sum+1
           
           print(n)

print("total prime numbers is",sum)                       