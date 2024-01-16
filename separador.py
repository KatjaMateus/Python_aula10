from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Separador")

label1 = ttk.Label(janela, text="Text 1")
label1.pack(pady=40)

separador = ttk.Separator(janela, orient=HORIZONTAL)
separador.pack(padx=20, ipadx=50)

label2 = ttk.Label(janela, text="Texto 2")
label2.pack(pady=40)

janela.mainloop()