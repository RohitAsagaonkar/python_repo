amount=float(input("enter amount "))

if amount <=1000:
    print ("you discount is 10 %" ,amount-amount*0.10 )


elif amount >=1000 and amount<=5000:
    print("your discount is 15 percent  ", amount-amount*0.15)

elif amount >=5000 and amount<=10000 :
    print (" your discount is 20 percent ", amount-amount *0.20)

elif amount >=10000 :
    print (" your discount is 25 percent ", amount-amount *0.25)

     