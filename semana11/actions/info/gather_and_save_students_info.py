from actions.info.student_name import request_student_info_name
from actions.info.student_class import request_student_info_class
from actions.info.student_grades import request_student_info_grades

class Student:
    def __init__(self, name, student_class, grades):
        self.name = name
        self.student_class = student_class
        self.grades = grades

def gather_all_students_info():
    student_info = []
    while True:
            name = request_student_info_name()
            student_class = request_student_info_class()
            grades = request_student_info_grades()
            student_info.append(Student(name, student_class, grades))
            while True:
                add_another = input("Do you want to add another student? 1=yes/2=no): ")
                try:
                    if not add_another.isdigit():
                        raise ValueError('Please use only numbers (1 or 2).')
                    add_another = int(add_another)
                    if add_another == 1:
                        break
                    elif add_another == 2:
                        return student_info
                    else:
                        raise ValueError('Please enter a valid option (1 or 2).')
                except ValueError as ex:
                    print(ex)


def save_main_students_information(students):
    all_info_of_students = gather_all_students_info()
    students.extend(all_info_of_students)
    print('Student information added successfully!')