#2- Dada una lista de números, obtén una nueva lista 
# con el doble de cada valor. Usa la función map().
numeros = [1, 2 , 3, 4, 5, 6]
num_double = list(map(lambda x: x*2, numeros)) # Aplicamos la función lambda que duplica cada número, usando map
print(num_double) # map devuelve un objeto iterable que contiene los valores transformados