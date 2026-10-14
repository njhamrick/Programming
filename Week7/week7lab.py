#LOOPS LAB

#PART 1: Basic While Looping
#Starts at 1 and keeps counting until the count reaches 5
x = 1

while x <= 5:
    print(x)
    x+= 1

#PART 2: While Loop That Uses User Input
#Keeps asking the user for their age until a valid age between 1 and 100 is entered
while True:
   age = int(input("Enter your age: "))
   if age >=1 and age <=100:
       print("Valid age")
       break
   else:
       print("Invalid age, please enter an age between 1 and 100.")
    
#PART 3: Basic For Loop
#Loops through the names of my fish and prints each fish name
fishNames = ['Pyrrhus', 'Pan', 'Eos']
for fish in fishNames:
    print(fish)

#PART 4: Loop with A Range
#Loops through the numbers 2 and 7 (prints 2 through 7, 8 is excluded)
for i in range(2, 8): #Starts range at 2 instead of 0
    print(i)
#Loops through the numbers 2 and 7 and prints their squares
for i in range(2, 8):
    print(i ** 2)

#PART 5: Loop Through A String
#Loops through each letter in my name and prints them individually
name = 'Nikki'
for letter in name:
    print(letter)

#PART 6:Controlling A Loop
#Counts up to 10 but stops at 8 due to the break statement
x = 1
while x < 10:
    if x == 8:
        break
    print(x)
    x+= 1

#PART 7: Nested Loops
#The inside loop goes through the numbers 1 to 3 for each iteration of the outside loop
for x in range(1,4):
    for y in range(1,4):
        print(x, y)

#Loops_Flowchart.png was completed in GoogleDocs, screenshot, and saved as an image file. Added to the week7 folder.