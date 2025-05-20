# Ask the first input number from user
input1 = int(input("Enter a number: "))

# Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Calls the function with a sample number and prints the output
output = factorial(input1)
print(f"The factorial of {input1} is:", output)