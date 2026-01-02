Program No. : 22
      Program : To check whether number is positive or negative.

def check_number_sign():
    print("--- Positive or Negative Checker ---")
    
    try:
        # 1. Get input from the user (float handles decimals too)
        number = float(input("Enter any number: "))

        # 2. Check the condition
        if number > 0:
            print(f"The number **{number}** is **Positive**.")
        elif number < 0:
            print(f"The number **{number}** is **Negative**.")
        else:
            print("The number is **Zero**.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid numerical value.")

# Run the program
check_number_sign()
