favorite_food = ["beef", "chichen satay", "yogurt", "fish", "seafood"]
# printing the whole list

print(favorite_food)

#printing the first food

print(favorite_food[0])

#print the last food
print(favorite_food[-1])

# print how many foods are in the list
print(len(favorite_food))

favorite_food.append("cheese")  #adds to end
print(favorite_food) 

favorite_food.insert(0, "avocado")  #adds at first position
print(favorite_food)

favorite_food.pop(0)    #removes by position
print(favorite_food)