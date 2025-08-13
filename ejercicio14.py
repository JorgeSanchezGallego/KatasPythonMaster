#14- Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
lista_palabras = ["hola", "adios", "cerveza", "comida", "bar"]
resultado_filtrado = list(filter(lambda word: word.startswith("c"), lista_palabras))# Usamos filter() con una función lambda para quedarnos solo con
                                                                                    # las palabras que empiecen con la letra "a"

print(resultado_filtrado)