#20- Para una lista con elementos de tipo integer y string, 
# obtén una nueva lista solo con los valores int. Usa la función filter().
lista_random = [1, "hola", 3, "adios", 5]
only_numbers = list(filter(lambda x: type(x)== int, lista_random))
print(only_numbers)
# filter() recorre la lista y mantiene solo los elementos que sean enteros
# lambda x: type(x) == int → True si x es un entero