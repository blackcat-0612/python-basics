# 1 
def greet(name, age):
    return f"Hi {name}! You are {age} years old."  #{} putting variables inside the string

result = greet ("Jay", 25)
print(result)

# 2
def person_info (age=25, city="Singapore", name="Shiela"):
    print(f"My name is {name}! ")
    print(f"I am {age} years old !")
    print(f"Hi! I am {name}, {age} years old from {city}!")

person_info ()    #calling the functions


# 3
def multiply(length, width):
    return length * width

result = multiply (10, 5)
print(f"The area of the rectangle is {result}!")

# 4
def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

result = convert (100)
print(f"100C is equal to {result} F")