#3- Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
#La función debe devolver una lista con todas las palabras 
#de la lista original que contengan la palabra objetivo.
def frase_objetivo(palabras, palabra_buscada):
    """funcion para generar una lista con las coincidencias

    Args:
        palabras (list): lista de palabras
        palabra_buscada (str): caracteres buscados a coincidir

    Returns:
        _type_: lista de palabras coincidentes
    """
    resultado = [palabra for palabra in palabras if palabra_buscada in palabra]
    return resultado
lista_palabras = ["perro", "gato", "pez", "loro"]
print(frase_objetivo(lista_palabras, "a"))