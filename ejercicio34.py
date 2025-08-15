"""Crea la clase Arbol
Define un árbol genérico con un tronco y ramas como atributos.
Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
Código a seguir:
Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
Implementar el método quitar_rama para eliminar una rama en una posición específica.
Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
Caso de uso:
        a. Crear un árbol.
        b. Hacer crecer el tronco una unidad.
        c. Añadir una nueva rama.
        d. Hacer crecer todas las ramas una unidad.
        e. Añadir dos nuevas ramas.
        f. Retirar la rama situada en la posición 2.
        g. Obtener información sobre el árbol."""

class Arbol:
    def __init__(self, tronco = 1):
        self.tronco = tronco
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1
        print(f"El tronco ahora mide {self.tronco}")

    def nueva_rama(self):
        self.ramas.append(1)
        print(f"Ahora tu arbol tiene {len(self.ramas)} ramas")

    def crecer_ramas(self):
        self.ramas = [rama +1 for rama in self.ramas]
        print(f"Las ramas crecieron: {self.ramas}")

    def quitar_rama(self, posicion):
        if posicion >= 0 and posicion < len(self.ramas):
            self.ramas.pop(posicion)
            print("Rama eliminada")
        else:
            print("Posición no encontrada")
    
    def info_arbol(self):
        print(f"Tu tronco mide {self.tronco} tiene {len(self.ramas)} rama con su longitud {self.ramas} ")

primer_arbol =Arbol()
primer_arbol.crecer_tronco()
primer_arbol.nueva_rama()
primer_arbol.crecer_ramas()
primer_arbol.nueva_rama()
primer_arbol.nueva_rama()
primer_arbol.quitar_rama(2)
primer_arbol.info_arbol()