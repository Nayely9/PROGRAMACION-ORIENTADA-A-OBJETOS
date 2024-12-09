# Clase base para un personaje
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        """
        Inicializa un personaje con atributos básicos.
        :param nombre: Nombre del personaje.
        :param fuerza: Fuerza física del personaje.
        :param inteligencia: Inteligencia mágica o estratégica del personaje.
        :param defensa: Capacidad de resistencia al daño.
        :param vida: Vida del personaje.
        """
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def mostrar_atributos(self):
        """Muestra los atributos del personaje."""
        print(f"{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        """Incrementa los atributos del personaje."""
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        """Comprueba si el personaje sigue vivo."""
        return self.vida > 0

    def recibir_daño(self, daño):
        """Reduce la vida del personaje según el daño recibido."""
        self.vida -= daño
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha muerto.")

# Clase Guerrero, hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        """
        Inicializa un Guerrero con un arma específica.
        :param espada: Daño adicional del arma del guerrero.
        """
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        """Permite al guerrero elegir un arma."""
        print("Elige un arma:")
        print("(1) Acero Valyrio (daño +8)")
        print("(2) Matadragones (daño +10)")
        opcion = int(input("Introduce tu opción: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Opción no válida.")

    def calcular_daño(self, enemigo):
        """Calcula el daño infligido al enemigo."""
        return max(0, (self.fuerza + self.espada) - enemigo.defensa)

# Clase Mago, hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        """
        Inicializa un Mago con un libro de hechizos.
        :param libro: Poder mágico adicional del libro.
        """
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def calcular_daño(self, enemigo):
        """Calcula el daño infligido al enemigo basado en magia."""
        return max(0, (self.inteligencia * self.libro) - enemigo.defensa)

# Función para simular el combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        print(f">>> {jugador_1.nombre} ataca a {jugador_2.nombre}.")
        daño = jugador_1.calcular_daño(jugador_2)
        jugador_2.recibir_daño(daño)
        print(f"{jugador_2.nombre} tiene {jugador_2.vida} de vida restante.")

        if not jugador_2.esta_vivo():
            break

        print(f">>> {jugador_2.nombre} ataca a {jugador_1.nombre}.")
        daño = jugador_2.calcular_daño(jugador_1)
        jugador_1.recibir_daño(daño)
        print(f"{jugador_1.nombre} tiene {jugador_1.vida} de vida restante.")
        turno += 1

    # Determinar el resultado del combate
    if jugador_1.esta_vivo():
        print(f"\n¡{jugador_1.nombre} ha ganado el combate!")
    elif jugador_2.esta_vivo():
        print(f"\n¡{jugador_2.nombre} ha ganado el combate!")
    else:
        print("\nEl combate ha terminado en empate.")

# Ejemplo de uso
if __name__ == "__main__":
    guerrero = Guerrero("Guts", fuerza=20, inteligencia=10, defensa=5, vida=100, espada=4)
    mago = Mago("Vanessa", fuerza=5, inteligencia=15, defensa=4, vida=100, libro=3)

    guerrero.mostrar_atributos()
    mago.mostrar_atributos()

    combate(guerrero, mago)
