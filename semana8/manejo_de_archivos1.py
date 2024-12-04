def open_and_print_canciones(file_path):
    list_to_sort = []
    with open(r'C:\Users\Kevin\progras de lift\Ejercicios entregables\Semana 8 (Manejo de Archivos, CSVs, and JSON)\Manejo de Archivos\Canciones.txt') as file:
        for line in file.readlines():
            list_to_sort.append(line)
    return list_to_sort


def open_and_sort_canciones():
    canciones_sorted = sorted(open_and_print_canciones(r'Canciones.txt'))
    return canciones_sorted


def main(file_path):
    open_and_print_canciones(r'Canciones.txt')
    print(open_and_print_canciones(r'Canciones.txt'))
    canciones_sorted = open_and_sort_canciones()
    new_text = '\n'.join(canciones_sorted)
    with open(r'C:\Users\Kevin\progras de lift\Ejercicios entregables\Semana 8 (Manejo de Archivos, CSVs, and JSON)\Manejo de Archivos\Canciones nuevo', 'a') as file:
        file.write(new_text)
        print(new_text)


main(r'Canciones nuevo.txt')