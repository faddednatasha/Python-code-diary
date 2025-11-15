Program No. : 9
#program : Find Quotient and reminder, input is 2 numbers.

def find_quotient_and_remainder():
    print("--- Quotient and Remainder Calculator ---")

    # Get user input
    try:
        dividend_str = input("Enter the dividend (the number to be divided): ")
        divisor_str = input("Enter the divisor (the number to divide by): ")

        dividend = int(dividend_str)
        divisor = int(divisor_str)

    except ValueError:
        print("Error: Invalid input. Please enter whole numbers (integers) only.")
        return

    # Check for division by zero
    if divisor == 0:
        print("\nError: The divisor cannot be zero.")
        return

    # 1. Calculate the Quotient (Integer Division)
    # The // operator performs FLOOR DIVISION, giving the whole number part of the result.
    quotient = dividend // divisor

    # 2. Calculate the Remainder
    # The % operator performs the MODULO operation, giving the remainder after division.
    remainder = dividend % divisor

    # Display the results
    print("\n--- Results ---")
    print(f"Dividend: {dividend}")
    print(f"Divisor: {divisor}")
    print(f"Quotient ({dividend} // {divisor}): **{quotient}**")
    print(f"Remainder ({dividend} % {divisor}): **{remainder}**")

# Run the function
find_quotient_and_remainder()