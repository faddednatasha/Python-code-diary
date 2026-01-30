Program No. : 27
      Program :  To calculate the electricity bill when the condition of meter reading are: units less than 100🡪2.25, 100-200 🡪 3.00, 200-500🡪4.25 and above 7.00Rs

def calculate_electricity_bill():
    print("--- Electricity Bill Calculator ---")
    
    try:
        # 1. Input total units consumed
        units = float(input("Enter the total units consumed: "))

        if units < 0:
            print("Error: Units consumed cannot be negative.")
            return

        # 2. Determine the rate based on unit slabs
        if units <= 100:
            rate = 2.25
        elif units <= 200:
            rate = 3.00
        elif units <= 500:
            rate = 4.25
        else:
            rate = 7.00

        # 3. Calculate total amount
        total_bill = units * rate

        # 4. Display the result
        print("\n--- Bill Summary ---")
        print(f"Units Consumed: {units}")
        print(f"Applied Rate:   {rate} Rs per unit")
        print(f"Total Amount:   **Rs. {total_bill:.2f}**")

    except ValueError:
        print("Error: Please enter a valid number for units.")

# Run the program
calculate_electricity_bill()
