# Program to find the LCM of two numbers

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# choose the greater number
if num1 > num2:
    greater = num1
else:
    greater = num2

# initialize the LCM to 1
lcm = 1

# loop until the LCM is divisible by both numbers
while(True):
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1

# print the LCM
print("The LCM of", num1,"and", num2,"is", lcm)