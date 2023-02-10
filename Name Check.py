name = input("Please enter a name: ").lower()
name_length = len(name)
print("Your name is", name_length, "characters long.")

repeats = []
for i in name:
    if name.count(i) > 1:
        if i not in repeats:
            repeats.append(i)

if len(repeats) > 0:
    print("The following letters repeat:", ', '.join(repeats))
else:
    print("No letters repeat.")
