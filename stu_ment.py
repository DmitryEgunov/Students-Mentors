class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectur(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average(self.grades)}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}"""
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return average(self.grades) < average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        text = f"""Имя: {self.name} 
Фамилия: {self.surname}"""
        return text


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        text = f"""Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {average(self.grades)}"""
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return average(self.grades) < average(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"""Имя: {self.name} 
Фамилия: {self.surname}"""
        return text


def average(grade):
    averages = 0
    for grade_ in grade:
        averages += sum(grade[grade_]) / len(grade[grade_])
        return round(averages, 1)


def compare():
    while True:
        user_input = input("\033[32m{}".format("""Для сравнения лекторов по средней оценке за лекции, введите : l
Для сравнения студентов по средней оценке за домашние задания, введите : s 
Для выхода из режима сравнения, введите : q\n\033[0m"""))
        if user_input == 'l':
            print(sum_lecturer1 < sum_lecturer2, 'sum_lecturer1 < sum_lecturer2')
        elif user_input == 's':
            print(sum_student1 > sum_student2, 'sum_student1 > sum_student2')
        elif user_input == 'q':
            break
        else:
            print("\033[31m{}".format('Введена неверная команда, попробуйте снова.\033[0m'))
            continue


def students_average(students, course):
    ave_cour = []
    i = 0
    while i < len(students):
        if isinstance(students[i], Student) and course in students[i].courses_in_progress:
            ave_cour += (students[i].grades[course])
            i += 1
    return round(sum(ave_cour) / len(ave_cour), 1)


def lecturers_average(lecturers, course):
    ave_cour = []
    i = 0
    while i < len(lecturers):
        if isinstance(lecturers[i], Lecturer) and course in lecturers[i].courses_attached:
            ave_cour += (lecturers[i].grades[course])
            i += 1
    return round(sum(ave_cour) / len(ave_cour), 1)


sum_reviewer1 = Reviewer('Some', 'Buddy')
sum_reviewer1.courses_attached += ['Python, Git']
sum_reviewer2 = Reviewer('Jack', 'Thunder')
sum_reviewer2.courses_attached += ['Python, Git']

sum_lecturer1 = Lecturer('Sume', 'Buddy')
sum_lecturer1.courses_attached += ['Python, Git']
sum_lecturer2 = Lecturer('Jack', 'Thunder')
sum_lecturer2.courses_attached += ['Python, Git']
lecturer_list = [sum_lecturer1, sum_lecturer2]

sum_student1 = Student('Ruoy', 'Eman', 'your_gender')
sum_student1.courses_in_progress += ['Python, Git']
sum_student1.finished_courses += ['Введение в программирование']
sum_student2 = Student('Billy', 'Boy', 'your_gender')
sum_student2.courses_in_progress += ['Python, Git']
sum_student2.finished_courses += ['Введение в программирование']
student_list = [sum_student1, sum_student2]

sum_student1.rate_lectur(sum_lecturer1, 'Python, Git', 9.2)
sum_student1.rate_lectur(sum_lecturer1, 'Python, Git', 9.8)
sum_student2.rate_lectur(sum_lecturer2, 'Python, Git', 10)
sum_student2.rate_lectur(sum_lecturer2, 'Python, Git', 10)
sum_reviewer1.rate_hw(sum_student1, 'Python, Git', 9.5)
sum_reviewer1.rate_hw(sum_student1, 'Python, Git', 9.3)
sum_reviewer2.rate_hw(sum_student2, 'Python, Git', 9.9)
sum_reviewer2.rate_hw(sum_student2, 'Python, Git', 9.5)


print("\033[31m{}".format(f'Reviewers:\033[0m \n{sum_reviewer1} \n\n{sum_reviewer2} \n'))

print("\033[34m{}".format(f'Lecturers:\033[0m \n{sum_lecturer1} \n\n{sum_lecturer2} \n'))

print("\033[33m{}".format(f'Students:\033[0m \n{sum_student1} \n\n{sum_student2} \n'))

compare()
print(sum_lecturer1 > sum_lecturer2, 'sum_lecturer1 > sum_lecturer2')
print(sum_student1 < sum_student2, 'sum_student1 > sum_student2')

print(f'Средняя оценка всех студентов по курсу "Python, Git": {students_average(student_list, "Python, Git")}')
print(f'Средняя оценка всех лекторов за лекции по курсу "Python, Git": {lecturers_average(lecturer_list, "Python, Git")}')

