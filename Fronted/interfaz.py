import tkinter as tk

# Función para capturar el texto ingresado por el usuario
def capturar_texto():
    texto_ingresado = entrada.get()
    print("Texto ingresado:", texto_ingresado)

# Crear la ventana
ventana = tk.Tk()

# Crear una etiqueta y mostrarla en la ventana
etiqueta = tk.Label(ventana, text="Ingresa el enlace de la canción:")
etiqueta.pack()

# Crear una entrada de texto y mostrarla en la ventana
entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón para capturar el texto ingresado
boton = tk.Button(ventana, text="Capturar", command=capturar_texto)
boton.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
