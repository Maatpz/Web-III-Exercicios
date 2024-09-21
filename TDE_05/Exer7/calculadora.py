from tkinter import *

#7. Crie uma calculadora simples com dois campos de entrada e botões para as quatro
#operações básicas (adição, subtração, multiplicação, divisão). Quando o usuário inserir dois
# e clicar em uma operação, o resultado deve ser mostrado em um Label.

'''
m=Tk()
m.geometry("600x400")
m.title("Exercicio sete")

def somar():
    resultado = int(e.get()) + int(e2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

def subtrair():
    resultado = int(e.get()) - int(e2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

def multiplicar():
    resultado = float(e.get()) * float(e2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

def dividir():
    resultado = float(e.get()) / float(e2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

l=Label(m, text="Número 1:").pack()
e = Entry(m)
e.pack()
l=Label(m, text="Número 2:").pack()
e2 = Entry(m)
e2.pack()

btn_soma=Button(m,text="Somar",command=somar).pack()
btn_diminuir=Button(m,text="Subtrair",command=subtrair).pack()
btn_multiplicar=Button(m,text="Multiplicar",command=multiplicar).pack()
btn_dividir=Button(m,text="Dividir",command=dividir).pack()

label_resultado = Label(m, text="Resultado:")
label_resultado.pack(pady=10)

m.mainloop()
'''