from tkinter import *
import tkinter as tk
ventana = tk.Tk()
ventana.geometry("500x250")
ventana.resizable(False,False)
ventana.title("TTIPOS DE TRIANGULOS")       
lblPrimerLado = tk.Label(ventana, text = "Primer lado")
lblPrimerLado.pack()
txtPrimerLado = tk.Entry(ventana)
txtPrimerLado.pack()
lblSegundoLado = tk.Label(ventana, text = "Segundo lado")
lblSegundoLado.pack()
txtSegundoLado = tk.Entry(ventana)
txtSegundoLado.pack()
lblTercerLado = tk.Label(ventana, text = "Tercer lado")
lblTercerLado.pack()
txtTercelLado = tk.Entry(ventana)
txtTercelLado.pack()
def main():
    lado1 = int(txtPrimerLado.get())
    lado2 = int(txtSegundoLado.get())
    lado3 = int(txtTercelLado.get())
    if (not((lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3
> lado1))):
        result.delete("1.0", tk.END)
        result.insert(tk.INSERT, "NO ES UN TRIÁNGULO")
    elif (lado1 == lado2 and lado1 == lado3):
        result.delete("1.0", tk.END)
        result.insert(tk.INSERT, "EQUILÁTERO")
    elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        result.delete("1.0", tk.END)
        result.insert(tk.INSERT, "ESCALENO")
    else:
        result.delete("1.0", tk.END)
        result.insert(tk.INSERT, "ISÓSELES")
btnClasificar = tk.Button(ventana, text="Calcular", command=main)
btnClasificar.pack()
result = tk.Text(ventana, height = 4, width = 30, bg = "light cyan")
result.pack()
ventana.mainloop()
