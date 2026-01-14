#fuction inside the fuction it is called nested fuction

def calculate_bill(amount):
    def add_tax():
        return amount*0.18
    tax=add_tax() # here add_tax fuction is called and value is stred in tax variable
    total=amount+tax
    print("total bill amount",total)
    print("gst",tax)
    print("without gst",amount)
    
calculate_bill(1000)