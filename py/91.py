l1=[1,2,3,4,54,6,7,8,9]

result=[]

for element in l1 :
    if element %2==0:
        result.append(element)

    else:
        result.insert(0,element)
print(result)




