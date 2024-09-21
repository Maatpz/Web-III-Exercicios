from tkinter import *

#3. Crie um programa com três opções de seleção (RadioButton): "Opção A", "Opção B", e
#"Opção C". Quando o usuário selecionar uma das opções e clicar em "Confirmar", a escolha
#deve ser exibida em um Label.

'''
m=Tk()
m.geometry("400x200")
valor = IntVar()

def exibir_escolha():
    escolha = valor.get()  # Pega o valor da variável 'valor'
    if escolha == 1:
        label_resultado.config(text="Escolheu a Opção A")
    elif escolha == 2:
        label_resultado.config(text="Escolheu a Opção B")
    elif escolha == 3:
        label_resultado.config(text="Escolheu a Opção C")


opcaoA = Radiobutton(m, text="Opção A", variable=valor, value=1)
opcaoA.pack()
opcaoB = Radiobutton(m, text="Opção B", variable=valor, value=2)
opcaoB.pack()
opcaoC = Radiobutton(m, text="Opção C", variable=valor, value=3)
opcaoC.pack()

btn_confirma = Button(m, text="Confirmar", command=exibir_escolha)
btn_confirma.pack()

label_resultado = Label(m, text="")
label_resultado.pack()

m.mainloop()
'''