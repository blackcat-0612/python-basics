expenses = []           #im creating an empty list

# introduction
print("welcome to expense tracker....my attempt to appy my basic python skills")

# menu
print("1. Add expense")
print("2. View expenses")
print("3. Total expenses")
print("4. Exit")

choice = input("Choose: ")
while True:
    print("\n1. Add expense")               # numbers cant be used as variable names
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("enter expense name: ")
        amount = float(input("enter an amount: "))
        expenses.append({"name": name, "amount": amount})
        print("expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("no expenses yet!")
        else:
            for i, expense in enumerate(expenses):
                print(f"{i+1}. {expense['name' ]} - ${expense['amount']: .2f}")
    
    elif choice == "3":
        if len(expenses) == 0:
            print("no total expenses yet!")
        else:
            total = sum(expense["amount"] for expense in expenses)
            print(f"total expenses: ${total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break


#next--figure oout why code choose 3 is not working
