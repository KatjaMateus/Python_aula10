from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Sizegrip")

janela.resizable(True, True)

sizegrip = ttk.Sizegrip(janela)
sizegrip.pack(anchor=SE, padx=3, pady=3, expand=True)

janela.mainloop()