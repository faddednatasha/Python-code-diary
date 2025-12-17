Program No. : 18
      #Program : Calculate distance between two cities in km. and change it into meters, feets and inches.

def convert_distance():
    print("--- City Distance Converter ---")

    # 1. Get distance in kilometers from the user
    try:
        km = float(input("Enter the distance between two cities (in km): "))
        
        if km < 0:
            print("Error: Distance cannot be negative.")
            return
            
    except ValueError:
        print("Error: Please enter a valid numerical value.")
        return

    # 2. Perform Conversions
    # Kilometers to Meters
    meters = km * 1000

    # Kilometers to Feet (1 km = 3280.84 feet)
    feet = km * 3280.84

    # Kilometers to Inches (1 km = 39370.1 inches)
    inches = km * 39370.1

    # 3. Display the results
    print(f"\n--- Conversion Results for {km} km ---")
    print(f"Distance in Meters:  **{meters:,.2f} m**")
    print(f"Distance in Feet:    **{feet:,.2f} ft**")
    print(f"Distance in Inches:  **{inches:,.2f} in**")

# Run the program
convert_distance()
