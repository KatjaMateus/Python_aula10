from tkinter import *

caixa = Tk()
caixa.title("Calculadora")
caixa.geometry("400x490")

nome_label=Label(text="", bg="blue", width=56, height=5)
nome_label.place(x=0, y=0)

botaoC = Button(caixa, text="C", bg="white", width=56, height=5)
botaoC.place(x=0, y=70)

botao1 = Button(caixa, text="1", bg = "yellow", width=13, height=5)
botao1.place(x=0, y=153)

botao2 = Button(caixa, text="2", bg = "yellow", width=13, height=5)
botao2.place(x=100, y=153)

botao3 = Button(caixa, text="3", bg = "yellow", width=13, height=5)
botao3.place(x=200, y=153)

botaoplus = Button(caixa, text="+", bg = "yellow", width=13, height=5)
botaoplus.place(x=300, y=153)

botao4 = Button(caixa, text="4", bg = "yellow", width=13, height=5)
botao4.place(x=0, y=237)

botao5 = Button(caixa, text="5", bg = "yellow", width=13, height=5)
botao5.place(x=100, y=237)

botao6 = Button(caixa, text="6", bg = "yellow", width=13, height=5)
botao6.place(x=200, y=237)

botaominus = Button(caixa, text="-", bg = "yellow", width=13, height=5)
botaominus.place(x=300, y=237)

botao7 = Button(caixa, text="7", bg = "yellow", width=13, height=5)
botao7.place(x=0, y=320)

botao8 = Button(caixa, text="8", bg = "yellow", width=13, height=5)
botao8.place(x=100, y=320)

botao9 = Button(caixa, text="9", bg = "yellow", width=13, height=5)
botao9.place(x=200, y=320)

botaomultiply = Button(caixa, text="*", bg = "yellow", width=13, height=5)
botaomultiply.place(x=300, y=320)

botaoerro = Button(caixa, text="⌫", bg = "yellow", width=13, height=5)
botaoerro.place(x=0, y=405)

botao0 = Button(caixa, text="0", bg = "yellow", width=13, height=5)
botao0.place(x=100, y=405)

botaocomma = Button(caixa, text=",", bg = "yellow", width=13, height=5)
botaocomma.place(x=200, y=405)

botaodivide = Button(caixa, text="/", bg = "yellow", width=13, height=5)
botaodivide.place(x=300, y=405)
caixa.mainloop()
