class Student:
    def __init__(self, name, surname, gender):
        self._grades_list = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _midgrade(self):
        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
            if len(grades_list) == 0:
                self.midgrade = 0
            else:
                self.midgrade = sum(grades_list) / len(grades_list)
            return self.midgrade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._midgrade()}\n' 
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' 
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self,other):
        if isinstance(other, Student):
            return self.midgrade < other.midgrade
        else:
            return 'Ошибка!'

    def lect_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses):
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviwer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.courses_grades = {}

    def _midgrade(self):
        grades_list = []
        for grades in self.courses_grades.values():
            for grade in grades:
                grades_list.append(grade)
        if len(grades_list) == 0:
            self.midgrade = 0
        else:
            self.midgrade = sum(grades_list) / len(grades_list)
        return self.midgrade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._midgrade()}\n'

    def __lt__(self,other):
        if isinstance(other, Lecturer):
            return self.midgrade < other.midgrade
        else:
            return 'Ошибка!'


student1 = Student('Jim', 'Hopkins', 'male')
student1.courses_in_progress = ['Math', 'Chemistry', 'Python']
student1.finished_courses = ['SQL', 'Java']


student2 = Student('Tom', 'Smith', 'male')
student2.courses_in_progress = ['Math', 'Chemistry', 'Python', 'SQL']
student2.finished_courses = ['Java']


lecturer1 = Lecturer('Antony', 'Black')
lecturer1.courses = ['SQL', 'Chemistry']


lecturer2 = Lecturer('Steve', 'Wonder')
lecturer2.courses = ['Math', 'Python', 'Java']


reviwer1 = Reviwer('Josh', 'McDerton')
reviwer1.courses_attached = ['Math', 'Chemistry',]
reviwer1.rate_hw(student2,'Math', 10)
reviwer1.rate_hw(student2,'Math', 3)
reviwer1.rate_hw(student2,'Chemistry', 8)
reviwer1.rate_hw(student1,'Math', 7)
reviwer1.rate_hw(student1,'Math', 4)
reviwer1.rate_hw(student1,'Chemistry', 6)
reviwer2 = Reviwer('Travis', 'Rice')
reviwer2.courses_attached = ['Python', 'SQL', 'Java']


student1.lect_rate(lecturer1,'SQL', 7)
student2.lect_rate(lecturer1,'SQL', 5)
student1.lect_rate(lecturer2,'Math', 3)
student2.lect_rate(lecturer2,'Math', 10)


print(reviwer1)
print(reviwer2)

print(lecturer1)
print(lecturer2)

print(student1)
print(student2)

print(student1 > student2)

print(lecturer2 > lecturer1)

students_list = [student1,student2]
lecturers_list = [lecturer2,lecturer1]
courses = ['SQL', 'Math', 'Python', 'Chemistry', 'Java']


def student_midgrades(students, course):
    all_course_grades = []
    for student in students:
        for grade in student.grades.get(course):
            all_course_grades += [grade]
    mid_grade = sum(all_course_grades) / len(all_course_grades)
    print(f'Средняя оценка за курс {course}: {mid_grade}')


def lecturer_midgrades(lecturers, course):
    all_course_grades = []
    for lecturer in lecturers:
        for grade in lecturer.grades.get(course):
            all_course_grades += [grade]
    mid_grade = sum(all_course_grades) / len(all_course_grades)
    print(f'Средняя оценка за курс {course}: {mid_grade}')


student_midgrades(students_list,courses[1])
lecturer_midgrades(students_list,courses[3])
