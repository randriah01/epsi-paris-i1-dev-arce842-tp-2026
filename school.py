class Student:

    def __init__(self, name: str, matter_1: float, matter_2: float, matter_3: float):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3

    @property
    def average(self):
        return (self.matter_1 + self.matter_2 + self.matter_3) / 3

    def __str__(self):
        return (f'Student {self.name} | M1: {self.matter_1} | M2: {self.matter_2} '
                f'| M3: {self.matter_3} | avg: {self.average:.2f}')


class SchoolClass:

    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        self.__students.append(student)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))