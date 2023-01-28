# Se utiliza un ciclo while infinito para que el usuario pueda intentar ingresar un número válido hasta que lo haga
while True:
    try:
        # Solicitar al usuario que ingrese un número
        num = int(input("Ingrese un número: "))
        # Verificar si el número ingresado es menor o igual a 0
        if num <= 0:
            # Si el número es menor o igual a 0, imprimir un mensaje de error
            print("Error: el número debe ser mayor a 0")
        else:
            # Si el número es mayor a 0, imprimir una serie de números
            # en forma de triangulo 
            for i in range(1, num+1):
                for j in range(1, i+1):
                    print(j, end=" ")
                print()
            break # Se sale del ciclo while
    except ValueError:
        # Si se genera una excepción ValueError, se imprime un mensaje de error
        # indicando que debe ingresar un número
        print("Error: debe ingresar un número")
