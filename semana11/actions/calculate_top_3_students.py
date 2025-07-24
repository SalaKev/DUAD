def calculate_top_3_students(students):
    if not students:
        print('No student information available.')
        return
    students_with_avg = [(student.name, student.grades['Average'])for student in students]
    students_with_avg.sort(key=lambda student: student[1], reverse=True)
    top_students = students_with_avg[:3]
    print('Top 3 Students:')
    for i, (name, avg) in enumerate(top_students, start=1):
        print(f'{i}. {name} - Average: {avg:.2f}')