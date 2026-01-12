l1=[1,17,7,-3,8]
print("this is up sequence sort",sorted(l1))
print("this is reverse sort",sorted(l1,reverse=True))
print("this is abs  ",sorted(l1,key=abs)) # abs trearts averything as positive


#recersed using
rev=reversed(l1)
print("this is reverse order",list(rev)) #here itrable is converted in to tyhe lisat 
#slice build tm function
list=[1,2,3,4,5,6,7,8,9]
s=slice(5) #only given where to stop start and step by defalt
print("this is sclice built in class",list[s])