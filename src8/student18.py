# Adds @property for house


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house  # Note: in order to not confuse Python, 
                            # need to change the attribute name


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"  # to make it works, cancel this line
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


'''
python student18.py
Harry
Gryffindor
'''