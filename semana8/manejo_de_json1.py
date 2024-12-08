import json


def read_file_save_info (path):
    try:
        with open(r'C:\Users\Kevin\progras de lift\Ejercicios entregables\Semana 8 (Manejo de Archivos, CSVs, and JSON)\Manejo de JSON\pokemones.json', 'r', encoding='utf-8') as file:
            file_content = file.read()
            if not file_content.strip():  # Si el archivo está vacío
                return []
            py_dict = json.loads(file_content)
            return py_dict
    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido. Iniciando con una lista vacía.")
        return []
    except FileNotFoundError:
        print(f"El archivo '{path}' no se encontró. Creando una lista vacía.")
        return []


def requesting_new_pokemon_info():
    name = str(input('Ingrese el nombe del nuevo Pokemon: '))
    t_ype = str(input('Ingrese su tipo: '))
    hp = int(input('Ingrese sus puntos de HP: '))
    attack = int(input('Ingrese sus puntos de Ataque: '))
    defense = int(input('Ingrese sus puntos de Defensa: '))
    sp_attack = int(input('Ingrese sus SP. de Ataque: '))
    sp_defense = int(input('Ingrese sus SP. de Defensa: '))
    speed = int(input('Ingrese sus puntos de Velocidad: '))
    new_pokemon_list = {
    "name": {
        "english": name
        },
    "type": [
        t_ype
        ],
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
        }
    }
    return new_pokemon_list


def main():
    counter = 1
    number_of_entries = 0
    py_dict = read_file_save_info (r'pokemones.json')
    print(py_dict)
    number_of_entries = int(input('Cuantos Pokemones deseas ingresar? '))
    while (counter <= number_of_entries):
        new_pokemon = requesting_new_pokemon_info()
        py_dict.append(new_pokemon)
        counter = counter + 1
    new_json = json.dumps(py_dict, indent=4)
    print(new_json)
    with open(r'C:\Users\Kevin\progras de lift\Ejercicios entregables\Semana 8 (Manejo de Archivos, CSVs, and JSON)\Manejo de JSON\pokemones.json', 'w', encoding='utf-8') as file:
        new_file = file.write(new_json)


main()