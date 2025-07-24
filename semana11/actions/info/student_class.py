def request_student_info_class():
    while True:
        while True:
            try:
                class_num = input('Enter the student class number (from 1 to 3) ')
                if not class_num.isdigit(): 
                    raise ValueError('Please use only numbers')
                class_num = int(class_num)
                if(class_num < 1 or class_num > 3):
                    raise ValueError('Please enter a number between 1 and 3.')
                break
            except ValueError as ex:
                print(ex)
        while  True:
            try:
                class_letter = input('Enter the student class letter (from A to B in caps)')
                if not class_letter.isalpha(): 
                    raise ValueError('Please use only the letters')
                if class_letter not in ['A', 'B', 'C']:
                    raise ValueError('Please enter a valid letter (A, B, or C) must be on caps.')
                break
            except ValueError as ex:
                print(ex) 
        return f'{class_num}{class_letter}'