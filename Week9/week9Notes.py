#Learn how to write/read/edit files in python
#Common modes when using files
# 'r' - read mode
# 'w' - write mode
# 'a' - append mode

#If file doesn't exit, you will get and error when trying to read it
#"w" mode will create a new file if it doesn't exist, but will overwrite the file if it does exist
#"a" mode will create a new file if it doesn't exist, but will append (add content) to the file if it does exist

#with open("filename","mode")
# with open("Week9/stuff.txt","r") as file:
#     contents = file.read()
#     print(contents)

#overwrite mode example
# with open("Week9/stuff.txt","w") as file:
#     file.write("Hello, World!\n This is a new line of text.\n Third line of text.\n")
#Once we leave the indentation block, the file is automatically closed
#\n is a new line character, it will create a new line in the file

#Another way to read
#method a: read the entire file at once
# with open("Week9/stuff.txt","r") as file:
#     contents = file.read()
#     print(contents)

#method b: read the file line by line
# with open("Week9/stuff.txt","r") as file:
#     for line in file:
#         print(line)

#Append mode example (adds content to the end of the file)
with open("Week9/stuff.txt","a") as file:
    file.write("\nThis is another appended line of text.\n")

#We use r mode to vweify if a file exists