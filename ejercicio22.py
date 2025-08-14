#22- Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9,10]
total = int(reduce(lambda acc, y: acc * y, numeros ))
print(total)