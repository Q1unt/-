class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student = []

    def rate_lecturer(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        sum_ = 0
        counter = 0
        for values in self.grades.values():
            for i in values:
                sum_ += i
                counter += 1
        return round(sum_ / counter)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка:{self.average_rating()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached = []
        self.grades = {}

    def average_rating(self):
        sum_ = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                sum_ += i
                counter += 1
        return round(sum_ / counter)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка:{self.average_rating()}'
        return res


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def average_student_grades(student_list, course):
    list_ = []
    for student in student_list:
        for key, values in student.grades.items():
            if course in key:
                list_.extend(values)
    return sum(list_) / len(list_)

def average_Lecturer_grades(Lecturer, course):
    list_ = []
    for Lecturer1 in Lecturer:
        list_.extend(Lecturer1.grades[course])
    return sum(list_) / len(list_)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress +=['Git']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Dima', 'Иванов', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress +=['Git']
second_student.finished_courses += ['Введение в программирование']


best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached +=['Git']

second_lecturer = Lecturer('sergey', 'elay')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached +=['Git']


cool_Reviewer = Reviewer('Антон', 'Шахов')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached +=['Git']

best_student.rate_lecturer(second_lecturer, 'Python', 6)
best_student.rate_lecturer(second_lecturer, 'Python', 7)
best_student.rate_lecturer(second_lecturer, 'Python', 6)

best_student.rate_lecturer(best_lecturer, 'Git', 10)
best_student.rate_lecturer(best_lecturer, 'Git', 10)
best_student.rate_lecturer(best_lecturer, 'Git', 10)

best_student.rate_lecturer(best_lecturer, 'Python', 6)
best_student.rate_lecturer(best_lecturer, 'Python', 7)
best_student.rate_lecturer(best_lecturer, 'Python', 7)


cool_Reviewer.rate_hw(best_student, 'Python', 6)
cool_Reviewer.rate_hw(best_student, 'Python', 6)
cool_Reviewer.rate_hw(best_student, 'Python', 6)

cool_Reviewer.rate_hw(best_student, 'Git', 9)
cool_Reviewer.rate_hw(best_student, 'Git', 9)
cool_Reviewer.rate_hw(best_student, 'Git', 9)

cool_Reviewer.rate_hw(second_student, 'Python', 9)
cool_Reviewer.rate_hw(second_student, 'Python', 9)
cool_Reviewer.rate_hw(second_student, 'Python', 9)

print(f'оценивают студенты {best_lecturer.grades}')
print(f'оценивают эксперты {best_student.grades}')
print(cool_Reviewer)
print(best_lecturer)
print(best_student)
print(second_student)
print(best_student < second_student)
print(best_student > second_student)
print(best_lecturer > second_lecturer)
print (average_student_grades([best_student,second_student], 'Python'))
print(average_Lecturer_grades([best_lecturer,second_lecturer],'Python'))
