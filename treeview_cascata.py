from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Treeview em cascata")
janela.geometry("400x300")

tree = ttk.Treeview(janela)

tree.insert("", END, iid="py", text="Python")
tree.insert("", END, iid="jv", text="JavaScript")

tree.insert("py", END, text="Condicionais")
tree.insert("py", END, text="Repetições")
tree.insert("py", END, text="Funções")

tree.insert("jv", END, text="Condicionais")
tree.insert("jv", END, text="Repetições")
tree.insert("jv", END, text="Funções")

tree.pack()

janela.mainloop()
