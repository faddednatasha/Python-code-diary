Program No. : 19
      Program : Calculate the sum of first and last digit of given 4 bit number

def sum_first_last_digit():
    print("--- First & Last Digit Sum (4-Digit Number) ---")

    # 1. Get input from the user
    user_input = input("Enter a 4-digit number: ")

    try:
        # Check if the length is exactly 4
        if len(user_input) != 4:
            print("Error: Please enter exactly 4 digits.")
            return

        number = int(user_input)

        # 2. Extract digits mathematically
        # % 10 gives the remainder when divided by 10 (the last digit)
        last_digit = number % 10
        
        # // 1000 gives the quotient when divided by 1000 (the first digit)
        first_digit = number // 1000

        # 3. Calculate Sum
        total_sum = first_digit + last_digit

        # 4. Display Result
        print(f"\nFirst Digit: {first_digit}")
        print(f"Last Digit:  {last_digit}")
        print(f"The sum of the first and last digit is: **{total_sum}**")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

# Run the program
sum_first_last_digit()
