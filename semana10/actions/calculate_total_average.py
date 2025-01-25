def calculate_total_average_of_all_the_school(students):
    if not students:
        print('No student information available.')
        return
    total_average = sum(student['grades']['Average'] for student in students)
    general_average = total_average / len(students)
    print(f'The general average of all of the students is {general_average:.2f}')