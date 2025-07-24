from actions.info.gather_and_save_students_info import save_main_students_information
from actions.students_list import show_students_list
from actions.calculate_top_3_students import calculate_top_3_students
from actions.calculate_total_average import calculate_total_average_of_all_the_school
from data.export_info_to_csv import export_info_to_csv_file, process_student_info_for_csv
from data.import_info_from_csv import import_info_from_csv_file


def menu():
    students = []
    while True:
        print('Welcome to our students info system, please select an option')
        print('(1) Enter student information')
        print('(2) Check all students information')
        print('(3) Check the top 3 students')
        print('(4) Check the average score among all the students')
        print('(5) Export students info to a CVS file')
        print('(6) Import students from CVS file')
        print('(7) Exit')
        try:
            select_option_number = input('Enter the number ')
            if not select_option_number.isdigit(): 
                raise ValueError('Please use only numbers')
            select_option_number = int(select_option_number)
            if(select_option_number < 1 or select_option_number > 7):
                raise ValueError('Please enter a valid option number.')
            if (select_option_number == 1):
                save_main_students_information(students)
            elif(select_option_number == 2):
                show_students_list(students)
            elif(select_option_number == 3):
                calculate_top_3_students(students)
            elif(select_option_number == 4):
                calculate_total_average_of_all_the_school(students)
            elif(select_option_number == 5):
                if not students:
                    print('No student information available to export.')
                else:
                    processed_students = process_student_info_for_csv(students)
                    export_info_to_csv_file('students.csv', processed_students, processed_students[0].keys())
            elif(select_option_number == 6):
                students_info_imported = import_info_from_csv_file('students.csv')
                students.extend(students_info_imported)
            elif(select_option_number == 7):
                print('Exiting the program. Goodbye!')
                break
            else:
                print('Please select a valid option (1-7).')
        except ValueError as ex:
            print(ex)