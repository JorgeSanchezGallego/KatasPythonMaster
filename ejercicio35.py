'''Crea la clase UsuarioBanco
    Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
    Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
Código a seguir:
    Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
    Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
    Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
    Implementar agregar_dinero para aumentar el saldo del usuario.
Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.'''
class saldoInsuficiente(Exception):
    pass
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo and cantidad > 0:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad} €")
        else:
            raise saldoInsuficiente ("Error de saldo")
        
    def transferir_dinero(self, destinatario, cantidad):
        if not isinstance(destinatario, UsuarioBanco):
            raise TypeError("El destinatario debe ser un objeto UsuarioBanco")
        if cantidad <= self.saldo and cantidad > 0:
            self.saldo -= cantidad
            destinatario.saldo += cantidad
            print(f"Transferencia realizada de {self.nombre} a {destinatario.nombre} de {cantidad}€")
        else:
            raise saldoInsuficiente ("Error de saldo")
        
    def agregar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Saldo agregado {cantidad} €, tu saldo ahora es de {self.saldo}")
        else:
            raise ValueError ("La cantidad debe ser mayor que cero")
        
user1 = UsuarioBanco("Alicia", 100, True)
user2 = UsuarioBanco("Bob", 50, True)
try:
    user2.agregar_dinero(20)
except ValueError as e:
    print(e)
try:
    user2.transferir_dinero(user1, 80)
except saldoInsuficiente as e:
    print(e)
except TypeError as e:
    print(e)
try:
    user1.retirar_dinero(50)
except saldoInsuficiente as e:
    print(e)