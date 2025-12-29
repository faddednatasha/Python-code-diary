Program No. : 18
      Program : Calculate aggregate of student marks.

def calculate_student_performance():
    print("--- Student Aggregate & Percentage Calculator ---")
    
    try:
        # 1. Input marks for 5 subjects
        # Assuming maximum marks for each subject is 100
        s1 = float(input("Enter marks for Mathematics: "))
        s2 = float(input("Enter marks for Physics: "))
        s3 = float(input("Enter marks for Chemistry: "))
        s4 = float(input("Enter marks for English: "))
        s5 = float(input("Enter marks for Computer Science: "))

        # 2. Calculate Aggregate (Total Marks)
        aggregate = s1 + s2 + s3 + s4 + s5

        # 3. Calculate Percentage 
        # (Total obtained / Total maximum marks) * 100
        # Total maximum marks = 500 (100 * 5)
        percentage = (aggregate / 500) * 100

        # 4. Display the results
        print("\n--- Performance Report ---")
        print(f"Total Marks (Aggregate): **{aggregate:.2f} / 500.00**")
        print(f"Percentage:             **{percentage:.2f}%**")

        # Basic Result Status
        if percentage >= 40:
            print("Status: PASSED")
        else:
            print("Status: FAILED")

    except ValueError:
        print("Error: Please enter valid numeric marks.")

# Run the program
calculate_student_performance()
