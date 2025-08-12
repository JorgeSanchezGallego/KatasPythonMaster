#Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas 
# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def letras_mayus_minus(caracteres):
    # Convertimos a set para eliminar duplicados
    letras_unicas = set(caracteres)
    # Usamos map para crear tuplas (mayúscula, minúscula)
    resultado = list(map(lambda c: (c.upper(), c.lower()), letras_unicas))
    return resultado

# Ejemplo
palabra = "Prometeo"
print(letras_mayus_minus(palabra))