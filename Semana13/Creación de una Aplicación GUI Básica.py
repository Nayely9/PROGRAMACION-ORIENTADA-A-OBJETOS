import tkinter as tk
from tkinter import messagebox

# Función para agregar un elemento a la lista
def agregar_elemento():
    elemento = entrada.get()
    if elemento:
        lista.insert(tk.END, elemento)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un dato antes de agregar.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Lista de Datos")
ventana.geometry("400x300")

# Crear etiquetas
titulo = tk.Label(ventana, text="Ingrese un dato y agréguelo a la lista", font=("Arial", 12))
titulo.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botón para agregar elementos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Lista para mostrar elementos
lista = tk.Listbox(ventana, font=("Arial", 12), width=40, height=8)
lista.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
