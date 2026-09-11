#At least one of those programs should get input from the user, 
# and then construct some output that uses that input as part of it. 
# At least one of those programs should do some math. Project Examples/Ideas
#  on a separate page. Your project does not have to follow these examples 
# precisely (you can make your own thing, if you really want) but if you're 
# struggling to come up with an idea I would suggest you follow the examples.


# I changed each input to a float so Python will treat the user input as numbers
# instead of strings. The terminal will ask each question one at a time, storing
# each number input provided.
desired_hours=float(input("What are your desired hours of sleep? "))
hours_slept=float(input("How many hours did you sleep last night? "))
# sleep_debt is the total we are looking for, this subtracts the desired_hours 
# by the hours_slept
sleep_debt=(desired_hours)-(hours_slept)
# This prints the sleep_debt (total)
print(f"You are currently owed {sleep_debt} hours of sleep.")