# Ciudades
import random

ciudades = ["Quito", "Guayaquil", "Cuenca", "Ambato"]

# Días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Semanas
semanas = [1, 2, 3, 4]

# Matriz 3D para almacenar temperaturas
temperaturas = [[[0 for _ in range(len(dias_semana))] for _ in range(len(semanas))] for _ in range(len(ciudades))]

# Llenar la matriz con datos de ejemplo
for ciudad in range(len(ciudades)):
    for semana in range(len(semanas)):
        for dia in range(len(dias_semana)):
            temperaturas[ciudad][semana][dia] = random.randint(20, 40)

# Promedio de temperaturas por ciudad y semana
promedios = [[0 for _ in range(len(semanas))] for _ in range(len(ciudades))]

for ciudad in range(len(ciudades)):
    for semana in range(len(semanas)):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[ciudad][semana][dia]
        promedios[ciudad][semana] = suma_temperaturas / len(dias_semana)

# Mostrar el promedio de temperaturas
for ciudad in range(len(ciudades)):
    print(f"Ciudad: {ciudades[ciudad]}")
    for semana in range(len(semanas)):
        print(f"Semana {semana+1}: {promedios[ciudad][semana]}°C")
    print()
