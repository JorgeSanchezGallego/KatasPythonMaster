#27- Crea una función que calcule el promedio de una lista de números.
from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9,10]
promedio = (lambda lista : reduce(lambda acc, x: acc + x,lista)/ len(lista))(numeros)  
print(promedio)
# Lambda externa que recibe la lista como parámetro
# Suma todos los elementos de la lista usando reduce
# Divide la suma total entre la cantidad de elementos
# Llama a la lambda pasando la lista 'numeros'