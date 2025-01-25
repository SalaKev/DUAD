def import_info_from_csv_file(file_path):
    import csv
    students = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                grades = {
                    'Spanish': int(row['Spanish']),
                    'English': int(row['English']),
                    'History': int(row['History']),
                    'Science': int(row['Science']),
                    'Average': float(row['Average'])
                }
                student = {
                    'name': row['name'],
                    'class': row['class'],
                    'grades': grades
                }
                students.append(student)
        print('The information was successfully imported')
        return students
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return []