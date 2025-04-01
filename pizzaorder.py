print("Choose the size of the pizza S,M or L")
size=str(input())
if size == 's' or size == 'S':
  price=100
elif size == 'm' or size == 'M':
  price=200
elif size == 'l' or size == 'L':
  price=300
else:
    print("invalid choice")
    exit()

print("do u want to add extra cheese")
c=str(input())
if c == 'y':
   if size == 's' or size == 'S':
    price=price+30
    print("total bill is",price)
   if size == 'm' or size == 'M':
    price=price+40
    print("total bill is",price)
   if size == 'l' or size == 'L':
    price=price+90
    print("total bill is",price)
else:
    print("total bill is",price)
    