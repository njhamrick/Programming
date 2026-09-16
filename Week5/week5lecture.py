# If, Else, Elif
#Boolean: True or False data type
    #print(5<10)    print(5>10)

answer=input("Do you want to continue? (yes or no) ").lower()
if answer == "yes":
    print("Continuing the program...")
elif answer == "no":
    print("Why do you not want to continue?")
else:
    print("Okay, exiting now.")

#Comparison operators:
    # ==   >   <   >=  <=  !=(not equal)

#true/false
score=85
print(score>75)
print(score==85)
print(score!=85)

#How do we compare 3 values?
    #We can compare 3 or more values with "and" & "or"
temp=72
if temp >= 68 and temp <= 75:
    print("Comfy room temp")
    #When using "and" both conditions must be true
    #When using "or" at least one condition must be true

day="Saturday"
is_holiday=False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You don't have class today.")


grade=75
if score <= score <90:
    print("Mediocre grade")

#Give a condition program that prints out shipping cost depending on total price

total=float(input("Enter your total order: "))
if total<25:
    print("Shipping is $10")
elif total<50:
    print("Shipping is $5")
else:
    print("Shipping is free! ")

list1=[1,2,3]
list2=[1,2,3]
list3=list1

print(list1==list2)
print(list1 is list2)