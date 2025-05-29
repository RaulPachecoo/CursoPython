import tkinter as tk

ventana = tk.Tk()
ventana.title("Menu")
ventana.geometry("500x500")

menuBar = tk.Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu = tk.Menu(menuBar, tearoff= 0)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)

archivoMenu.add_command(label="Nuevo", command=lambda: resultado.config(text = "Nuevo Archivo"))
archivoMenu.add_command(label="Abrir Archivo", command=lambda: resultado.config(text = "Abrir Archivo"))
archivoMenu.add_command(label="Guardar Archivo", command=lambda: resultado.config(text = "Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

editarMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Editar", menu=editarMenu)

editarMenu.add_command(label="Cortar", command=lambda: resultado.config(text = "Cortar"))
editarMenu.add_command(label="Copiar", command=lambda: resultado.config(text = "Copiar"))
editarMenu.add_command(label="Pegar", command=lambda: resultado.config(text = "Pegar"))


resultado = tk.Label(ventana, text="")
resultado.pack()


ventana.mainloop()