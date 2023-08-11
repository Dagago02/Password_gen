import tkinter as tk
from tkinter import ttk
import main 

def get_selection():
    selected_option = option_combobox.get()
    mode = option_values[selected_option]
    passlen = int(number_combobox.get())
    direction = text_entry.get()
    
    main.Password(mode=mode,passlen=passlen,direction=direction)
    """print("Selected Option:", selected_option)
    print("Selected Option Value:", mode)
    print("Selected Number:", passlen)
    print("Text Input:", direction)"""

# Crear la ventana principal
root = tk.Tk()
root.title("Passwordgen")

# Crear un Combobox para opciones
option_label = tk.Label(root, text="Modo:")
option_label.pack()

option_values = {"Normal": 1, "XKCD": 0}
options = list(option_values.keys())
option_combobox = ttk.Combobox(root, values=options, state="readonly")
option_combobox.pack()
option_combobox.set("NORMAL")

# Crear un Combobox para números del 1 al 10
number_label = tk.Label(root, text="PasswordLenght:")
number_label.pack()

numbers = list(range(1, 11))
number_combobox = ttk.Combobox(root, values=numbers, state="readonly")
number_combobox.pack()

# Configurar el segundo Combobox para no permitir la selección del número 0
number_combobox.set("10")  # Establecer un valor inicial distinto de 0

# Crear un Entry para ingresar texto
text_label = tk.Label(root, text="Direccion:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

# Botón para obtener selecciones
get_selection_button = tk.Button(root, text="Generar Contraseña", command=get_selection)
get_selection_button.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()
