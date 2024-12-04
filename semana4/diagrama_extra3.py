print("Tienes que adivinar un numero del 1 al 10")
my_guess = int(input("Digita el numero que creas correcto: "))
while (my_guess != 4):
    my_guess = int(input("Ese no es el numero, intentalo de nuevo!: "))
print(f"Has adivinado! El numero es {my_guess}")