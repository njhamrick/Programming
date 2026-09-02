# a= 13               #I commented out the variables for a and b so that I can overwrite them with user input.
# b= 7.2
a= int(input("Enter an integer: "))
b= float(input("Enter a float: "))


print (a,type(a))
print (b,type(b))

print(a*b)  #Yes, you can multiply an integer and a float. The result will be a float.
print(a/b)  #Yes, you can divide an integer and a float. The result will be a float.


#What is a String? A string is text data

message= "What is your favorite color? "
answer= input(message)
print(f"Wow! {answer} is a great color!")

print(message[0]) #This selects the first character 
substring=(message[0:7]) # substring is a portion of the string, in this case, the first 7 characters of the string. 
print(substring)

#The data a list can contain is many types, and they can be mixed. A list can contain strings, integers, floats, etc.

pets= ["dog", "cat", "fish"]
print(pets)
pets.append("ferret") #This adds the element "ferret" to the end of the list
print(pets)
pets.remove("fish") #This removes the element "fish" from the list
print(pets)

print(len(pets)) #This prints the length of the list


# In this lab, I learned that .remove() can easily remove an item from a list, just as .append() can easily add an item. This would be extremely useful in 
# situations requiring you remove/add specific items from a large list. I also learned about substring, which is a portion of a string that you can select. This would be useful in situations
# where you need to extract a specific part of a string.


