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


class StudentIteratorMatter2(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter_2, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter3(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter_3, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


# Réponse à la question étape 7 :
# Problème : chaque nouvelle matière oblige à créer un nouvel itérateur ET
# à modifier SchoolClass pour ajouter une nouvelle méthode iter_matter_X.
# On transgresse à nouveau l'OCP dans deux classes simultanément.


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

    def iter_matter_2(self):
        return StudentIteratorMatter2(self.__students)

    def iter_matter_3(self):
        return StudentIteratorMatter3(self.__students)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print('=== Classement Matière 1 (itérateur __iter__) ===')
    for student in school_class:
        print(student)

    print('\n=== Classement Matière 2 (itérateur) ===')
    for student in school_class.iter_matter_2():
        print(student)

    print('\n=== Classement Matière 3 (itérateur) ===')
    for student in school_class.iter_matter_3():
        print(student)