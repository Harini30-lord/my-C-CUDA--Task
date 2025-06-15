# main.py

import mymath

# Calculate factorial
n = 5
factorial_result = mymath.factorial(n)
print(f"The factorial of {n} is {factorial_result}")

# Check if a number is prime
num = 17
if mymath.is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
