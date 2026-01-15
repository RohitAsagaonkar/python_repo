"""outer fuction runs only one time dose not run two times hense i called f() three"""
def outer ():
    print("car")
    def inner():
        print("welcome")
        
    return inner # here inner fuction object (all code of it) is returned not inner fuction run and return
f=outer()  #here f is storing exicuted outer and outer was returning inner and now f has stored inner fuction object (code)
f() # f now becamed the inner because it has inner code then we can call directly inner like this means we are calomh the fuction
f()
f()