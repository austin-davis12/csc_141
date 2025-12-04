

name = input("Enter your name: ")

with open("guest.txt", "w") as file:
    file.write(name)

print("Your name has been written to guest.txt.")
