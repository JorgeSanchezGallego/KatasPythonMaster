#29- Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
contraseña = 12345678910
def secreto(password):
    password_str = str(password)
    codificada = "#" * (len(password_str) -4) + password_str[-4:]
    return codificada
print(secreto(contraseña))

