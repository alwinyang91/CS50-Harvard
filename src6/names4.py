# Adds context manager

name = input("What's your name? ")

'''
instead of using:
file = open("names.txt", "a")
'''

# it will automatically closed after file.write executing
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
