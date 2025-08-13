#15- Crea una función lambda que sume 3 a cada número de una lista dada.
numeros = [1,2,3,4,5,6,7]
numeros3 = list(map(lambda numero: numero + 3, numeros))
print(numeros3)