#Age Classifier:
age=float(input("Enter your age: "))
if age<=12:
    print("You are a child.")

elif age>=13 and age<=19:
    print("You are a teenager.")

elif age>=20 and age<=64:
    print("You are an adult.")

else:
    print("You are a senior.")

#BMI Checker
height=float(input("Enter your height (inches): "))
weight=float(input("Enter your weight (pounds): "))

height2=height*height
BMI=(weight/height2*703)
print (BMI) 
if BMI<18.5:
    print("You are underweight.")
elif BMI==18.5 or BMI<=24.9:
    print("You are healthy.")
elif BMI==25 or BMI<=29.9:
    print("You are overweight.")
else:
    print("You are obese")

#Discount Calculator
total=float(input("Please enter your total: "))
if total<30:
    print("You get a 0% discount.")
elif total<50:
    print("You get a 5% discount.")
elif total<100:
    print("You get a 10% discount.")
else:
    print("You get a 15% discount.")
