from tkinter import *

#4. Implemente uma interface com três caixas de seleção (CheckButton): "Python", "Java" e
#"C++". O usuário pode selecionar mais de uma linguagem. Após clicar no botão "Confirmar",
#exiba as linguagens selecionadas em um Label.

'''
m = Tk()
m.title("Selecionar Linguagens")
m.geometry("300x200")

def exibir_linguagens():
    linguagens_selecionadas = []

    if v_python.get() == 1:
        linguagens_selecionadas.append("Python")
    if v_java.get() == 1:
        linguagens_selecionadas.append("Java")
    if v_cpp.get() == 1:
        linguagens_selecionadas.append("C++")

    # Atualiza o Label com as linguagens selecionadas
    if linguagens_selecionadas:
        label_resultado.config(text="Linguagens selecionadas: " + ", ".join(linguagens_selecionadas))
    else:
        label_resultado.config(text="Nenhuma linguagem selecionada")

v_python = IntVar()
v_java = IntVar()
v_cpp = IntVar()

cx_python = Checkbutton(m, text="Python", variable=v_python)
cx_python.pack()

cx_java = Checkbutton(m, text="Java", variable=v_java)
cx_java.pack()

cx_cpp = Checkbutton(m, text="C++", variable=v_cpp)
cx_cpp.pack()

btn_confirmar = Button(m, text="Confirmar", command=exibir_linguagens)
btn_confirmar.pack(pady=10)

label_resultado = Label(m, text="")
label_resultado.pack(pady=10)

m.mainloop()
'''