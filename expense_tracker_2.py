
print ("this is my expense tracker exercise!")

print("1. Add expense")
print("2. View expenses")
print("3. Total expenses")
print("4. Exit")

expenses = []   #creating an empty list


while True:             #start infinitiy loop
    option = input("Choose: ")  #asking users to choose

    if option == "1":   #if they choose 1
        name = input ("enter expenses name: ")
        amount = float(input("enter amount: "))
        if amount <= 0:                         #another control added in case user entered 0
            print("amount must be greater than 0. invalid input! ") #when users entered 0, print this
        else:
            expenses.append({
                "name": name, 
                "amount": amount
            })
            print("expenses added!")
    
    elif option == "2":     #if user entered 2
            for i, expense in enumerate (expenses): #the purpose of i here .....is Index.
                print(f"{i+1}. {expense['name']} - ${expense['amount']: .2f} ")

    elif option =="3":
         total = sum (expense["amount"] for expense in expenses)
         print(f"total expenses: ${total: .2f}")

    elif option == "4":
         print("exit calculator!")
         break