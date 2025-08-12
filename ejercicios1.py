#1- Escribe una función que reciba una cadena de texto como parámetro y 
# devuelva un diccionario con las frecuencias de cada letra en la 
# cadena. Los espacios no deben ser considerados

def contador(palabra):
    """función para contar las letras de nuestra cadena

    Args:
        palabra (str): string o cadena de strings

    Returns:
        diccionario: diccionario con cada letra y su valor
    """
    frecuencias = dict()
    for letra in palabra.replace(" ", ""):
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias
print(contador("caracol y rata"))