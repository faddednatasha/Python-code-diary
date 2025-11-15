Program No. : 11
 Program : Find area of rectangle.

def calculate_rectangle_area():
    """
    Prompts the user for the length and width of a rectangle and calculates the area.
    """
    print("--- Rectangle Area Calculator ---")

    # 1. Get the length from the user
    try:
        length_str = input("Enter the length of the rectangle: ")
        length = float(length_str)

        # 2. Get the width from the user
        width_str = input("Enter the width of the rectangle: ")
        width = float(width_str)

        # Basic validation
        if length < 0 or width < 0:
            print("Error: Length and width must be non-negative.")
            return

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return

    # 3. Calculate the Area
    area = length * width

    # 4. Display the result
    print("\n--- Results ---")
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Area of the Rectangle (Length × Width): **{area}**")

# Run the function
calculate_rectangle_area()
