#Genera una función que, al recibir una frase, devuelva una lista 
# con la longitud de cada palabra. Usa la función map().
frase = "esto es una frase"
palabras = frase.split()
longitud_frase = list(map(len, palabras))
print(longitud_frase)