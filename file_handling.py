# the purpose of file handling is simply saving and retrieving data even after the program closess
# step 1 is writing to a file
# i literally copied this code from Claude lol

with open("notes.txt", "w") as file:         # "w" will create and wrote file
    file.write("Hello World!\n")
    file.write("I am learning Python!\n")
    file.write("File handling is useful!\n")

print("File created successfully!")

# step 2 reading of the file

with open("notes.txt", "r") as file:    # "r" read the file
    content = file.read()
    print(content)

# appending to a file
with open("notes.txt", "a") as file:    # a append
    file.write("I just appended this line!\n")

print("Line appended!")


# remember: if i'll remove "w" part, and run the code 3x
# the append lines will be added multiple times
# its because the "a" mode keeps adding everty time
# w mode helps to overwirtes everytime 