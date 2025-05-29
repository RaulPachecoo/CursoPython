import tkinter as tk

ventana = tk.Tk()
ventana.title("Personalizar Wisgets")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, 
    text="Bienvenidos a Tkinter", 
    bg="lightblue", 
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica", 24, "italic"),

)
etiqueta.pack(pady=25)

def accionBoton():
    etiqueta.config(text="Botón presionado", bg="green")

boton = tk.Button(ventana, 
    text="Haz click aquí",
    font=("Arial", 20, "bold"),
    bg = "orange",
    fg = "white",
    activebackground="red",
    activeforeground="yellow",
    width=15,
    command=accionBoton
)
boton.pack()

ventana.mainloop()