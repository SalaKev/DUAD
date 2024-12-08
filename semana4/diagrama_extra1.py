numero_a = int(input("Ingrese 3 numeros, vamos con el primero "))
numero_b = int(input("Ahora el segundo "))
numebro_c = int(input("Y por ultimo, el tercero "))
if(numero_a == 30):
    print("Correcto! Uno de los 3 numeros debian ser 30 o la suma de los tres debian dar 30 para este resultado")
elif(numero_b == 30):
    print("Correcto! Uno de los 3 numeros debian ser 30 o la suma de los tres debian dar 30 para este resultado")
elif(numebro_c == 30):
    print("Correcto! Uno de los 3 numeros debian ser 30 o la suma de los tres debian dar 30 para este resultado")
elif(numero_a + numero_b + numebro_c == 30):
    print("Correcto! Uno de los 3 numeros debian ser 30 o la suma de los tres debian dar 30 para este resultado")
else:print("Ninguno de los 3 numeros individualmente es 30, ni sumandolos cumple con el parametro, que es dar resultado 30, por favor, reinicia el proceso")