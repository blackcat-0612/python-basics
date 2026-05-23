# lists is a collection of items stored in one variable !
#
shopping = ["milk", "eggs", "butter", "banana"]
sales = [1000, 3000, 3500]

# accessing items
fruits = ["apple", "oranges", "mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# adding items
fruits.append ("grapes")        # adds to end
fruits.insert(1,"kiwi")         # adds at position 1

# removing items
fruits.remove("apple")          # removes by value
fruits.pop()                    # removes last item

# list length:
print(len(fruits))

# looping
for fruit in fruits:
    print(fruit)

# slicing
print(fruits[0:2])              # first 2 items

