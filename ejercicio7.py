#7- Genera una función que convierta una lista de tuplas
#a una lista de strings. Usa la función map().
lista_tuplas = [("soy",), ("una",), ("tupla", "muy", "fea")]
def convertir(list_tuple):
    return list(map(lambda x: " ".join(x), list_tuple))
print(convertir(lista_tuplas))