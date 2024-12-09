class ClimaDiario:
    def __init__(self, dia, temperatura=0.0):
        self.dia = dia
        self.temperatura = temperatura

    def ingresar_temperatura(self):
        self.temperatura = float(input(f"Ingrese la temperatura para el {self.dia}: "))

class PromedioClimaSemanal:
    def __init__(self):
        self.datos_semanales = [
            ClimaDiario("Día 1"),
            ClimaDiario("Día 2"),
            ClimaDiario("Día 3"),
            ClimaDiario("Día 4"),
            ClimaDiario("Día 5"),
            ClimaDiario("Día 6"),
            ClimaDiario("Día 7")
        ]

    def ingresar_datos(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for clima in self.datos_semanales:
            clima.ingresar_temperatura()

    def calcular_promedio(self):
        total = sum([clima.temperatura for clima in self.datos_semanales])
        return total / len(self.datos_semanales)

# Uso de las clases
if __name__ == "__main__":
    clima_semanal = PromedioClimaSemanal()
    clima_semanal.ingresar_datos()
    promedio = clima_semanal.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")
