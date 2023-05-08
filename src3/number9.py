# Adds prompt


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


# make the function more reuseable
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")


if __name__ == "__main__":
    main()

