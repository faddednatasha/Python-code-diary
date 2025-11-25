Program No. : 15
      Program :  Convert temperature Fahrenheit to Celsius.
 
def fahrenheit_to_celsius():
    """
    Prompts the user for a temperature in Fahrenheit and converts it to Celsius.
    """
    print("--- Fahrenheit to Celsius Converter ---")

    # 1. Get the temperature in Fahrenheit from the user
    try:
        fahrenheit_str = input("Enter temperature in Fahrenheit (°F): ")
        fahrenheit = float(fahrenheit_str)

    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the temperature.")
        return

    # 2. Apply the conversion formula
    # C = (F - 32) * (5/9)
    # Note: 5/9 must be calculated as a float (0.555...) for accurate results.
    celsius = (fahrenheit - 32) * (5 / 9)

    # 3. Display the result
    print("\n--- Result ---")
    print(f"Input Temperature: **{fahrenheit:.2f} °F**")
    print(f"Converted Temperature: **{celsius:.2f} °C**")

# Run the function
fahrenheit_to_celsius()
