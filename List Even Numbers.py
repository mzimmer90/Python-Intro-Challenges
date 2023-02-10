while True:
    user_number = input("Enter a number between 1 and 100: ")
    try:
        num = int(user_number)
        if 1 <= num <= 100:
            break
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Please enter a number.")

print(f"The even numbers between 0 and {user_number} are:")
for i in range(0, num + 1, 2):
    print(i)
