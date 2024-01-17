from tkinter import *
janela = Tk()
janela.title("login")
janela.geometry("250x300")

def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    if "@" in email and len(senha) > 6:
        resultado.configure(text="Login realizado com sucesso", bg="green", fg="white")
    else:
        resultado.configure(text="Login inválido", bg="red", fg="white")

label_email = Label(text="Digite seu email")
label_email.pack()

entry_email = Entry()
entry_email.pack()

label_senha = Label(text="Digite sua senha")
label_senha.pack()

entry_senha = StringVar()
entry_senha = Entry(janela, textvariable=entry_senha, show=entry_senha)
entry_senha.pack()

botao = Button(janela, text="Validar", command=validar_login)
botao.pack()

resultado = Label("")
resultado.pack()

janela.mainloop()