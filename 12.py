Program No. : 12
 Program :  Swap two numbers using third variable.

def swap_with_temp_variable():
    """
    Takes two numbers as input and swaps their values using a temporary variable.
    """
    print("--- Swapping Program (Using Temp Variable) ---")

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
    # Step 1: Store the original value of A in a temporary variable
    temp = a

    # Step 2: Assign the value of B to A
    a = b

    # Step 3: Assign the original value of A (stored in temp) to B
    b = temp

    # 3. Display the result
    print(f"After Swap:  A = {a}, B = {b}")

# Run the function
swap_with_temp_variable()
