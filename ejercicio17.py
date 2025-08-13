#17- Crea una función que tome una lista de dígitos y 
# devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
from functools import reduce
numeros = [8,4,3,5]
num = reduce(lambda acc, n: acc*10 + n, numeros)
# reduce() aplica la lambda acumulando el resultado
# acc es el acumulador, n es el dígito actual
# acc*10 "desplaza" los dígitos a la izquierda y sumamos el nuevo
print(num)