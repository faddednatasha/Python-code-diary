Program No. : 28
      Program :  To find roots of a quadratic equation.

import math
import cmath # Used for complex numbers if D < 0

def solve_quadratic():
    print("--- Quadratic Equation Solver (ax² + bx + c = 0) ---")
    
    try:
        # 1. Input coefficients
        a = float(input("Enter coefficient a (non-zero): "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Error: 'a' cannot be zero in a quadratic equation.")
            return

        # 2. Calculate the Discriminant
        d = (b**2) - (4*a*c)
        print(f"\nDiscriminant (D): {d}")

        # 3. Find roots based on the value of D
        if d > 0:
            root1 = (-b + math.sqrt(d)) / (2*a)
            root2 = (-b - math.sqrt(d)) / (2*a)
            print(f"Roots are Real and Different.")
            print(f"Root 1: **{root1:.2f}**")
            print(f"Root 2: **{root2:.2f}**")

        elif d == 0:
            root1 = -b / (2*a)
            print(f"Roots are Real and Same.")
            print(f"Root: **{root1:.2f}**")

        else:
            # Using cmath for complex square root
            root1 = (-b + cmath.sqrt(d)) / (2*a)
            root2 = (-b - cmath.sqrt(d)) / (2*a)
            print(f"Roots are Complex/Imaginary.")
            print(f"Root 1: **{root1}**")
            print(f"Root 2: **{root2}**")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the program
solve_quadratic()
