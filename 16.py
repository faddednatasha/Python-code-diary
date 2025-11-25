Program No. : 16
      Program : Calculate gross salary of person

# Define standard allowance rates (as percentages of Basic Salary)
# These values are examples and will vary in real-world scenarios.
DA_PERCENTAGE = 20.0  # Dearness Allowance is 20% of Basic Salary
HRA_PERCENTAGE = 15.0 # House Rent Allowance is 15% of Basic Salary

def calculate_gross_salary():
    """
    Prompts the user for the Basic Salary and calculates Gross Salary 
    using predefined DA and HRA percentages.
    """
    print("--- Gross Salary Calculator ---")
    print(f"Rates Used: DA = {DA_PERCENTAGE}%, HRA = {HRA_PERCENTAGE}% of Basic Salary.")

    # 1. Get the Basic Salary from the user
    try:
        basic_salary_str = input("Enter the Basic Salary amount (P): ")
        basic_salary = float(basic_salary_str)

    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the Basic Salary.")
        return

    if basic_salary < 0:
        print("Error: Basic Salary cannot be negative.")
        return

    # 2. Calculate Allowances
    
    # Calculate Dearness Allowance (DA)
    da = (basic_salary * DA_PERCENTAGE) / 100
    
    # Calculate House Rent Allowance (HRA)
    hra = (basic_salary * HRA_PERCENTAGE) / 100

    # 3. Calculate Gross Salary
    # Gross Salary = Basic + DA + HRA
    gross_salary = basic_salary + da + hra

    # 4. Display the results
    print("\n--- Salary Breakdown ---")
    print(f"Basic Salary:        {basic_salary:10.2f}")
    print(f"Dearness Allowance:  {da:10.2f}")
    print(f"House Rent Allowance:{hra:10.2f}")
    print("---------------------------------")
    print(f"**Gross Salary:** **{gross_salary:10.2f}**")

# Run the function
calculate_gross_salary()
