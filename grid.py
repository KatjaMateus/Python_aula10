from tkinter import *

janela = Tk()
janela.title("Aprendendo grid")
janela.geometry("300x300")

nome_label=Label(text="Digite seu nome", padx=30, pady=30)
nome_label.grid(row=0, column=0)

nome_input=Entry()
nome_input.grid(row=0, column=1)

idade_label=Label(text="Digite sua idade")
idade_label.grid(row=1, column=0)

idade_input=Entry()
idade_input.grid(row=1, column=1)

botao = Button(janela, text="Enviar", width=38, padx=10)
botao.grid(row=2, column=0, columnspan=2)


janela.mainloop()