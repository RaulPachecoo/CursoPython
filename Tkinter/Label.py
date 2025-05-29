import tkinter as tk

ventana = tk.Tk()
ventana.title("Label")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text="Hola, bienvenidos a Tkinter!")
etiqueta.pack()

etiqueta2 = tk.Label(ventana, text="Este es un segundo Label") 
etiqueta2.pack()

ventana.mainloop()