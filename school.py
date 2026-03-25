from collections.abc import Iterable, Iterator


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


# Réponse à la question étape 5 :
# Si on ajoute une nouvelle matière, il faudrait créer une nouvelle méthode
# rank_matter_4 dans SchoolClass, ce qui transgresse le principe Open/Closed (OCP)
# car on modifie une classe existante au lieu de l'étendre.


class StudentIteratorMatter1(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter_1, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class SchoolClass(Iterable):

    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        self.__students.append(student)

    def rank_matter_1(self):
        return sorted(self.__students, key=lambda s: s.matter_1, reverse=True)

    def rank_matter_2(self):
        return sorted(self.__students, key=lambda s: s.matter_2, reverse=True)

    def rank_matter_3(self):
        return sorted(self.__students, key=lambda s: s.matter_3, reverse=True)

    def __iter__(self):
        return StudentIteratorMatter1(self.__students)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print('=== Classement Matière 1 (méthode) ===')
    for student in school_class.rank_matter_1():
        print(student)

    print('\n=== Classement Matière 2 (méthode) ===')
    for student in school_class.rank_matter_2():
        print(student)

    print('\n=== Classement Matière 3 (méthode) ===')
    for student in school_class.rank_matter_3():
        print(student)

    print('\n=== Classement Matière 1 (itérateur __iter__) ===')
    for student in school_class:
        print(student)