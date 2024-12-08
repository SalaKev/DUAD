import csv

games_list = [
    {
        'nombre':'Infamous',
        'genero':'open-world action-adventure',
        'desarrollador':'Sucker Punch',
        'clasificacion':'E-M'
    },
    {
        'nombre':'God of War',
        'genero':'hack and slash',
        'desarrollador':'Santa Monica',
        'clasificacion':'M'
    },
    {
        'nombre':'Crash Bandicoot',
        'genero':'Platform',
        'desarrollador':'Naughty Dog',
        'clasificacion':'E'
    },
    {
        'nombre':'Dead Space',
        'genero':'Survival Horror',
        'desarrollador':'Visceral Games',
        'clasificacion':'M'
    },
]


def write_csv_games(file_path, games, headers):
    with open(r'C:\Users\Kevin\progras de lift\Ejercicios entregables\Semana 8 (Manejo de Archivos, CSVs, and JSON)\Manejo de CSVs\games', 'w') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        
        writer.writerows(games)


write_csv_games('games.csv', games_list, games_list[0].keys())