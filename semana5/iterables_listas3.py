my_list = ['flip', 'Real', 'Plan B', 'Primitive']

if len(my_list) > 1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)