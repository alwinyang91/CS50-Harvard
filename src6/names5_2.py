# Reads from a file

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)  # it will have extra lines
