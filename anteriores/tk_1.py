from tkinter import * 

def eventomio():
    print("Hola Mundo")
    print(entrada.get())
    label1.configure(text = entrada.get())

ventana = Tk()
ventana.title('titulo de mi ventana')
ventana.geometry("200x100")
label1 = Label(ventana,text="Intro a Tkinter")
label1.pack()
varstr = StringVar()
entrada = Entry(ventana,textvariable=varstr)
entrada.pack()
boton1 = Button(ventana,text="Boton 1")
boton1.pack()
boton2 = Button(ventana,text="Boton 2", command = eventomio)
boton2.pack()
ventana.mainloop()

