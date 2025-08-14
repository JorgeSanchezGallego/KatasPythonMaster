#24- Calcula la diferencia total en los valores de una lista. Usa la función reduce().
from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9,10]
diferencia = reduce(lambda acc, x: acc - x,numeros)
print(diferencia)