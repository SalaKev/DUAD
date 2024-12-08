respuesta = str("Si")
resultado = str
while(respuesta == "Si"):
    numero = int(input("Ingrese un numero que sea divisible entre 3, 5 o ambos "))
    if(numero % 15 == 0):
        resultado = "FizzBuzz"
        print(f"El resultado es {resultado}")
    elif(numero % 5 == 0):
        resultado = "Buzz"
        print(f"El resultado es {resultado}")
    elif(numero % 3 == 0):
        resultado = "Fizz"
        print(f"El resultado es {resultado}")
    respuesta = str(input("Quieres averiguar otro resultado? Digita Si o No "))