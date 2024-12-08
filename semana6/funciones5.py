def upper_case_count(string):
    upper_count = 0
    for i in range(0, len(string)):
        letter = string[i]
        if (letter.isupper()):
            upper_count = upper_count + 1
    return(upper_count)


def lower_case_count(string):
    lower_count = 0
    for letter in string:
        if (letter.islower()):
            lower_count = lower_count + 1
    return(lower_count)


def sum_of_all_cases():
    string = 'Las Funciones son muy Utiles y hacen que el Codigo sea mas Amigable para leer'
    print(f'There’s {upper_case_count(string)} upper cases and {lower_case_count(string)} lower cases')


sum_of_all_cases()