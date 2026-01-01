Program No. : 21
      Program : Program to check even or odd numbers.

def check_even_odd():
    print("--- Even or Odd Checker ---")
    
    try:
        # 1. Get integer input from the user
        number = int(input("Enter an integer: "))

        # 2. Use the modulo operator to check the remainder
        if number % 2 == 0:
            print(f"The number **{number}** is **Even**.")
        else:
            print(f"The number **{number}** is **Odd**.")

    except ValueError:
        print("Error: Please enter a valid whole number.")

# Run the program
check_even_odd()
