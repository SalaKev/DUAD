contador = int(1)
suma = int(0)
numero = int(input("Ingrese cualquier numero y te mostraremos el resultado de la suma de todos los numeros, desde el 1 hasta el numero que ingreses "))
while(contador <= numero):
    suma = int(contador + suma)
    contador = contador + 1
print(f"La suma de todos los numeros es {suma}")