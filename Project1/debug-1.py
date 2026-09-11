# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.
# Add your own comments discussing what you did and why you did it

# Debug Exercise 2
# This program should add three numbers together.
# total = 0
# num1 = input("What's the first number? >")
# total = num1
# num2 = input("What's the second number? >")
# total = num2
# num3 = input("What's the third number? >")
# total = num3
# print(f"Total is: {total}")


# I changed each input to a float so Python will treat the user input as numbers
# instead of strings. The terminal will ask each question one at a time, storing
# each number input provided.
num1 = float(input("What's the first number? >"))
num2 = float(input("What's the second number? >"))
num3 = float(input("What's the third number? >"))
#  I removed each original total, and added a total so that all three numbers
# would be added together
total = (num1)+(num2)+(num3)
# This prints the final total after the three numbers have been added together.
print(f"Total is: {total}")