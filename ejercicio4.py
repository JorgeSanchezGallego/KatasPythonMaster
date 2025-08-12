#4- Genera una función que calcule la diferencia entre 
# los valores de dos listas. Usa la función map().
def diferencias(lista1, lista2):
    """funcion para sacar la diferencia de dos listas

    Args:
        lista1 (list): lista de numeros
        lista2 (list): lista de numeros

    Returns:
        list: lista de numeros diferenciados
    """
    diferencia = list(map(lambda x, y: x-y, lista1, lista2))
    return diferencia
a = [10, 20, 30]
b = [1, 5, 15]
print(diferencias(a,b))