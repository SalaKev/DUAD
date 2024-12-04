def orden_alfabetico():
    my_string = 'wheels-truck-deck-griptape-screws'
    words = my_string.split('-')
    sorted_list = sorted(words)
    final_list = '-'.join(sorted_list)
    return(final_list)


print(orden_alfabetico())