def check(sentence): 
   
    sentence=sentence.lower()
    
    present=[]  
    
    missing=[]
    

    l1=[ "abcdefghijklmnopqrstuvwxyz"]
    for i in  (sentence):
        
          if i in l1:
           present.append(i)

          else:
             
             missing.append(i)
    print(present,missing)
 
 
print(check("hello bro"))
    
  



        

    
    


