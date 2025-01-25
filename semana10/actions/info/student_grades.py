def validate_grade(subject):
    while True:
        try:
            grade = input(f'Enter your {subject} grade (from 0 to 100): ')
            if not grade.isdigit():
                raise ValueError('Please use only numbers.')
            grade = int(grade)
            if grade < 0 or grade > 100:
                raise ValueError('Please enter a number between 0 and 100.')
            return grade
        except ValueError as ex:
            print(ex)


def request_student_info_grades():
    subjects = ['Spanish', 'English', 'History', 'Science']
    grades = {}
    for subject in subjects:
        grades[subject] = validate_grade(subject)
    average = sum(grades.values()) / len(grades)
    grades['Average'] = average
    return grades