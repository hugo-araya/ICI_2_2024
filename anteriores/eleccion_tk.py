# Autor: yo
import tkinter as tk
from tkinter import ttk

def limpia():
    strvar.set('')

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title('Resultados elecciones')
    ventana.geometry("800x500")
    ventana.resizable(0,0)
    etiqueta1 = ttk.Label(ventana, text = 'Archivo')
    etiqueta1.grid(row=0, column=0)
    strvar = tk.StringVar()
    strvar.set('Ingrese nombre')
    entrada = ttk.Entry(ventana, textvariable = strvar)
    entrada.grid(row=0, column = 1)
    ejecutar = ttk.Button(ventana, text = 'Ejecutar')
    ejecutar.grid(row = 1, column = 0)
    cancelar = ttk.Button(ventana, text = 'cancelar', command = limpia)
    cancelar.grid(row = 1, column = 1)
    salir = ttk.Button(ventana, text = 'salir', command = quit)
    salir.grid(row = 1, column = 2)
    ventana.mainloop()
