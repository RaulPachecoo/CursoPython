import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("ProgressBar")
ventana.geometry("500x500")

barraProgreso = ttk.Progressbar(ventana, mode='determinate', length=200)
barraProgreso.pack()

def iniciarProgreso():
    barraProgreso['value'] = 0
    ventana.update()
    for i in range(101):
        barraProgreso['value'] = i
        ventana.update()
        ventana.after(500)

boton = tk.Button(ventana, text="Iniciar Progreso", command=iniciarProgreso)
boton.pack()


ventana.mainloop()