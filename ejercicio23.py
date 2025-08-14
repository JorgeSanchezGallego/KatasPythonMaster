#23- Concatena una lista de palabras. Usa la función reduce().
from functools import reduce
palabras = ["Jorge", "Cristina", "Sultan", "Pepe"]
concatena =  reduce(lambda acc, x : acc+" "+x, palabras)
print(concatena)