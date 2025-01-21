class FileHandler:
    # Constructor (__init__) que inicializa el archivo y el modo de apertura.
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print(f"Constructor: Abriendo el archivo '{self.filename}' en modo '{self.mode}'")

        try:
            # abrir el archivo en el modo especificado
            self.file = open(self.filename, self.mode)
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    # Metodo para escribir en el archivo
    def write_data(self, data):
        if self.file:
            try:
                self.file.write(data)
                print("Datos escritos en el archivo.")
            except Exception as e:
                print(f"Error al escribir en el archivo: {e}")
        else:
            print("El archivo no está abierto para escritura.")

    # Destructor (__del__) que cierra el archivo si está abierto
    def __del__(self):
        if self.file:
            try:
                # Cerrar el archivo si está abierto
                self.file.close()
                print(f"Destructor: El archivo '{self.filename}' ha sido cerrado correctamente.")
            except Exception as e:
                print(f"Error al cerrar el archivo: {e}")


# Ejemplo de uso del programa

# Creación de un objeto de la clase FileHandler. El constructor se activa aquí.
file_handler = FileHandler("example.txt", "w")

# Escribimos algunos datos en el archivo usando el metodo write_data.
file_handler.write_data("Hola, este es un texto de prueba.\n")

# Cuando el objeto file_handler ya no se use o al final del programa, el destructor se activa automáticamente.
del file_handler  # Aquí se invoca el destructor explícitamente, aunque esto también ocurriría automáticamente al salir del alcance del objeto.
