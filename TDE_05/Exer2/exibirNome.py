from tkinter import *

#2. Crie uma interface gráfica que contenha um Label com o texto "Digite seu nome" e um
#campo de entrada (Entry). Quando o usuário digitar o nome e pressionar um botão
#"Mostrar", o nome deve ser exibido em um novo Label abaixo.
'''
m = Tk()
m.title("Exercício 2")
m.geometry("400x200")
def exibir_nome():
    nome = e.get()
    label_resultado.config(text=f"Nome: {nome}")

l = Label(m, text='Digite seu nome:', relief='raised').pack(pady=10)

e = Entry(m)
e.pack(pady=5)

btn = Button(m, text="Mostrar", bg="black", fg="white", width=13, command=exibir_nome)
btn.pack(pady=10)

label_resultado = Label(m, font='Verdana 10 italic', text="")
label_resultado.pack(pady=10)
m.mainloop()
'''