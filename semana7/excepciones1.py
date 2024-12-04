def suma(entry_number):
    try:
        other_number = int(input())
        return entry_number + other_number
    except ValueError as ex:
        print(f'Ingrese un numero valido (solo numero naturales), se cerrara el programa. Error: {ex}')
        exit()


def resta(entry_number):
    try:
        other_number = int(input())
        return entry_number - other_number
    except ValueError as ex:
        print(f'Ingrese un numero valido (solo numero naturales), se cerrara el programa. Error: {ex}')
        exit()


def multiplicacion(entry_number):
    try:
        other_number = int(input())
        return entry_number * other_number
    except ValueError as ex:
        print(f'Ingrese un numero valido (solo numero naturales), se cerrara el programa. Error: {ex}')
        exit()


def division(entry_number):
    try:
        other_number = int(input())
        return entry_number // other_number
    except ValueError as ex:
        print(f'Ingrese un numero valido (solo numero naturales), se cerrara el programa. Error: {ex}')
        exit()


def erase(entry_number):
    entry_number = 0
    return entry_number


def main():
    entry_number = 0
    decision = int
    base_number = 0
    print('Calculator')
    print(base_number)
    try:
        entry_number = int(input())
        while True:
            try: 
                print('Para sumar elige 1')
                print('Para restar elige 2')
                print('Para multiplicar elige 3')
                print('Para dividir elige 4')
                print('Para borrar resultado o el numero ingresado elige 5')
                print('Para salir elige 6')
                selection = int(input('Que quieres hacer: '))
                if(selection == 1):
                    entry_number = suma(entry_number)
                    print(entry_number)
                elif(selection == 2):
                    entry_number = resta(entry_number)
                    print(entry_number)
                elif(selection == 3):
                    entry_number = multiplicacion(entry_number)
                    print(entry_number)
                elif(selection == 4):
                    entry_number = division(entry_number)
                    print(entry_number)
                elif(selection == 5):
                    entry_number = erase(entry_number)
                    print(entry_number)
                    try:
                        entry_number = int(input())
                    except ValueError as ex:
                        print(f'Ingrese un numero valido (solo numero naturales), se cerrara el programa. Error: {ex}')
                        exit()
                elif(selection == 6):
                    break
                elif(selection != 6 and selection != 5 and selection != 4 and selection != 3 and selection != 2 and selection != 1):
                    raise ValueError()
            except Exception as ex:
                print('No elegiste una opcion valida, se cerrara el programa')
                break
    except ValueError as ex:
        print(f'Ingrese un numero valido (solo numero naturales), se cerrara el programa. Error {ex}')
        
main()