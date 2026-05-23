#1 basic user input program
#The simplest way to get user input is by using the `input()` function. 
#This function reads a line from input, converts it into a string, and returns that string.

#2 Get user input
name = input("What is your name? ") #the input function takes a string argument which is the prompt that will be displayed to the user.

#3 get integer input
age = int(input("What is your age? ")) #the input function returns a string, so we need to convert it to an integer using the `int()` function.

print("You are " + str(age) + " years old.") #we can also convert the integer back to a string using the `str()` function to concatenate it with other strings.

#4 get float input
height = float(input("What is your height in meters? ")) #the input function returns a string, so we need to convert it to a float using the `float()` function.
print("my height is " + str(height) + " meters.")

#combine user input with other data types
#I can combine user input with other data types to create more complex programs. 
number = int(input("Enter a number: "))
result = number * 2
print("The double of your number is: " + str(result))