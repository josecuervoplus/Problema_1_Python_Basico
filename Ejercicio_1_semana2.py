#1-Solicitar al usuario que ingrese un número
#2-Verificar si el número ingresado es menor que 0
#3-Si el número es menor que 0, imprimir un mensaje de error
#4-Si el número es mayor o igual a 0, calcular el factorial del número
#5-Imprimir el resultado del factorial

# Solicitar al usuario que ingrese un número
num = int(input("Ingrese un número: "))

# Verificar si el número ingresado es menor que 0
if num < 0:
    # Si el número es menor que 0, imprimir un mensaje de error
    print("Error: el número debe ser mayor o igual a 0")
else:
    # Si el número es mayor o igual a 0, calcular el factorial del número
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    # Imprimir el resultado del factorial
    print("El factorial de", num, "es", factorial)
