#basic of f-string
name = "Tesseya"
age = "25"
print(f"hello, {name}! ")
print(f"I am {age} years old")

# Decimals
# f means float
# :.2f, show only 2 decimal places

pi = 3.4569088
print(f"pi is {pi: .2f}") 
print(f"pi is {pi: .4f}")

# numbers with commas

salary = 100000 
print(f"salary: {salary: ,}")


# math inside f-strings:
a = 90
b = 5
print(f"90 + 5 = {a + b} ")


# uppercase/lowercase

name = "tesseya"
print(f"{name.upper()}")
print(f"{name.capitalize()}")
