hotel_dic = {
    'nombre' : 'Kame House hotel',
    'numero de estrellas' : '7',
    'Habitaciones' :  [{
        'Habitaciones Deluxe' : [{
            'Numero' : 3,
            'Piso' : 3,
            'Precio por noche' : 500000
        },
        {
            'Numero' : 2,
            'Piso' : 3,
            'Precio por noche' : 500000
        },
        {
            'Numero' : 1,
            'Piso' : 3,
            'Precio por noche' : 500000
        }],
        'Habitacion Mid' : [{
            'Numero' : 3,
            'Piso' : 2,
            'Precio por noche' : 250000
        },
        {
            'Numero' : 2,
            'Piso' : 2,
            'Precio por noche' : 250000
        },
        {
            'Numero' : 1,
            'Piso' : 2,
            'Precio por noche' : 250000
        }],
        'Habitacion Regular' : [{
            'Numero' : 1,
            'Piso' : 1,
            'Precio por noche' : 100000
        },
        {
            'Numero' : 1,
            'Piso' : 1,
            'Precio por noche' : 100000
        }]
        
        

    }]
    
    

}

for datos, valores in hotel_dic.items():
    print(f'{datos}:{valores}') 