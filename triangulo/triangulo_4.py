import tkinter as tk
from tkinter import ttk

def calcula():
    lado1 = int(txtPrimerLado.get())
    lado2 = int(txtSegundoLado.get())
    lado3 = int(txtTercelLado.get())
    if (not((lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1))):
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
        result.insert(tk.INSERT, "ISÓCELES")

def dibuja():
    ventana = tk.Tk()
    ventana.geometry("500x250")
    ventana.resizable(False,False)
    ventana.title("TIPOS DE TRIANGULOS")       
    lblPrimerLado = ttk.Label(ventana, text = "Primer lado")
    lblPrimerLado.pack()
    txtPrimerLado = ttk.Entry(ventana)
    txtPrimerLado.pack()
    lblSegundoLado = ttk.Label(ventana, text = "Segundo lado")
    lblSegundoLado.pack()
    txtSegundoLado = ttk.Entry(ventana)
    txtSegundoLado.pack()
    lblTercerLado = ttk.Label(ventana, text = "Tercer lado")
    lblTercerLado.pack()
    txtTercelLado = ttk.Entry(ventana)
    txtTercelLado.pack()   
    btnClasificar = ttk.Button(ventana, text="Calcular", command=calcula)
    btnClasificar.pack()
    result = tk.Text(ventana, height = 4, width = 30, bg = "light cyan")
    result.pack()    
    return ventana, txtPrimerLado, txtSegundoLado, txtTercelLado, btnClasificar, result

if __name__ == '__main__':
    ventana, txtPrimerLado, txtSegundoLado, txtTercelLado, btnClasificar, result = dibuja()
    ventana.mainloop()
