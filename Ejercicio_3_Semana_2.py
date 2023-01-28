# Solicitar al usuario que ingrese el primer string
string1 = input("Ingrese el primer string: ")
# Solicitar al usuario que ingrese el segundo string
string2 = input("Ingrese el segundo string: ")
# Verificar si las longitudes de los dos strings son diferentes
if len(string1) != len(string2):
    # Si las longitudes son diferentes, imprimir un mensaje de error
    print("Error: los strings deben tener la misma longitud")
else:
    # Si las longitudes son iguales, inicializar una variable result con un valor vacío
    result = ""
    # Recorrer los caracteres de los dos strings
    for i in range(len(string1)):
        # Concatenar el caracter actual del primer string con el caracter actual del segundo string
        result += string1[i] + string2[i]
    # Imprimir el resultado final
    print(result)
