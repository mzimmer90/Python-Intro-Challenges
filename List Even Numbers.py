# Start an infinite loop

while True:
    # Get user input and store it as a string
    user_number = input("Enter a number between 1 and 100: ")

    # Try to convert the string into an integer
    try:
        num = int(user_number)

        # Check if the number is between 1 and 100
        if 1 <= num <= 100:
            # If true, exit loop
            break
        else:
            # If false, print an error message
            print("Please enter a number between 1 and 100.")
    except ValueError:
        # If the string cannot be converted into an integer, print an error message
        print("Please enter a number.")

# Print a message indicating the even numbers between 0 and the user's number
print(f"The even numbers between 0 and {user_number} are:")

# Loop through the range from 0 to the user's number
# (need num + 1 because loop would stop before user number), incrementing by 2, meaning even numbers
for i in range(0, num + 1, 2):
    # Print each even number
    print(i)
