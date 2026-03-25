from collections.abc import Iterable, Iterator


def add_matter_4(grade: float):
    """Décorateur de classe qui ajoute la matière 4 à tous les étudiants."""
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, name, matter_1, matter_2, matter_3):
            original_init(self, name, matter_1, matter_2, matter_3)
            self.matter_4 = grade

        cls.__init__ = new_init

        original_str = cls.__str__

        def new_str(self):
            return original_str(self) + f' | M4: {self.matter_4}'

        cls.__str__ = new_str
        return cls
    return decorator


@add_matter_4(grade=15.0)
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


class StudentIteratorMatter4(Iterator):

    def __init__(self, students: list):
        self.__students = sorted(students, key=lambda s: s.matter_4, reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


def add_matter_4_iterator(cls):
    """Décorateur de classe qui ajoute iter_matter_4 à SchoolClass."""
    def iter_matter_4(self):
        return StudentIteratorMatter4(self._SchoolClass__students)
    cls.iter_matter_4 = iter_matter_4
    return cls


@add_matter_4_iterator
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

    print('=== Classement Matière 1 (itérateur) ===')
    for student in school_class:
        print(student)

    print('\n=== Classement Matière 2 (itérateur) ===')
    for student in school_class.iter_matter_2():
        print(student)

    print('\n=== Classement Matière 3 (itérateur) ===')
    for student in school_class.iter_matter_3():
        print(student)

    print('\n=== Classement Matière 4 (itérateur via décorateur) ===')
    for student in school_class.iter_matter_4():
        print(student)