entries = []

user_num = int(input("Enter number of entries: "))
while user_num <= 0:
    print("Cannot enter anything equal or less than 0. Try again.")
    user_num = int(input("Enter number of entries: "))

for i in range(1, user_num + 1):
    print(f"Write for entry #{i}:")
    user_entry = input("")
    entries.append(user_entry)

print("All entries created!")
user_opt = input("View entries?(yes/no) ")
while (user_opt != "yes"):
    if user_opt == "no":
        break
    else:
        user_opt = input("Try again ")

if user_opt == "yes":
    while user_opt != "quit":
        user_opt = input(f"Choose entry (#1 - {i})('quit' to exit): ")
        if user_opt == "quit":
            break
        elif (int(user_opt) > i) or (int(user_opt) <= 0):
            print("Choosen entry doesn't exist")
        else:   
            entry_choice = entries[int(user_opt) - 1]
            print(entry_choice)

print("End of program. See ya later!")
