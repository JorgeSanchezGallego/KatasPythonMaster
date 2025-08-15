#32- Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista 
# y devuelva el puesto del empleado si se encuentra; de lo contrario, 
# devuelve un mensaje indicando que la persona no trabaja aquí.
empleados = [
    {"nombre": "Juan Pérez", "puesto": "Desarrollador Backend"},
    {"nombre": "María Gómez", "puesto": "Gerente de Ventas"},
    {"nombre": "Carlos López", "puesto": "Analista de Datos"},
    {"nombre": "Lucía Torres", "puesto": "Diseñadora UX/UI"},
    {"nombre": "Miguel Hernández", "puesto": "Administrador de Sistemas"},
    {"nombre": "Ana Fernández", "puesto": "Especialista en Marketing Digital"},
    {"nombre": "Diego Ramírez", "puesto": "Ingeniero DevOps"},
    {"nombre": "Sofía Martínez", "puesto": "Desarrolladora Frontend"},
    {"nombre": "Javier Ruiz", "puesto": "Contador"},
    {"nombre": "Valentina Castro", "puesto": "Recursos Humanos"}
]
def buscar_empleado(nombre, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    return f"{nombre} no trabaja aqui"

print(buscar_empleado("Juan Pérez", empleados))
print(buscar_empleado("Pedro Torres", empleados))