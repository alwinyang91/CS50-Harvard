# Demonstrates defining functions


def main():
    n = get_number()
    meow(n)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")

if __name__ == '__main__':
    main()
