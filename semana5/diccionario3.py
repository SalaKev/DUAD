my_list = ['secundario', 'segundo apoyo']

my_team = {
    'primario' : 'Zoro',
    my_list[0] : 'Usopp',
    'primer apoyo' : 'Sanji',
    my_list[1] : 'Nami'
}

deleted_items = my_team.pop(my_list[0]), my_team.pop(my_list[1])
print(my_team)
print(f'Deleted members: {deleted_items}')