# How would you open a file called 'thisimyfile.txt' to read only? What would opening this file this way do?
# Can you automatically close a file after opening it? If so, how and what would the syntax look like?
# Is there a way to verify that a file already exists? Why would you need to check if it already exists?
# Can you create a file on demand if one doesn't exist or does the file have to exist?
# What would be the benefits of being able to read or write to a file? What happens after a regular python program runs? What would be the difference when reading and writing to a file?


file_path = "thisimyfile.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)
# Using "r" when opening a file means you are opening it in read-only mode. Python will give you an error if the file does not exist.


# Using with ensures that the file is properly closed after the block finishes running so you don't have to manually close it.


try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
#You can use a try-except block that allows the program to attempt to open a file and handle the case where the file does not exist to prevent the program from crashing.

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' has been created.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")
# Using "x" when opening a file means you are trying to create a new file. If the file already exists, Python will stop and raise a FileExistsError.


txt_data = "I like pizza!"

file_path = "output.txt"
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' has been created.")
# If the file does not exist, it will be created using "w". If it does exist, its contents will be overwritten.

# Reading and writing to files allows you to either access existing data or store new data. Writing to a file ensures that your data is saved even after the program ends. Reading from a file allows you to retrieve and use previously stored data.
# Normally, data in a Python program exists only while the program is running. Once the program ends, all data in memory is lost.