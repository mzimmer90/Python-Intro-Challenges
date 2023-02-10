while True:
    user_number = input("Enter a number to check if it's odd or even: ")
    try:
        num = int(user_number)
        break
    except ValueError:
        print("Please enter a valid whole number.")

even_check = num % 2

if not even_check:
    print("Your number is even")
else:
    print("Your number is odd")
