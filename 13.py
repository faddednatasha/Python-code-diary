Program No. : 13
 Program :  Swap two numbers without using third variable.

def swap_without_temp_arithmetic():
    """
    Swaps two numbers using addition and subtraction.
    """
    print("--- Swapping Program (Arithmetic Method) ---")

    # 1. Get user input
    try:
        a_str = input("Enter the first number (A): ")
        b_str = input("Enter the second number (B): ")

        # Convert to float to handle both integers and decimals
        a = float(a_str)
        b = float(b_str)

    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    print(f"\nBefore Swap: A = {a}, B = {b}")

    # 2. Swapping Logic
    a = a + b  # A now holds the sum
    b = a - b  # B is updated to the original value of A
    a = a - b  # A is updated to the original value of B

    # 3. Display the result
    print(f"After Swap:  A = {a}, B = {b}")

# Run the function
swap_without_temp_arithmetic()
