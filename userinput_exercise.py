#Get User Input**: Write a program that asks the user for their name and greets 
#them with a personalized message.

prompt = input("What is your name? ")
print("Hello, " + prompt + "! Welcome to the world of programming!")

#**Convert Input**: Modify the above program to ask the user for their age, 
#convert it to an integer, and then print a message indicating how old they are in 5 years

age = int(input("What is your age? "))
future_age = age + 5
print("In 5 years, I will be " + str(future_age) + " years old.")


#**Error Handling**: Create a program that prompts the user to enter a 
#floating-point number and calculates its square. Include error handling to ensure the input is valid.

number = input("Enter a floating-point number: ") #ask the user to input a number
try:                                              #attempt this code block
    number = float(number)                        #convert the input to a float
    results = number ** 2                         #calculate the square of the number
    print("The square of", number, "is", results)
except ValueError:                  #if a ValueError occurs, execute this block of code
    print("Invalid input. Please enter a valid floating-point number.")


#note on line 18. i can already write my code as this: number=float(input("Enter a floating point number:" )).
#clean code

#Another exercise ;)
#Ask the user for two numbers
#Add them together
#Print the result

number1 = int(input("Give me two numbers: "))
number2 = int(input("Give me two numbers: "))
total = number1 + number2
print("The sum is: " + str(total))