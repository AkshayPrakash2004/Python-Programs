print("Welcome to BMI calculator")
print("Enter your weight in Kilograms")
w=int(input())
print("enter your height in Meters")
h=float(input())
bmi= float(w/(h**2))
print("Your BMI is",bmi)
if bmi<18.5:
 print("Underweight")
elif bmi<25:
 print("Normal")  
elif bmi<30:
 print("Overweight") 
elif bmi<35:
 print("Obese")
elif bmi>35:
 print("Clinically Obese")
