# Appends to a file

name = input("What's your name? ")

file = open("names.txt", "a")  # Appends to a file, then it can store multiple names
file.write(f"{name}\n")
file.close()
