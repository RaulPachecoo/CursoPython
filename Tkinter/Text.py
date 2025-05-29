import tkinter as tk

def mostrarComentario():
    comentarioObtenido = comentario.get("1.0", tk.END).strip()
    resultado.config(text=f"Comentario: {comentarioObtenido}")

ventana = tk.Tk()
ventana.title("Text")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text="Escriba su comentario:")
etiqueta.pack()

comentario = tk.Text(ventana, width=40, height=5, wrap="word")
comentario.pack()

boton = tk.Button(ventana, text="Mostrar comentario", command=mostrarComentario)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()