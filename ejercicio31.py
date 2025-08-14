#31- Crea una función que solicite al usuario ingresar una lista de nombres y 
#luego un nombre para buscar en esa lista. Si el nombre está en la lista,
#imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
class MiError(Exception):
    pass
nombres = ["Pepe", "Cristina", "Jorge", "Sultan"]
nombre_buscado = "Antonio"
def segurata(lista, nombre):
    if nombre in lista:
        print("Estás en la lista, pasa")
    else:
        raise MiError("No estás en la lista, fuera")
try:
    segurata(nombres,nombre_buscado)
except MiError as e:
    print(e)