# Returns student as tuple, without unpacking it


def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)  # tuple, and can make it immutable


if __name__ == "__main__":
    main()
