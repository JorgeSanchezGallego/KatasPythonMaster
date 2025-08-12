#Escribe una función que reciba una lista de números y calcule su promedio.
#Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def promedio(numeros):
    resultado = 0
    suma = 0
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía")
    else:
        for num in numeros:
            
            suma += num
        resultado = suma / len(numeros)
        return f"El promedio es de {resultado}"
try:
    numeros = [1,2,3,4,5,6,7,8,9,10]
    print(f"El promedio es de {promedio(numeros)}")
    
    
    print(promedio([]))
except ListaVaciaError as e:
    print(f"Error: {e}")