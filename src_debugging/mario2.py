

def main():
    height = int(input("Height: "))
    pyramind(height)

def pyramind(n):
    for i in range(n):
        print("#" * i+1)


if __name__ == "__main__":
    main()