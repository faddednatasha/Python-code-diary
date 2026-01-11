Program No. : 24
      Program :  To find maximum of 3 numbers

def find_max_of_three():
    print("--- Maximum of Three Numbers ---")
    
    try:
        # 1. Get three numbers as input
        a = float(input("Enter first number (A): "))
        b = float(input("Enter second number (B): "))
        c = float(input("Enter third number (C): "))

        # 2. Comparison Logic using logical 'and'
        if (a >= b) and (a >= c):
            largest = a
        elif (b >= a) and (b >= c):
            largest = b
        else:
            largest = c

        # 3. Display Result
        print(f"\nThe maximum of {a}, {b}, and {c} is: **{largest}**")

    except ValueError:
        print("Error: Please enter valid numeric values.")

# Run the program
find_max_of_three()
