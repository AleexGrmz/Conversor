#App para convertir pies a metros usando tkinter
#Ramon Alejandro Gallegos Ramirez
#23 de febrero del 2023

from tkinter import* #es un paquete en python
from tkinter import ttk

class conversor:
    #tipo constructor de la clase
 def __init__(self, raiz):
    raiz.title("Pies a metros")

    mainFrame = ttk.Frame(raiz)
    mainFrame.grid(column=0, row=0)

    piesEntry = ttk.Entry(mainFrame)
    piesEntry.grid(column=1, row=0)

    ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
    ttk.Label(mainFrame, text="Son equivalentes a:").grid(column=0, row=1)
    ttk.Label(mainFrame, text="Resultado").grid(column=1, row=1)
    ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

    ttk.Button(mainFrame, text="Calcular").grid(column=2, row=2)

if __name__=="__main__":
    print("Este es el archivo principal")
    print("Nada mas se mostrara esto si es el principal") 
       
