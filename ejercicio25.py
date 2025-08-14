#25- Crea una función que cuente el número de caracteres en una cadena de texto dada.
from functools import reduce
texto = "Soy un texto de prueba"
largo = reduce(lambda acc, x: acc + 1, texto, 0)
print(largo)
# reduce aplica la función lambda a cada carácter de 'texto', acumulando el total en 'acc'
# lambda acc, x: acc + 1 → por cada carácter x, suma 1 al acumulador acc
# El 0 al final es el valor inicial de acc