def request_student_info_name():
    print('Please fill the following information')
    while True:
        try:
            name = str(input('Enter the student full name '))
            if not all(c.isalpha() or c.isspace() for c in name):
                raise ValueError('Please use only letters and spaces')
            if name.strip() == '':
                raise ValueError('The name can not be blank')
            return name
        except ValueError as ex:
            print(ex)