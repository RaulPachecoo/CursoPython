import tkinter as tk

def mostrarNombre():
    nombreObtenido = nombre.get()
    resultado.config(text=f"Hola bienvenido, {nombreObtenido}")

ventana = tk.Tk()
ventana.title("Entry")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text="Ingrese su nombre: ")
etiqueta.pack()

nombre = tk.StringVar()
entradaNombre = tk.Entry(ventana, width=25, textvariable=nombre)
entradaNombre.pack()

boton = tk.Button(ventana, text="Saludar", command=mostrarNombre)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()


ventana.mainloop()