# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation selected."

# Main function
def main():
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform calculation and display result
        result = calculate(num1, num2, operation)
        print(f"The result is: {result}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
main()