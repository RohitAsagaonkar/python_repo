#type is a fuction that takes object(car ,123) and gives what class it belogs to ex str,int,float
print(type(10))
#isinstance it take object and check does it is class which has we asking
x=10
print("result of type  ",isinstance(x,int))
#hasasttr it check where the given object has the given method or not
print("result of haswattr  ",hasattr(x,'find'))
print("result of haswattr  ",hasattr(x,'bit_length'))