import tkinter as tk

ventana = tk.Tk()
ventana.title("Scale")
ventana.geometry("500x500")

valorVar = tk.IntVar()

def mostrarValor():
    resultado.config(text=f"Valor seleccionado por el usuario: {valorVar.get()}")

escala = tk.Scale(
    ventana, 
    from_ = 0, 
    to= 100,
    orient=tk.HORIZONTAL,
    variable=valorVar
)
escala.pack()

boton = tk.Button(ventana, text="Mostrar Valor", command=mostrarValor)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()