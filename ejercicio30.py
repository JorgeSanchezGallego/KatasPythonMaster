#30- Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
palabra1 = "Roma"
palabra2 = "Amor"
def anagrama(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())
print(anagrama(palabra1,palabra2))
#Recuerda que sorted ordena alfabeticamente Strings