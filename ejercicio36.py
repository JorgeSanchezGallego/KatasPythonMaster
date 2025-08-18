'''Crea una función llamada procesar_texto
Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
Código a seguir:
Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
Caso de uso:
Verificar el funcionamiento completo de procesar_texto.'''
def contar_palabras(texto):
    cantidad_palabras = {}
    for word in texto.split():
        word = word.lower()
        if word in cantidad_palabras:
            cantidad_palabras[word]  += 1
        else:
            cantidad_palabras[word] = 1
    return cantidad_palabras

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    palabras = texto.split()
    return " ".join([palabra_nueva if word.lower() == palabra_original.lower() else word for word in palabras])

def eliminar_palabras(texto, palabra_eliminada):
    palabras = texto.split()
    return " ".join([word for word in palabras if word.lower() != palabra_eliminada.lower()])
def procesar_texto(texto):
    while True:
        
            print("----Menú----")
            print("1- Contar palabras")
            print("2- Reemplazar palabras")
            print("3- Eliminar palabras")
            print("4- Salir")
            try:    
                indice = int(input("Cual es tu indice?"))
            except ValueError:
                print("Introduce un numero")
                continue
            match indice:
                case 1: print(contar_palabras(texto))
                case 2: 
                        palabra_original = input("¿Que palabra quieres cambiar?").lower()
                        palabra_nueva = input("¿Cual es tu palabra nueva?").lower()
                        texto = reemplazar_palabras(texto, palabra_original, palabra_nueva)
                case 3: 
                        palabra_eliminada = input("¿Cual es tu palabra a eliminar?").lower()
                        texto = eliminar_palabras(texto, palabra_eliminada)
                case 4:
                        print("Apagando...")
                        return False
                case _:
                        print("Opcion invalida")
            
procesar_texto("Hola soy un texto de prueba Hola caracola hola")