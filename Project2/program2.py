
painting_outside=input("Are you planning on painting outside? ")

if painting_outside=="yes":
    raining=input("Is it raining? ")

    if raining=="yes":
        print ("You should paint inside.")
    else:
        print ("It is safe to paint outside.")

else:
    print("You are painting inside.")

