class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio  # Precio del producto

    def __str__(self):
        # Representación en cadena del producto
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio}"


class Inventario:
    # Clase que maneja la lista de productos en el inventario
    def __init__(self):
        self.productos = []  # Lista de productos en el inventario

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        # Añade un nuevo producto al inventario si el ID es único
        if any(p.id_producto == id_producto for p in self.productos):
            print("Error: El ID ya existe.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario por su ID
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto por su ID
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos en el inventario por su nombre (puede haber nombres similares)
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos.")

    def mostrar_productos(self):
        # Muestra todos los productos en el inventario
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    # Función que implementa un menú interactivo en la consola
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío si no desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            # Mostrar todos los productos
            inventario.mostrar_productos()
        elif opcion == "6":
            # Salir del sistema
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
