import json  # Importa la biblioteca json para trabajar con archivos JSON

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Args:
            id_producto (str): El ID único del producto.
            nombre (str): El nombre del producto.
            cantidad (int): La cantidad en stock del producto.
            precio (float): El precio del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del objeto Producto.

        Returns:
            str: Una cadena con la información del producto.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar los productos.
        """
        self.productos = {}

    def cargar_inventario(self, archivo='inventario.json'):
        """
        Carga el inventario desde un archivo JSON.
        """
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                if isinstance(datos, dict):
                    self.productos = datos
                else:
                    print("Formato inválido en el archivo JSON. Se usará un inventario vacío.")
                    self.productos = {}
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error al cargar el inventario. Se usará un inventario vacío.")
            self.productos = {}

    def guardar_inventario(self, archivo='inventario.json'):
        """
        Guardar el inventario en un archivo JSON.
        """
        try:
            with open(archivo, 'w') as f:
                json.dump(self.productos, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.
        """
        if producto.id_producto in self.productos:
            print("Producto ya existe.")
        else:
            self.productos[producto.id_producto] = {
                'nombre': producto.nombre,
                'cantidad': producto.cantidad,
                'precio': producto.precio
            }

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto en el inventario.
        """
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto]['cantidad'] = cantidad
            if precio is not None:
                self.productos[id_producto]['precio'] = precio
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca y muestra productos por nombre.
        """
        encontrados = [Producto(id_prod, info['nombre'], info['cantidad'], info['precio'])
                       for id_prod, info in self.productos.items() if info['nombre'].lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """
        Muestra la información de todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for id_producto, info in self.productos.items():
                print(Producto(id_producto, info['nombre'], info['cantidad'], info['precio']))

def menu():
    """
    Función principal que muestra el menú y maneja las opciones del usuario.
    """
    inventario = Inventario()
    inventario.cargar_inventario()

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto por Nombre\n5. Mostrar Inventario\n6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            inventario.guardar_inventario()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()