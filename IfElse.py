#The `if` and `else` statements are fundamental control structures in Python that allow me to make decisions based on conditions. 
#They enable my program to execute different blocks of code depending on whether a certain condition is true or false.

#basic of IF statement

#The most basic form of an `if` statement checks if a condition is true and executes the block of code under it, if it is.

x = 10
if x > 5:
    print("x is greater than 5")

y = 4
if y > 5:
    print("y is greater than 5") #this runs when y is greater
else:
    print("y is not greater than 5") #this runs when y is not greater

#if condition:
    #runs if TRUE
#ELSE:
    #runs if FALSE

### `if-elif-else` Statement
#The `if-elif-else` statement allows you to test multiple conditions in sequence. The first condition that evaluates to true will execute its block of code.

# if-elif-else statement
score = 60
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#GOLDEN RULE
#Python checks conditions TOP to BOTTOM and stops at the FIRST one that is TRUE! ✅
#if condition1:    # checked first
#elif condition2:  # checked second
#elif condition3:  # checked third
#else:             # runs if ALL above are FALSE

#writing a program
#ask the user for their age

age = 18
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")

#if only 2 options, use ELSE

#making the above program interactive
age=int(input("Enter your age: "))
if age >=18:
    print("You are an adult!")
else:
    print("you are a minor!")


#nested if statement
x = int(input("Enter a number: "))
if x > 0:
    if x % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")


# Using logical operators
num = int(input("Enter a number: "))
if num > 0 and num < 10:
    print("Number is between 0 and 10")
elif num >= 10 or num <= -10:
    print("Number is outside the range of 0 to 10")
else:
    print("Number is zero or at the boundary.")


