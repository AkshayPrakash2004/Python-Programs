bid={}
y=""
finish=False
while not finish:
    name=input("enter your name")
    price=input("enter the bid price")
    bid[name]=price
    y=input("are there any more bidders?")
    if y == "no":
        finish=True
    

    
