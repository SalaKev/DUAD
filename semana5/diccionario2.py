first_list = ['Name', 'Role', 'Spaceship']
second_list = ['Isaac Clark', 'Engineer', 'USG Kellion']

data_dictionary = {
    first_list[0] : second_list[0],
    first_list[1] : second_list[1],
    first_list[2] : second_list[2],
}

for datos, valores in data_dictionary.items():
    print(f'{datos}:{valores}')