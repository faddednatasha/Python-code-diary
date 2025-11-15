Program No. : 7
#Program : Combine all above 5 arithmetic operations in one program.

def add(a, b):
    """Calculates the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Calculates the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Calculates the product of two numbers."""
    return a * b

def divide(a, b):
    """Calculates the quotient of two numbers, with division-by-zero handling."""
    if b == 0:
        return "Cannot divide by zero (Denominator is 0)"
    else:
        # Standard division, resulting in a float
        return a / b

def average(a, b):
    """Calculates the mean (average) of two numbers."""
    # Sum of numbers divided by the count (which is 2)
    return (a + b) / 2

# --- Main Program Execution ---

print("--- Basic Arithmetic Calculator ---")

# 1. Get user input
try:
    num1_str = input("Enter the first number (A): ")
    num2_str = input("Enter the second number (B): ")

    # Convert inputs to float to handle decimals in all operations
    num1 = float(num1_str)
    num2 = float(num2_str)

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
    exit() # Stop the program if input is invalid

# 2. Perform all operations
sum_result = add(num1, num2)
difference_result = subtract(num1, num2)
product_result = multiply(num1, num2)
division_result = divide(num1, num2)
average_result = average(num1, num2)

# 3. Display all results
print("\n--- Results ---")
print(f"Numbers used: A = {num1}, B = {num2}\n")

print(f"1. Addition (A + B):         {sum_result}")
print(f"2. Subtraction (A - B):      {difference_result}")
print(f"3. Multiplication (A * B):   {product_result}")
print(f"4. Division (A / B):         {division_result}")
print(f"5. Average of A and B:       {average_result}")
