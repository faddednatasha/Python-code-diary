Program No. : 20
      Program : Program to separate decimal and integer part of given floating point number.

import math

def separate_parts_modf():
    num = float(input("Enter a floating point number: "))
    
    # math.modf returns (fractional_part, integer_part)
    fractional, integer = math.modf(num)
    
    print(f"\n--- Method: math.modf ---")
    print(f"Original Number: {num}")
    print(f"Integer Part: {int(integer)}")
    print(f"Decimal Part: {fractional}")

separate_parts_modf()
