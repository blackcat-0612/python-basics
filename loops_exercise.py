#1. **Sum of Numbers**: Implement the code to calculate and print the sum of numbers from 1 to `n`.
n = int(input("Enter a number: ")) #n is a varibale here that stores whatever the number user types
total = 0
for i in range (1, n+1):       #i used n initially, claude said it overwrites. changed to i=loop counter
    total = total + i
print("the sum is:", total)

#n = 4
#total = 0
#i = 1 -> total = 0 + 1
#i = 2 -> total = 1 + 2
#i = 3 -> total = 3 + 3
#i = 4 -> total = 6 + 4
#explanation of why the sum is: 10


#2. **Even Numbers**: Iterate over numbers from 1 to 20 and print only the even numbers.
for j in range (1, 21):
    if j % 2 == 0:
        print (j)   #the result of this code are even numbers

for j in range (1, 22):
    if n % 1 == 0:
        print (n) #the result of this code are odd numbers


#3. **Break Statement**: Use a loop to allow the user to input multiple values until they enter 'q' or 'Q'.
while True:
    user = input("enter a value: ")
    if user == 'q' or user == 'Q':
        break
    print ("you entered:", user)







#4. **Continue Statement**: Skip printing numbers that are divisible by 3.




