import sys
if len(sys.argv) != 3:
    print("Usage: python script.py <integer1> <integer2>")
    sys.exit(1)
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("Error: Both arguments should be integers.")
    sys.exit(1)
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
