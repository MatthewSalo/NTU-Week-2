
n = int(input("Please enter a number: "))

# Check if user input is less than 2
if (n < 2):
    print("Please enter a number greater than 2")

else:
    for num in range(2,n+1):
        prime = True
        for i in range(2,num):
            if (num % i == 0):
                prime = False
        if prime:
            print(num)