n=int(input("enetr roation number"))

#l1=[1,2,3,4,5,6,7]
#l2=l1[n-1::]
#l3=l1[0:n-1:]
#print(l2+l3)
# it can be wriiten as 

l1=[1,2,3,4,5,6,7]
ratated=l1[n::]+l1[:n:]
print ("rotataed lis is :",ratated)