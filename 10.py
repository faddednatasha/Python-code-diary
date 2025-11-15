Program No. : 10
#Program : Find area and perimeter of circle.

import math

def calculate_circle_properties():
    """
    Prompts the user for the circle's radius and calculates its area and circumference.
    """
    print("--- Circle Area and Circumference Calculator ---")

    # 1. Get the radius from the user
    try:
        radius_str = input("Enter the radius of the circle: ")
        radius = float(radius_str)

        if radius < 0:
            print("Error: Radius cannot be negative.")
            return

    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the radius.")
        return

    # 2. Calculate the Area
    # Area = pi * r^2. We use math.pi and the exponent operator (**)
    area = math.pi * (radius ** 2)

    # 3. Calculate the Circumference (Perimeter)
    # Circumference = 2 * pi * r
    circumference = 2 * math.pi * radius

    # 4. Display the results
    print("\n--- Results ---")
    print(f"Radius (r): {radius}")
    print(f"Value of Pi (π): {math.pi}")
    print(f"Area of the Circle (πr²): **{area:.4f}**")
    print(f"Circumference (Perimeter) of the Circle (2πr): **{circumference:.4f}**")

# Run the function
calculate_circle_properties()
