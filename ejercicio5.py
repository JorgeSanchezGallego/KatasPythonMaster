#5- Escribe una función que tome una lista de números como parámetro y
#un valor opcional nota_aprobado (por defecto 5). La función debe 
#calcular la media de los números en la lista y determinar si la media
#es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado";
#de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def media(numeros, nota_aprobado = 5):
    """funcion para ver si esta aprobado o no

    Args:
        numeros (list): lista de numeros
        nota_aprobado (int): entero opcional. Defaults to 5.

    Returns:
        tuple: tupla con la media y el estado
    """
    suma_notas = 0
    
    for numero in numeros:
        suma_notas += numero
    media_notas = suma_notas / len(numeros)
    if media_notas >= nota_aprobado:
        tupla_final = (media_notas, "aprobado")
    else:
        tupla_final = (media_notas, "suspenso")
    return tupla_final
notas = [5,6,3,6,5,10]
print(media(notas))
