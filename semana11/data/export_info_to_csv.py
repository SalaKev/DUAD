def process_student_info_for_csv(students):
    processed_students = []
    for student in students:
        student_copy = student.__dict__.copy()
        grades = student_copy.pop('grades')
        for subject, grade in grades.items():
            student_copy[subject] = grade
        processed_students.append(student_copy)
    return processed_students


def export_info_to_csv_file(file_path, students, headers):
    import csv
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(students)
        print('The information was successfully exported!')