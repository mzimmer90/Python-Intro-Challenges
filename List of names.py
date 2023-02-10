names = []
list_length = int(input("How many names would you like to add? "))
for i in range(list_length):
    name = input(f"Enter your {i+1} name: ")
    while not name.isalpha():
        print("Please enter a name only containing letters.")
        name = input(f"Enter your {i + 1} name: ")
    names.append(name)

print("The names you entered were:", ', '.join(names))
# for i in range(list_length):
#     print(names[i])
