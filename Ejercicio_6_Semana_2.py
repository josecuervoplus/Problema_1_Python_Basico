# El siguiente código elimina los elementos duplicados de una lista.
numbers = [1, 2, 3, 3, 2, 4, 6]
# Se verifica que la lista no esté vacía
if len(numbers)==0:
    print("Error: la lista no puede estar vacía")
else:
    # Se utiliza la función set() para eliminar los elementos duplicados y convertirlo en una lista nuevamente
    no_duplicates = list(set(numbers))
    print(no_duplicates)
