

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
    print(answer)

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

def power():
    # Ask the user to enter n and m
    n = int(input("Please enter n: "))
    m = int(input("Please enter m: "))

    # Initialize the result
    result = 1

    # Multiply the result by n m times
    for i in range(m):
        result = result * n

    # Print the result
    print(n, "to the power of", m, "is", result)


