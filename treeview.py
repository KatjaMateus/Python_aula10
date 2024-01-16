from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Treeview")

tree = ttk.Treeview(janela)
tree["columns"]=("nome", "email", "telefone")

tree.column("#0", width=110,minwidth=100,anchor=CENTER)
tree.column("nome", width=150, minwidth=150, anchor = CENTER)
tree.column("email", width=150, minwidth=150, anchor = CENTER)
tree.column("telefone", width=150, minwidth=150, anchor = CENTER)

tree.heading("#0", text="ID")
tree.heading("nome", text="NOME")
tree.heading("email", text="EMAIL")
tree.heading("telefone", text="TEL")

tree.insert("", END, text="1", values=("João Silva", "joalsilva@gmail.com", "(41)555444"))
tree.insert("", END, text="2", values=("Maria Santos", "mariasnatos@gmail.com", "(71)3334456"))
tree.insert("", END, text="3", values=("Pedro Alemeida", "pedro@gmail.com", "(85)7009 444"))

tree.pack()
janela.mainloop()