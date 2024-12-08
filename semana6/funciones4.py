def reversed_string():
    string = 'Las funciones son muy utiles y hacen que el codigo sea mas amigable para leer'
    for i in range(len(string)-1, -1, -1):
        letter = string[i]
        print(letter)


reversed_string()