#28- Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
numeros = [1,2,3,4,4,5,5,6,7,7]
def primer_duplicado(lista):
   duplicado = set()
   for num in lista:
      if num in duplicado:
         return num
      else:
         duplicado.add(num)
print(primer_duplicado(numeros))
