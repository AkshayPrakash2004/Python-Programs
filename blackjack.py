import random
print("welcome to a game of blackjack")
choice=input("type y if u wanna play else n")
c=[10,2,3,4,5,6,7,8,9,10,10,10,11]
a=[0,]
b=[0,]
pos=c.index(random.randint(2,11))
pos1=c.index(random.randint(2,11))
pos2=c.index(random.randint(2,11))
pos3=c.index(random.randint(2,11))
a.append(pos)
a.append(pos1)
b.append(pos2)
b.append(pos3)
print("your cards are")
print(a[1:3])
r=0
ans=0
ans1=0
choice1=input("do u want to draw more")
print("dealer's cards are")
print(b[1:3])
if choice1 == "y":
    pos3=c.index(random.randint(2,11))
    a.append(pos3)
    for r in range(0,len(a)):
        ans=a[r]+ans
    print("your cards are")
    print(a[1:4])
    print("results")
    for r in range(0,len(b)):
        ans1=b[r]+ans1      
    if ans1 <= 17:
        print("dealer draws")
        pos4=c.index(random.randint(2,11))
        b.append(pos4)
        ans1=ans1+b[len(b)-1]
        print(b[1:4])
if (a[0] == 11 or a[1] == 11 or a[2] == 11 or a[3]== 11) and ans>21:
    ans=ans-10
if ans>ans1 and ans<=21:
    print("you win")
elif ans1> ans and ans1<=21:
    print("dealer wins")
    print(ans1)
elif ans1 == ans or ans1>=21 and ans>=21:
    print("draw")






      



    
