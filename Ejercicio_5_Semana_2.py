# Se crea un diccionario de ejemplo con información de un estudiante
Dicionario_Notas = {
    "clase": {
        "estudiante": {
            "nombre": "Mike",
            "calificaciones": {
                "física": 70,
                "historia": 80,
                "matemáticas": 90
            },
        }
    }
}

# Se accede al nombre del estudiante y al diccionario de calificaciones
nombre = Dicionario_Notas["clase"]["estudiante"]["nombre"]
calificaciones = Dicionario_Notas["clase"]["estudiante"]["calificaciones"]

# Se inicializan variables para almacenar la suma de las calificaciones y el número de calificaciones
total = 0
cuenta = 0

# Se recorre el diccionario de calificaciones y se suman las calificaciones y se cuentan
for key, value in calificaciones.items():
    total += value
    cuenta += 1

# Se calcula el promedio de las calificaciones
promedio = total / cuenta

# Se imprime un diccionario con el nombre del estudiante y su promedio
print({"nombre": nombre, "promedio": promedio})
