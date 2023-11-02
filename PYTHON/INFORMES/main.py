import tkinter as tk
from tkinter import filedialog

global folder_path

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_label.config(text=f"Ruta de la carpeta seleccionada: {folder_path}")
    print(folder_path)

# Crear una ventana
root = tk.Tk()
root.title("Selector de Carpeta")

# Crear un botón para seleccionar la carpeta
select_button = tk.Button(root, text="Seleccionar Carpeta", command=select_folder)
select_button.pack(pady=20)

# Etiqueta para mostrar la ruta de la carpeta seleccionada
folder_label = tk.Label(root, text="", wraplength=300)
folder_label.pack()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()


