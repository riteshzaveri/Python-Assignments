import math

# Ask the user for a number as input
number = float(input("Enter a number: "))

# Calculate square root, natural log, and sine (in radians)
sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)

# Print the results
print("Square Root:", sqrt_result)
print("Natural Logarithm (base e):", log_result)
print("Sine (in radians):", sine_result)