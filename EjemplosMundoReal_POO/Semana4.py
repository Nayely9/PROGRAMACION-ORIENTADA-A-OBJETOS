# Clase que representa una cuenta bancaria
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        """
        Inicializa los atributos de la cuenta bancaria.
        :param numero_cuenta: Número único de la cuenta.
        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto, 0).
        """
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """
        Añade dinero al saldo de la cuenta.
        :param cantidad: Monto a depositar.
        """
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo}"
        else:
            return "El monto a depositar debe ser mayor a cero."

    def retirar(self, cantidad):
        """
        Retira dinero del saldo de la cuenta.
        :param cantidad: Monto a retirar.
        """
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        elif cantidad > 0:
            self.saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: ${self.saldo}"
        else:
            return "El monto a retirar debe ser mayor a cero."

    def mostrar_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        return f"Saldo actual de la cuenta {self.numero_cuenta}: ${self.saldo}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta bancaria
    cuenta = CuentaBancaria("123456789", "Ana Pérez", 100)

    # Mostrar saldo inicial
    print(cuenta.mostrar_saldo())

    # Realizar un depósito
    print(cuenta.depositar(50))

    # Intentar un retiro mayor al saldo
    print(cuenta.retirar(200))

    # Realizar un retiro válido
    print(cuenta.retirar(80))

    # Mostrar saldo final
    print(cuenta.mostrar_saldo())
