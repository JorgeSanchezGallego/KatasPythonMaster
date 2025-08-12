#Escribe un programa que pida al usuario que introduzca su edad.
#  Si el usuario ingresa un valor no numérico o un valor fuera del 
# rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
class FueraDeRango(Exception):
    pass
try:
    edad = int(input("Cual es tu edad?\n"))
    if edad < 0 or edad > 120:
        raise FueraDeRango("Edad fuera de rango")
except ValueError:
    print("Caracter invalido")
except FueraDeRango as e:
    print(e)
else:
    print(f"Tu edad es: {edad}")