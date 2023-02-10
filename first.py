import math

# Calculate area and circ of circle with radius

# While loop only lets positive numbers pass
while True:
    circle_rad = input("Enter the radius of a circle: ")
    try:
        radius = float(circle_rad)
        if radius > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a number.")

area = round((math.pi * radius * radius), 2)
circumference = round((2 * math.pi * radius), 2)

print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")
