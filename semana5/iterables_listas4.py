my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in range(len(my_list)-1, -1, -1):
    number = my_list[i]
    if number % 2 != 0:
        delete_item = my_list.pop(i)
print(my_list)