# Initialize an empty list to store names
names = []

# Get user to enter amount of names to be added
list_length = int(input("How many names would you like to add? "))

# Loop for the amount of names
for i in range(list_length):
    # Get a name from the user and store it as a string
    name = input(f"Enter your {i + 1} name: ")

    # Check if the name contains only letters
    while not name.isalpha():
        # If not, print an error message
        print("Please enter a name only containing letters.")
        # Get the name again from the user
        name = input(f"Enter your {i + 1} name: ")

    # Add the name to the list
    names.append(name)

# Print the names separated by commas
print("The names you entered were:", ', '.join(names))

# Old code which printed each name individually in separate lines
# for i in range(list_length):
#     print(names[i])
