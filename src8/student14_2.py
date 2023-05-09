# Adds __str__


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    # def __str__(self):
    #     return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)  # only print the class


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


'''
python student14_2.py
harry
Gryffindor
'''