#1. Crear una función "es_multiplo_de_cinco" que recibe un número
#2. Convertir el número a una lista de dígitos
#3. Ordenar los dígitos en orden ascendente
#4. Convertir la lista de dígitos a un número
#5. Verificar si el número ordenado es múltiplo de 5
#6. Devolver True o False
#7. Pedir al usuario que ingrese un número entero
#8. Llamar a la función "es_multiplo_de_cinco" con el número ingresado
#9. Imprimir si el número es múltiplo de 5 o no

def es_multiplo_de_cinco(numero):
    # convertir el número a una lista de dígitos
    digitos = [int(d) for d in str(numero)]
    # ordenar los dígitos
    digitos.sort()
    # convertir la lista de dígitos a un número
    numero_ordenado = int("".join(str(d) for d in digitos))
    # verificar si el número ordenado es múltiplo de 5
    return numero_ordenado % 5 == 0

# pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# verificar si el número es múltiplo de 5
if es_multiplo_de_cinco(numero):
    print("El número es múltiplo de 5.")
else:
    print("El número no es múltiplo de 5.")