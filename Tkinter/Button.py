import tkinter as tk


def cambiarTexto():
    mensaje.config(text="Texto cambiado")

def restablecerTexto():
    mensaje.config(text="Texto original")


ventana = tk.Tk()
ventana.title("Label")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text="Botones:")
etiqueta.pack()

etiqueta.config(text="Funcionalidades:")

mensaje = tk.Label(ventana, text="Texto original")
mensaje.pack()

boton1 = tk.Button(ventana, text="Cambiar texto", command=cambiarTexto)
boton1.pack()

boton2 = tk.Button(ventana, text="Restablecer texto", command=restablecerTexto)
boton2.pack()

ventana.mainloop()