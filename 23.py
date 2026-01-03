Program No. : 23
      Program :  To find maximum of 2 numbers.

def find_maximum():
    print("--- Maximum of Two Numbers ---")
    
    try:
        # 1. Get two numbers as input
        num1 = float(input("Enter first number (A): "))
        num2 = float(input("Enter second number (B): "))

        # 2. Compare the numbers
        if num1 > num2:
            print(f"\n**{num1}** is the maximum.")
        elif num2 > num1:
            print(f"\n**{num2}** is the maximum.")
        else:
            print("\nBoth numbers are **equal**.")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the program
find_maximum()
