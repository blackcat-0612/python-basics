 #A function in Python is a block of organized, reusable code that is used to perform a single, related action. 
 # Here's a detailed overview of functions in Python:

## 1. defining & calling a function
#to define a function in Python, you use the `def` keyword followed by the 
#function name and parentheses `()`. The statements that form the body of the 
#function start at the next line and must be indented.
#To call a function, simply use its name followed by parentheses containing any required arguments.

def greet (name):
    print(f"hello, {name}!") #f-string puts the variable inside strings 

greet("Alice")
greet("Jay")
greet("Daisy")
greet("Tom")
greet("Gina")

#def --> define (Create it)
#greet --> sample function name
#(name) -->parameter 


### 3. Parameters and Arguments
#Parameters**: These are variables that are defined within the function's definition.
#Arguments**: These are the actual values passed to the function when it is called.

def add(a, b):            # a, b are PARAMETERS
    """This function adds two numbers."""
    return a + b
result = add(3, 5)      # 3, 5 are ARGUMENTS
print(result)  # Output: 8

#just another sample
def subtract (a, b):
    return a - b
result = subtract(10, 7)
print(result)

#just another sample
def multiply (a, b):
    return a * b
result = multiply (3, 2)
print (result)


### 4. Default Parameters
#You can provide default values for parameters in the function definition. 
#If an argument is not provided when calling the function, it will use the default value.
def greet(name="Guest"):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

#writing my own example
def t_shirt(size="medium"):
    print(f"{size} t_shirt!")
t_shirt()
t_shirt("small")
t_shirt("large")
t_shirt("medium")


#return values
#return values is simply sends a value back from the function

def add (a, b):
    return (a + b)

result = add (3, 5)
print(result)

#
def add (a, b):
    return (a + b)

result = add (3, 5)
print(result + 100)
print(result * 2)



#Keyword & variable-length arguments are advanced !

### 5. Keyword Arguments
#you can pass arguments to functions using keywords, which makes the code more readable and allows you to skip parameters.

def greet(first_name, last_name):
    """This function greets a person using first and last name."""
    print(f"Hello, {first_name} {last_name}!")

greet(last_name="Smith", first_name="John")
# Output: Hello, John Smith!

### 6. Variable-Length Arguments
#Positional Arguments**: Using `*args` to allow a function to accept any number of positional arguments.
#Keyword Arguments**: Using `**kwargs` to allow a function to accept any number of keyword arguments.

def add(*numbers):
    """This function adds any number of numbers."""
    return sum(numbers)
result = add(1, 2, 3, 4)
print(result)  # Output: 10

def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York