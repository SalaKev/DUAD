def sum_of_numbers():
    suma = 0
    list_of_numbers = [35, 78, 92, 46, 123]
    for i in range(0, len(list_of_numbers)):
        suma = list_of_numbers[i] + suma

    return(suma)


print('El resultado de la suma es')
print(sum_of_numbers()) 