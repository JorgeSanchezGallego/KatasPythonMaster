#9- Escribe una función que tome una lista de nombres de mascotas como parámetro 
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter().
mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
mascotas_deseadas = ["Perro", "Gato", "Serpiente Pitón", "Cocodrilo", "Oso", "Pez", "Huron"]
masc_legales = list(filter(lambda m: m not in mascotas_prohibidas, mascotas_deseadas))
print(masc_legales)