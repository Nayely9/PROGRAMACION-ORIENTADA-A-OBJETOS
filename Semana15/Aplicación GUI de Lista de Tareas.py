import tkinter as tk
from tkinter import messagebox, ttk


class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tareas")
        self.master.geometry("400x350")

        # Entrada de nueva tarea
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', self.add_task)  # Añadir tarea con Enter

        # Botones
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_list = tk.Listbox(master, width=50, height=10)
        self.task_list.pack(pady=10)

        # Evento de doble clic para marcar como completada
        self.task_list.bind('<Double-Button-1>', lambda event: self.complete_task())

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_index)
            self.task_list.delete(selected_index)
            self.task_list.insert(selected_index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Selección vacía", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selección vacía", "Por favor, selecciona una tarea para eliminar.")


if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
