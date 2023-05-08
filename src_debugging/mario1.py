

def main():
    height = int(input("Height: "))
    pyramind(height)

def pyramind(n):
    for i in range(n):
        print(i, end=" ")  # to debug, pre-print
        print("#" * i)


if __name__ == "__main__":
    main()