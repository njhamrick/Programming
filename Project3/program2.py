# Write two Python programs.

# Each program should use a loop to solve a problem or reach a goal. Each program should be an example of a different kind of loop.*

# One of these programs will be an example of a finite loop (its condition should only allow it to repeat a fixed number of times - for example, using a for loop with a range or list.).

# Program 2: Indefinite loop
# This loop runs until the user enters 'x' to exit.
while True:
    user_input = input("Enter a number or type 'x' to exit: ")
    if user_input.lower() == "x":
        print("Goodbye!")
        break
    print(f"You entered: {user_input}")