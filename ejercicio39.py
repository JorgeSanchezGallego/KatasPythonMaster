#Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") 
# y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math
def calcular_area(figura, datos):
    if figura.lower() == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura.lower() == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    elif figura.lower() == "circulo":
        (radio, ) = datos
        return math.pi * radio**2
    else:
        return "Figura no reconocida"
print("Área rectángulo:", calcular_area("rectangulo", (5, 3)))  
print("Área triángulo:", calcular_area("triangulo", (4, 6)))    
print("Área círculo:", calcular_area("circulo", (2,)))          