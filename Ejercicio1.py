#1. Recibir frase del usuario
#2. Convertir frase a minusculas y eliminar espacios
#3. Comparar frase con su inverso
#4. Si son iguales, imprimir "La frase es un palíndromo."
#5. Si no son iguales, imprimir "La frase no es un palíndromo."


#Función para verificar si una frase es palindrome
def es_palindromo(frase):
    # Convertir la frase a minúsculas
    frase = frase.lower()
    #Remover los espacios
    frase = frase.replace(" ","")
    #Invertir la frase
    inversa = ""
    for letra in frase:
        inversa = letra + inversa
    #Comparar las dos frases
    if inversa == frase:
        return True
    else:
        return False

# pedir la frase al usuario
frase = input("Ingresa una frase: ")

# llamando a la función y verificar si es un palindrome o no
if es_palindromo(frase) == True:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")