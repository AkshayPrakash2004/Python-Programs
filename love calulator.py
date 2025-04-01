print("Welcome to Love Calculator!")
print("Enter ur crush's name")
c=str(input())
c=str(c.lower())
print("enter ur name")
y=str(input())
y=y.lower()
tt1=c.count("t")
tt1=tt1+c.count("r")
tt1=tt1+c.count("u")
tt1=tt1+c.count("e")

tt2=y.count("l")
tt2=tt2+y.count("o")
tt2=tt2+y.count("v")
tt2=tt2+y.count("e")

tt3=tt1*10+tt2
print(tt3)
