# Inicializar una lista de números
numbers = [1, 2, 3]
# Verificar si la lista está vacía
if len(numbers)==0:
    # Si la lista está vacía, imprimir un mensaje de error
    print("Error: la lista no puede estar vacía")
else:
    # Si la lista no está vacía, imprimir la lista original
    print("Lista original:", numbers)
    # Crear una nueva lista con los números elevados al cubo
    numbers_cubed = [x**3 for x in numbers]
    # Imprimir la nueva lista
    print("Lista al cubo:", numbers_cubed)
