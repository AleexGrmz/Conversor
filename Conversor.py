#App para convertir pies a metros usando tkinter
#Ramon Alejandro Gallegos Ramirez
#23 de febrero del 2023

from tkinter import* #es un paquete en python
from tkinter import ttk

class conversor:
    #tipo constructor de la clase
    def __init__(self , raiz):
        raiz.title("Pies a metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0)

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies).grid(column=1, row=0) #Entry = textbox

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0) #Label = etiqueta
        ttk.Label(mainFrame, text="Son equivalentes a:").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)
        
        ttk.Button(mainFrame, text="Calcular", command=self.calcular ).grid(column=2, row=2)

        #Hacer la operacion precionar <enter>
        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
        print("Boton presionado")
        piesUsuario = self.pies.get()
        print("pies ingresados", piesUsuario)
        piesFlotante = float (piesUsuario)#conversion de cadena a flotante
        metros = piesFlotante * 0.3048 
        print("Metros: ",metros)
        self.metros.set(metros)
    
if __name__=="__main__":
    print("Este es el archivo principal")
    print("Nada mas se mostrara esto si es el principal") 
  
