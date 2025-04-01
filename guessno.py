from random import randint
print("i have a number between 1-100 try and guess it!!")
a=randint(1,100)
print(a)
b=input("easy or hard")
n=6
n1=11
if b == "easy":
    while n1!=0:
        n1=n1-1
        print(" chances left")
        print(n1)
        d=int(input("enter the number"))
        if d<a:
                print("higher")
                if d>a:
                    print("lower")
                if d == a:
                    print("you win!!")
                break
        
        
elif b == "hard":
     while n!=0:
            if n == 0:
                print("your lose") 
                break
            else:
                n=n-1
                print(" chances left")
                print(n)
                d=int(input("enter the number"))
                if d<a:
                    print("higher")
                if d>a:
                    print("lower")
                if d == a:
                    print("you win!!")
                break