print("Welcomen to Leap Year calculator")
print("Enter the year")
y=int(input())
if y%4 == 0:
    if y%100 == 0:
        if y%400 == 0:
         print("Leap year")
        else:
         print("not a Leap year")
         
    else:
     print("Not a Leap Year")
else:
    print("not a leap year")