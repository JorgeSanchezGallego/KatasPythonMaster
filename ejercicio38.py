"""Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente"""
def calificacion (nota_numerica):
    if nota_numerica >= 0 and nota_numerica <= 69:
        print(f"Tu nota {nota_numerica} equivale a un insuficiente")
    elif nota_numerica >= 70 and nota_numerica <= 79:
        print(f"Tu nota {nota_numerica} equivale a un bien")
    elif nota_numerica >= 80 and nota_numerica <= 89:
        print(f"Tu nota {nota_numerica} equivale a un muy bien")
    elif nota_numerica >=90  and nota_numerica <=100:
        print(f"Tu nota {nota_numerica} equivale a un excelente")
    else:
        print("Nota fuera de rango")
calificacion(90)