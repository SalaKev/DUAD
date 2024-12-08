tiempo_en_segundos = int(input("Ingrese el tiempo en segundos para saber si es mayor a 10 minutos, si no lo es, te mostraremos por cuantos segundos te hizo falta para al menos llegar a los 10 minutos "))
if(tiempo_en_segundos > 600):
    segundos_de_mas = int(tiempo_en_segundos - 600)
    print(f"!!El tiempo ingresado supero los 10 minutos por {segundos_de_mas} segundos!!")
else: segundos_faltantes = int(600 - tiempo_en_segundos); print(f"Para llegar a 10 minutos te hicieron falta los siguientes segundos {segundos_faltantes}")