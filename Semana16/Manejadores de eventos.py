import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "La tarea no puede estar vacía.")

def mark_completed(event=None):
    try:
        selected_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_index)
        if not task_text.startswith("✔ "):
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Aviso", "Seleccione una tarea para marcar como completada.")

def delete_task(event=None):
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Seleccione una tarea para eliminar.")

def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x300")
root.resizable(False, False)

# Campo de entrada y botones
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
entry_task.bind("<Return>", add_task)  # Atajo para agregar tarea

frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="Añadir", command=add_task)
btn_add.grid(row=0, column=0, padx=5)

btn_complete = tk.Button(frame_buttons, text="Completar", command=mark_completed)
btn_complete.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Eliminar", command=delete_task)
btn_delete.grid(row=0, column=2, padx=5)

# Lista de tareas
listbox_tasks = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=5)
listbox_tasks.bind("<BackSpace>", delete_task)  # Asignar eliminación a la lista

# Atajos de teclado
root.bind("1", mark_completed)  # Marcar como completada con '1'
root.bind("<Escape>", close_app)  # Cerrar con 'Escape'

# Ejecutar la aplicación
root.mainloop()
