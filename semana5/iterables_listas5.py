my_list = []
counter = 1
mayor = 0
while (counter <= 10):
    number = int(input("Ingrese un numero "))
    my_list.append(number)
    if (number > mayor):
        mayor = number
    counter = counter + 1
print(my_list)
print(f'El numero mayor es {mayor}')