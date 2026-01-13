s1=input("enter string  ")
s2=s1.replace(" ",  "") #replacing spacess wiuth empty spacess
rev=s2[ :  :  -1]

if s2.casefold()==rev.casefold():
    print(s1 , "its palidrome str already")

else:
    palidrome=s2.casefold()+rev.casefold()
    print(palidrome)

