Program No. : 31
      Program :  To check whether the year leap year or not.

def check_leap_year():
    print("--- Leap Year Checker ---")
    
    try:
        # 1. Get the year from the user
        year = int(input("Enter a year (e.g., 2024): "))

        # 2. Apply Leap Year Logic
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    print(f"**{year}** is a Leap Year.")
                else:
                    print(f"**{year}** is NOT a Leap Year.")
            else:
                print(f"**{year}** is a Leap Year.")
        else:
            print(f"**{year}** is NOT a Leap Year.")

    except ValueError:
        print("Error: Please enter a valid whole number for the year.")

# Run the function
check_leap_year()
