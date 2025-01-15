# Programa que demuestra un sistema de gestión de estudiantes

# Clase base que representa una Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.edad = edad  # Atributo público

    # Método que describe a la persona
    def describir(self):
        return f"{self.nombre}, {self.edad} años"

# Clase derivada que representa un Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.matricula = matricula  # Atributo adicional para el estudiante

    # Sobrescritura del método describir (polimorfismo)
    def describir(self):
        return f"Estudiante {self.nombre}, {self.edad} años, Matrícula: {self.matricula}"

# Clase derivada que representa un Profesor
class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.especialidad = especialidad  # Atributo adicional para el profesor

    # Sobrescritura del método describir (polimorfismo)
    def describir(self):
        return f"Profesor {self.nombre}, {self.edad} años, Especialidad: {self.especialidad}"

# Programa principal para demostrar la funcionalidad de las clases
def main():
    # Crear instancias de las clases
    estudiante = Estudiante("Luis", 20, "A12345")
    profesor = Profesor("María", 40, "Matemáticas")

    # Mostrar descripciones utilizando polimorfismo
    print(estudiante.describir())
    print(profesor.describir())

    # Mostrar detalles básicos usando la clase base
    print("\nDetalles básicos:")
    print(f"Nombre del estudiante: {estudiante.nombre}")
    print(f"Nombre del profesor: {profesor.nombre}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
