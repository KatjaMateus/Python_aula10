from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Progressbar")

progressbar = ttk.Progressbar(janela, orient = HORIZONTAL, length = 200, mode = "indeterminate")
progressbar.pack()
progressbar.start(50)

janela.mainloop()