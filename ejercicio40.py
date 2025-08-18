"""Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones."""
def precio_original():
    precio_real = float(input("¿Cual es el precio original del producto?"))
    return tiene_descuento(precio_real)
def tiene_descuento(precio_real):
    tiene_descuento = input("¿Este producto tiene descuento?")
    if tiene_descuento.lower() == "si":
        porcentaje_descuento = int(input("¿Cual es su porcentaje de descuento?"))
        if porcentaje_descuento > 0 and porcentaje_descuento < 100:
            precio_final = precio_real - (precio_real * porcentaje_descuento / 100)
            return precio_final 
        else:
            print("Porcentaje invalido")
            return precio_real
    else:
        return precio_real

print(f"El precio de tu producto es de {precio_original()}")