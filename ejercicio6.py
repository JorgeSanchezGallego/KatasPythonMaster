#6- Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(num):
    """funcion para sacar el factorial

    Args:
        num (int): numero entero

    Returns:
        int : resultado factorial
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))