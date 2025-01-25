def show_students_list(students):
    if not students:
        print('No students have been added yet.')
    else:
        print('Here is all the information about the students')
        for i, student in enumerate(students, start=1):
            print(f'Student {i}: {student['name']}, Class {student['class']}')
            for subject, grade in student['grades'].items():
                print(f'{subject}:{grade}')
            print()