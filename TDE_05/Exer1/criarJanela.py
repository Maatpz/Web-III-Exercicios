from tkinter import *

#1. Criação de uma Janela Básica Crie um programa que abra uma janela básica com o título
#"Minha Primeira Janela". A janela deve ter as dimensões 300x200 pixels e um botão que, ao
#ser clicado, fecha a janela.
'''
m = Tk()
def fechar_janela():
   m.destroy()

m.title("Minha Primeira Janela")
m.geometry('300x200')
m.resizable(0,0)

btn = Button(m, text="Fechar",bg="black", width=15,command=fechar_janela)
btn.pack(pady=20)
m.mainloop()
'''
