Program No. : 8
#Program : Print ASCII value of char input

# Get a single character from the user
user_char = input("Enter a single character: ")

# Check if the user entered exactly one character
if len(user_char) == 1:
    # Get the ASCII value
    ascii_value = ord(user_char)
    print(f"The ASCII value of '{user_char}' is: {ascii_value}")
else:
    print("Error: Please enter only a single character.")
