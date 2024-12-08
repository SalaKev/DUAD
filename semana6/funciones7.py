def verificar_numero_primo():
    complete_list = [5, 4, 7, 29, 56, 47, 13]
    new_list = []
    
    for number in complete_list:
        if number > 1:  
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                new_list.append(number)
    
    return new_list


print(verificar_numero_primo())