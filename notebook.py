entries = []

user_num = int(input("Enter number of entries: "))
while user_num <= 0:
    print("Cannot enter anything equal or less than 0. Try again.")
    user_num = int(input("Enter number of entries: "))

for i in range(1, user_num + 1):
    print(f"Write for entry #{i}:")
    user_entry = input("")
    entries.append(user_entry)
print(entries)