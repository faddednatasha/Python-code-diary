Program No. : 14
 Program : Calculate Simple Interest & Compound Interest.


def calculate_interests():
    """
    Calculates Simple Interest and Compound Interest based on user input.
    """
    print("--- Interest Rate Calculator (SI & CI) ---")

    # 1. Get user input
    try:
        principal = float(input("Enter the Principal Amount (P): "))
        rate = float(input("Enter the Annual Interest Rate (R in %): "))
        time = float(input("Enter the Time Period (T in years): "))

    except ValueError:
        print("Error: Please enter valid numerical values for all inputs.")
        return

    # Basic input validation
    if principal < 0 or rate < 0 or time < 0:
        print("Error: Principal, Rate, and Time cannot be negative.")
        return

    # --- Calculation 1: Simple Interest (SI) ---
    # Formula: (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    
    # Calculate the total amount for SI
    si_total_amount = principal + simple_interest

    # --- Calculation 2: Compound Interest (CI) ---
    # Formula: P * (1 + R/100)^T - P
    
    # Term 1: (1 + R/100)
    rate_term = 1 + (rate / 100)
    
    # Calculate the total amount for CI (A = P * (1 + R/100)^T)
    ci_total_amount = principal * (rate_term ** time)
    
    # Calculate the compound interest (CI = A - P)
    compound_interest = ci_total_amount - principal


    # 3. Display the results
    print("\n--- Results ---")
    print(f"P = {principal:.2f}, R = {rate:.2f}%, T = {time:.2f} years\n")
    
    print("## 💵 Simple Interest (SI)")
    print(f"Interest Earned (SI): **{simple_interest:.2f}**")
    print(f"Total Amount (P + SI): {si_total_amount:.2f}")

    print("\n## 📈 Compound Interest (CI) - Annually Compounded")
    print(f"Interest Earned (CI): **{compound_interest:.2f}**")
    print(f"Total Amount (A): {ci_total_amount:.2f}")

# Run the function
calculate_interests()
