# Calculadora - Manual de usuario

#Este programa es una calculadora que permite realizar operaciones aritméticas básicas como suma, resta, multiplicación, división, factorial y potencia.

## Uso

#1. Ejecute el programa para iniciar la calculadora.

#2. Se le pedirá que ingrese la operación que desea realizar. Puede elegir entre las siguientes opciones:
#   * Suma: ingrese '+'
#  * Resta: ingrese '-'
#   * Multiplicación: ingrese 'x'
#   * División: ingrese '/'
#   * Factorial: ingrese '2x'
#   * Potencia: ingrese 'xx'
#   * Salir: ingrese 'salir'

#3. Después de elegir la operación, se le pedirá que ingrese los números para la operación, separados por comas.

#4. El programa calculará el resultado y lo imprimirá en pantalla. También se guardará en un archivo de texto llamado 'calculator_history.txt' en el mismo directorio que el programa.

## Notas

#- Asegúrese de ingresar los números y la operación correctamente, ya que el programa no realizará comprobaciones adicionales.
#- Si ingresa una operación inválida, el programa imprimirá un mensaje de error.
#- El archivo 'calculator_history.txt' se actualiza cada vez que se realiza una operación y se guarda en el mismo directorio que el programa.


import math

# Primero se definen las funciones necesarias para el programa

# Función de suma
def suma(*args):
    result = 0
    for i in args:
        result += i
    return result

# Función de resta
def resta(a, b):
    return a - b

# Función de multiplicación
def multiplicacion(*args):
    result = 1
    for i in args:
        result *= i
    return result

# Función de división
def division(a, b):
    return a / b

# Función de factoriales
def factorial(a):
    return math.factorial(a)

# Función de potencias
def potencia(a, b):
    return a ** b

# Se crea una lista con las operaciones necesarias
# Para que el programa funcione, el usuario debe ingresar los siguientes caracteres
operations = {
    '+': suma,
    '-': resta,
    'x': multiplicacion,
    '/': division,
    '2x': factorial,
    'xx': potencia
}

# Se crea un ciclo con las funciones según lo que el usuario ingrese con los caracteres ingresados
def calculate():
    while True:
        # Pide al usuario la operación a realizar
        operation = input('Ingrese la operación que desea realizar (+, -, x, /, 2x, xx, salir): ')
        if operation == 'salir':
            # Salir del ciclo y terminar el programa
            break
        elif operation in operations:
            # Pide al usuario los números para la operación
            params = input('Ingrese los numeros separados por comas: ')
            # Convierte la cadena de entrada en una lista de números
            params = [int(i) for i in params.split(',')]
            # Ejecuta la operación y almacena el resultado
            result = operations[operation](*params)
            # Guarda el resultado en un archivo de texto
            with open('calculator_history.txt', 'a') as file:
                file.write(f'{operation}: {params} = {result}\n')
            # Imprime el resultado
            print('Resultado:', result)
        else:
            # Mensaje para operación inválida
            print('Operación no válida')

if __name__ == '__main__':
    # Llamada a la función principal
    calculate()