# FAÇA UMA INTERFACE QUE PEDE PARA O USUÁRIO DIGITAR 3 NOTAS E UM BOTÃO QUE AO SER CLICADO MOSTRA NA TELA UMA MENSAGEM "Aprovado" 
# SE A MÉDIA FOR MAIOR OU IGUAL A 7 COM A COR VERDE, "Reprovado" SE A MÉDIA FOR MENOR QUE 7 COM A COR DE FUNDO VERMELHO E "Aprovado com distinção" 
# SE A MÉDIA FOR IGUAL A 10 COM A COR DE FUNDO AZUL


from tkinter import *

janelinha = Tk()
janelinha.title("Resultado")
janelinha.geometry("350x350")

def media():
    # n1 = float(nota_input1.get())
    # n2 = float(nota_input2.get())
    # n3 = float(nota_input3.get())
    # media = (n1 + n2 + n3)/3
    media = (float(nota_input_1.get()) + float(nota_input_2.get()) + float(nota_input_3.get())) / 3
    if media >= 7 and media <10:
        resposta.configure(text=f"Aprovado", bg="green", fg="white")
    elif media < 7:
        resposta.configure(text=f"Reprovado", bg="red", fg="white")
    elif media == 10:
        resposta.configure(text=f"Aprovado com distinção", bg="blue", fg="white")
    else:
        resposta.configure(text="Nota inválida")

nota_1 = Label(text="Digite a primeira nota")
nota_1.pack()

nota_input_1 = Entry()
nota_input_1.pack()

nota_2 = Label(text="Digite a segunda nota")
nota_2.pack()

nota_input_2 = Entry()
nota_input_2.pack()

nota_3 = Label(text="Digite a terceira nota")
nota_3.pack()

nota_input_3 = Entry()
nota_input_3.pack()

botao = Button(janelinha, text="Resultado", command=media)
botao.pack()

resposta = Label(text="")
resposta.pack()


janelinha.mainloop()