nombre = input("Ingrese su nombre: " )
apellido = input("Ingrese su apellido: " )
edad = int(input("Ahora ingrese su edad: "))
if (edad <= 4):
    print("Eres un bebé")
elif (edad > 4 and edad <= 11):
    print("Eres un niño")
elif (edad > 11 and edad <= 15):
    print("Eres un preadolescente")
elif (edad > 15 and edad <= 17):
    print("Eres un adolescente")
elif (edad > 17 and edad <= 35):
    print("Eres un adulto joven")
elif (edad > 35 and edad <= 65):
    print("Eres un adulto")
elif (edad > 65 and edad <= 100):
    print("Eres un adulto mayor")