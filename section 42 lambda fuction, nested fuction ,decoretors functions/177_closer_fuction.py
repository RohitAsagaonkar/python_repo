"""the closer name is come from the mathenmatics in 1990 at that time pythone is not created 
so when pythone add this name to the consept it barrove this name from mathematichs

#what does it measn:
a thing which captures everything it need and closed itself 

# here the fuction keeps the outer fuction veriable ehichg are need for it to exicute and closed itself

"""
def outer ():
    msg="welcome"
    def inner():
        print(msg)
        
    return inner
f=outer()
f()