#8- Escribe un programa que pida al usuario dos números e intente dividirlos.
#Si el usuario ingresa un valor no numérico o intenta dividir por cero,
#maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
def division(numA, numB):
    try:
        resultado =  numA / numB 
    except ZeroDivisionError:
        return "No se puede dividir entre 0"
    except TypeError:
        return "Caracter invalido"
    else:
        return f"La division fue exitosa: {resultado}"
try:
    numA = int(input("Dime un numero\n"))
    numB = int(input("Y por cual lo quieres dividir\n"))
except ValueError:
    print("Caracter invalido")
else:    
    print(division(numA, numB))