def calculate (num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"
    
print("welcome to tesseya's calculator")

while True:
    num1 = float(input("enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("enter first number: "))

    result = calculate (num1, operator, num2)
    print(f"Result: {num1} {operator} {num2} = {result: .2f}")

    again = input("Calculate again? (y/n): ")
    if again == "n":
        print("goodbye!")
        break

