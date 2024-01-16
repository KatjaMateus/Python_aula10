from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Combobox")

dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

combobox = ttk.Combobox(janela, values=dias_semana)
combobox.pack(padx=75, pady=20)

janela.mainloop()