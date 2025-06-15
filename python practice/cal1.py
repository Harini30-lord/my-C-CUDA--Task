import sys

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculator.py 'mathematical_expression'")
    else:
        expression = sys.argv[1]
        result = calculate(expression)
        print(f"Result: {result}")
