### Exercise: Temperature Check
#Objective**: Write a program that checks the temperature and prints appropriate messages based on the temperature.

#Define Variables**:
   #Get the temperature from the user as an integer.
   #Assign this value to a variable named `temperature`

temperature = int(input("What is user temperature?" ))
if temperature >=38:
    print("you have a fever!")
elif temperature >=36 and temperature <= 38: #using 'and' nor 'or' means both conditions must be true
    print("you are normal!")
elif temperature <= 36:
    print("you are low!")
