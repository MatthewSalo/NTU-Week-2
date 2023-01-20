# Function to find the LCM of two numbers

def lcm():
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

def prime():
    n = int(input("Please enter a number: "))

    # Check if user input is less than 2
    if (n < 2):
        print("Please enter a number greater than 2")

    else:
        for num in range(2, n + 1):
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime:
                print(num)