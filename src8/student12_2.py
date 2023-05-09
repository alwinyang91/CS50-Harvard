# Adds validation in __init__ using raise
import sys

class Student:
    def __init__(self, name, house):
        if not name:
            sys.exit("Missing name")  # but if we do not want exit the code?
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
