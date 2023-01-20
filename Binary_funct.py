
def binary(n):
    # Create an empty list to store the binary representation
    binary_list = []

    # Loop through the number until it is 0
    while n > 0:
        # Calculate the remainder and append it to the list
        remainder = n % 2
        binary_list.append(remainder)

        # Update the number
        n = n // 2
    # Reverse the list
    binary_list.reverse()

    # Return the list
    return binary_list

print(binary(6))