url=input("enter url")
protocol=url[ :url.find(":")]
print("protocol is",protocol)

dot1=url.find(".")
dot2=url.find(".",dot1+1)
domain= url[dot1+1:dot2]
print("domain'",domain)
page=url[url.find("/" , dot2) :   ]
print("page=>",page)