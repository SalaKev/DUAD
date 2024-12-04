variable_global = 30

def local_variable():
    variable_local = 55
    print(f'Esta es una variable local y no se puede cambiar desde afuera de esta funcion su valor es {variable_local}')


def global_variable():
    variable_global = 250 
    print(f'Esta es una variable global y si la podemos accesar y hasta cambiar dentro de una funcion, su valor era 30 y ahora el nuevo valor es {variable_global}')


local_variable()
#print(f'No podemos accesar a esta variable {variable_local}')


global_variable()