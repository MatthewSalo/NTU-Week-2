# Program start

print("Welcome to the calculator program!")

# Manually calculate multiplication
def multiply():
    # Get input from users
    number = int(input('Enter a number: '))
    multiplier = int(input('Enter a multiplier: '))
    answer = 0
    i = 0

    while i < multiplier:
        answer += number
        i = i + 1
    print("The result of the multiplication is:", answer)

# Manually calculate division
def division():
    # input two integers
    p = int(input("Enter the dividend: "))
    q = int(input("Enter the divisor: "))

    # initialise quotient and remainder
    quotient = 0
    remainder = p

    # subtract divisor from dividend until dividend is less than divisor
    while remainder >= q:
        remainder = remainder - q
        quotient += 1

    # output quotient and remainder
    print("Quotient: ", quotient)
    print("Remainder: ", remainder)

# Other function definitions
def add(n,m):
    return n + m

def subtract(n,m):
    return n - m

def exponent(n, m):
    return n ** m

# Starting a loop
while True:
    print("Please select an operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exponent")
    print("4. Evaluate a string")
    print("5. Multiplication")
    print("6. Division")
    print("7. Quit")
    selection = input("Enter your selection (1-7): ")

    if selection == '1':
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        print("The result of the addition is:", add(num1, num2))
    elif selection == '2':
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        print("The result of the subtraction is:", subtract(num1, num2))
    elif selection == '3':
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        print("The result of the exponent is:", exponent(num1, num2))
    elif selection == '4':
        expression = input("Please enter the expression: ")
        result = eval(expression)
        print("The result of the expression is:", result)
    elif selection == '5':
        multiply()
    elif selection == '6':
        division()
    elif selection == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid input, please try again.")

    # Asking the user if they want to perform another operation
    another_operation = input("Do you want to perform another operation? (yes/no): ")
    if another_operation == 'no':
        print("Goodbye!")
        break