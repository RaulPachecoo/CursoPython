import tkinter as tk


ventana = tk.Tk()
ventana.title("CheckButton")
ventana.geometry("500x500")

opcionVar = tk.IntVar()

checkOpciones = tk.Checkbutton(
    ventana, 
    text="¿Desea recibir notificaciones?",
    variable=opcionVar,
    onvalue=1,
    offvalue=0
)
checkOpciones.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

def mostrarEstado():
    if opcionVar.get() == 1:
        resultado.config(text="Notificaciones Activadas")
        print(opcionVar)
    else:
        resultado.config(text="Notificaciones Desactivadas")
        print(opcionVar)

boton = tk.Button(ventana, text="Confirmar", command=mostrarEstado)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()