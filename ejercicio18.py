#18- Escribe un programa en Python que cree una lista de diccionarios con 
# información de estudiantes (nombre, edad, calificación) y use filter 
# para extraer a los estudiantes con una calificación mayor o igual a 90.
estudiantes = [
    {"nombre": "Jorge", "edad": 20, "calificacion": 9.0},
    {"nombre": "Ana", "edad": 22, "calificacion": 8.5},
    {"nombre": "Luis", "edad": 19, "calificacion": 7.8},
    {"nombre": "María", "edad": 21, "calificacion": 9.2}
]
def nota(estudiante): # Función que verifica si la calificación es >= 9
    return estudiante["calificacion"] >= 9.0
matricula = list(filter(nota, estudiantes)) # Filtrar estudiantes con calificación >= 9
print(matricula)