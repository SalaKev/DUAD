print("Ingrese tres numeros y te mostraremos cual es el mayor")
first_number = int(input("Ingres el primer numero: "))
second_number = int(input("Ingres el segundo numero: "))
third_number = int(input("Ingres el tercer numero: "))
if (first_number > second_number and first_number > third_number):
    print(f"El numero mayor es {first_number}")
elif (second_number > first_number and second_number > third_number):
    print(f"El numero mayor es {second_number}")
elif (third_number > first_number and third_number > second_number):
    print(f"El numero mayor es {third_number}")