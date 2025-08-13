#16- Escribe una función que tome una cadena de texto y un número entero n 
# como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
texto = "Hola soy una cadena de texto"
palabras_largas = list(filter(lambda word: len(word) > 3, texto.split() ))
print(palabras_largas)