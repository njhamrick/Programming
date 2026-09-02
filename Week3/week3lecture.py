# a=10
# b=3
# c= a+b
# d= a/b
# #Difference between integer and float
# #Integer is a whole number, while a float is a decimal number. 
# #Integer will round down to the nearest whole number, while float will give you a decimal result.
# #Integer (3, 6, 10, 23)
# #Float (3.5, 6.9, 10.2, 23.7)

# x=15
# y=2.5

# print (x,type(x))
# #prints the class type of the variable x, which is an integer
# print (y,type(y))
# #prints the class type of the variable y, which is a float

# print(x//y) #// floor division operator, which rounds down to the nearest whole number
# print(x/y) #/ regular division operator, which gives you a decimal result
# #Both gives 6.0, but the first one is an integer and the second one is a float. The first one is an integer 
# # because it is using the floor division operator (//) which rounds down to the nearest whole number. The second one 
# # is a float because it is using the regular division operator (/) which gives you a decimal result.

# user_text= input("Type something: ")
# print(f"Hello, {user_text}!")

#user input authomatically converts to a string, so if you want to use it as a number, 
# you have to convert it to an integer or float.
# age_text=input("How old are you? ") #asking the user for their age and storing it as a string in the variable age_text
# age_int=int(age_text) #converting the string to an integer and storing it in the variable age_int
# print(age_int,type(age_int)) 

# print("How old are you?")
# age = input("Enter your age:")
# print(f"Wow! You're {age} years old. That's old!")

#String is text data
# message= "Hello, World!"
# print(message, type(message)) #prints the class type of the variable message, which is a string

# word="Python"
# print(word[0])#This selects the first character in the string, which is "P".The first character in a string is at index 0
# print(word[1])#This selects the second character in the string, which is "y".The second character in a string is at index 1
# print(word[2])#This selects the third character in the string, which is "t".The third character in a string is at index 2   
# print(word[3])#This selects the fourth character in the string, which is "h".The fourth character in a string is at index 3
# print(word[4])#This selects the fifth character in the string, which is "o".The fifth character in a string is at index 4
# print(word[5])#This selects the sixth character in the string, which is "n".The sixth character in a string is at index 5

#Slicing is when we want to print a range from string text
# word="Python"
# print(word[0:4])#This selects the first four characters in the string, which is "Pyth".The first character in a string is at index 0 
# # and the fourth character is at index 3, so we have to go one index further to get the fourth character.
# #start:end, the end index is not included in the slice, so we have to go one index further to get the fourth character.
# # .upper()  .lower() --- must include the () after for it to work
# print("Hello, World!".upper())#This converts the string to uppercase, which is "HELLO, WORLD!"
# print("Hello, World!".lower())#This converts the string to lowercase, which is "hello, world!"
# phrase= "Hello, World!"
# print(phrase.upper())#This converts the string to uppercase, which is "HELLO, WORLD!"
# print(phrase.lower())#This converts the string to lowercase, which is "hello, world!"   

# fruits= ["apple", "banana", "cherry"]
# numbers= [10, 2, 3.5]
# mixed= [100, "score", 3.5]

# print(fruits)
# print (fruits[0]) #This selects the first element in the list, which is "apple".The first element in a list is at index 0
# print (fruits[0:2]) #This selects the first two elements in the list, which is "apple" and "banana".The first element in a list is at index 0
# print (numbers)
# print (mixed)

# fruits.append("orange") #This adds the element "orange" to the end of the list
# print(fruits)