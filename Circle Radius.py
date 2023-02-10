import math

# Import the math module to access the value of pi

# Calculate area and circ of circle with radius

while True:
    # Prompt the user to enter the radius of the circle
    circle_rad = input("Enter the radius of a circle: ")

    try:
        # Convert the input to a floating-point number
        radius = float(circle_rad)

        # Check if the radius is positive
        if radius > 0:
            # If the radius is positive, exit the loop
            break
        else:
            # If the radius is not positive, display an error message
            print("Please enter a positive number.")
    except ValueError:
        # If the input cannot be converted to a floating-point number, display an error message
        print("Please enter a number.")

# Calculate the area of the circle
area = round((math.pi * radius * radius), 2)

# Calculate the circumference of the circle
circumference = round((2 * math.pi * radius), 2)

# Display the results
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")
