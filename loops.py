#Loops are another fundamental concept in programming that allow you to  execute a block of code repeatedly. Python provides two types of loops: `for` 
#loops and `while` loops.loops repeats codes over and over again until the conditions aae met

##1. `for` loop
#A `for` loop iterates over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. 
#It executes the block of code for each item in the sequence.
#repeats FOR each item in the list

for i in range(5):  #colon means "start a block code" and whenever i used colon the next line must be indented! -->rule
    print (i)

##2. `while`loop
#A `while` loop continues to execute as long as a specified condition is true. 
#The block of code inside the loop is executed repeatedly until the condition becomes false.

count = 1
while count <= 5:
    print(count)
    count += 1


##nested loops
# loops inside other loops that's why its called nested
for i in range (3):
    for j in range (5):
        print (i, j)

##loop control statements
 #**`break`**: Terminates the current loop and exits it.
#**`continue`**: Skips the rest of the code inside the loop for the current iteration only.

#trying to use the break and continue
#Python is designed to start counting at 0
for i in range (10):
    if i == 5:     #break at 5
        break
    print (i)

for i in range (1,6):
    if i % 2 == 0:  #break when i is 2 % 2=0
        break
    print(i)


#####LOOPS EXCERCISES####

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
for j in range (1, 21):
    if j % 3 == 0:
        continue
    print (j)


#loop controls I know:
#break --> stop the loop
#continue --> skip and keep going
#while True --> loop forever
#range(start, stop) --> control the range
#% modulo --> check even/odd/divisible


#another exercise
a = int(input("enter a number: "))
for user in range (1, 11):
    result = a * user
    print( a, "x", user, "=", result)

#
for p in range (10, 0, -1): #counting the numbers backwards
    print(p)
print( "Blast off! ")

for i in range (20): #python starts counting 0 so this will print until 19
    print(i)
print ("Yay! ")

for p in range (10, 0, -2): #counting the numbers backwards minus two
    print(p)
print( "Blast off! ")


#range (10, 0, -2)
#10 start,0 stop, -2 step


#Print all numbers from 1 to 50 that are divisible by 5:
for t in range(1, 51):
    if t % 5 == 0:
        print(t)

#Print all numbers from 1 to 50 that are divisible by 5, but skip 25 and stop at 40!
for t in range(1, 51):
    if t % 5 == 0:
        if t == 25:
            continue
        print (t)
        if t == 40:
            break


#Ask the user to enter numbers one by one.
#Add each number to a running total, Skip any number that is negative, Stop when they enter 0, Print the total at the end!

total = 
while True:
    user = int(input("Enter a numbers: "))
    if user == 0:
        break
    if user < 0:
        print("skipped negative number. ")
        continue
    total = total + user
print("Total is:", total)



