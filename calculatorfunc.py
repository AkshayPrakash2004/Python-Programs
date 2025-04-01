def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
c=int(input("enter the first operand: "))
d=int(input("enter the second operand: "))
f=str(input("enter the operation: "))
if f == "+":
    answer= add(c,d)
    print(answer)
elif f =="-":
    answer=sub(c,d)
    print(answer)
elif f== "/":
    answer=div(c,d)
    print(answer)
elif f == "%":
    answer=rem(c,d)
    print(answer)
