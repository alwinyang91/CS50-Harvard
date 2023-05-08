# Demonstrates a NameError

try:
    x = int(input("What's x? "))  # only try one line of code
except ValueError:
    print("x is not an integer")

print(f"x is {x}")  # if input is not int, then it will broke
