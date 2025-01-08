# Programa para calcular el costo total de una comida con propina e impuestos
# Este programa permite al usuario ingresar el costo de una comida, calcular la propina, los impuestos y el costo total.

def calcular_costo_total(costo_comida, porcentaje_propina, porcentaje_impuestos):
    """Calcula el costo total de una comida incluyendo propina e impuestos."""
    propina = costo_comida * (porcentaje_propina / 100)
    impuestos = costo_comida * (porcentaje_impuestos / 100)
    costo_total = costo_comida + propina + impuestos
    return costo_total, propina, impuestos

def main():
    """Función principal del programa."""
    print("Calculadora de costo total de una comida")

    # Solicitar al usuario el costo de la comida y los porcentajes
    costo_comida = float(input("Ingresa el costo de la comida: "))
    porcentaje_propina = float(input("Ingresa el porcentaje de propina: "))
    porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos: "))

    # Calcular el costo total, la propina y los impuestos
    costo_total, propina, impuestos = calcular_costo_total(costo_comida, porcentaje_propina, porcentaje_impuestos)

    # Mostrar los resultados al usuario
    print(f"Costo de la comida: ${costo_comida:.2f}")
    print(f"Propina ({porcentaje_propina}%): ${propina:.2f}")
    print(f"Impuestos ({porcentaje_impuestos}%): ${impuestos:.2f}")
    print(f"Costo total: ${costo_total:.2f}")

if __name__ == "__main__":
    main()
