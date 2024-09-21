from tkinter import *

#8. Crie um programa que contenha uma lista de 10 itens em um Listbox. Adicione uma barra
#de rolagem (Scrollbar) para que o usuário possa navegar pela lista. Permita que o usuário
#selecione um item e exiba o item selecionado em um Label.

#Rever codigo para entender

'''
m=Tk()
m.geometry("500x500")
m.title("Exercicio oito")
scroll = Scrollbar(m)
scroll.pack(fill=Y)
def item_selecionado():
    item = lista.get(ACTIVE)
    label_selecionado.config(text="Item selecionado: " + item)

lista = Listbox(m, yscrollcommand=scroll.set)
lista.pack(pady=10)

itens = ['AC', 'AL', 'RJ', 'SP', 'TH', 'YU', 'KO', 'JP', 'AM', 'BR', 'SG']

for i, item in enumerate(itens):
    lista.insert(i, item)

scroll.config(command=lista.yview)

btn = Button(m, text="Mostrar Seleção", command=item_selecionado,pady=10)
btn.pack()

label_selecionado = Label(m, text="Item selecionado: ")
label_selecionado.pack(pady=10)

m.mainloop()
'''

'''
lista = Listbox(m)
lista.insert(0,'AC')
lista.insert(1,'AL')
lista.insert(2,'RJ')
lista.insert(3,'SP')
lista.insert(4,'TH')
lista.insert(5,'YU')
lista.insert(6,'KO')
lista.insert(7,'JP')
lista.insert(8,'AM')
lista.insert(9,'BR')
lista.insert(10,'SG')
lista.pack()
'''