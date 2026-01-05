s1=input("enter word or phrase  ")
s2=input ("anather word or phrase  ")

s1=s1.casefold()
s2=s2.casefold ()

for x in s1:
    if x.isalpha():
        if s1.count(x)!=s2.count(x):
            print("not anagaram ")
            break

else:
        print ("its anagram")
   
     






