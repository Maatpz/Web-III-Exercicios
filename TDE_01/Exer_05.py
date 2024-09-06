#5. Crie um programa que leia o nome completo de uma pessoa e mostre:
#a) O nome com todas as letras maiúsculas e minúsculas
#b) Quantas letras ao todo
#c) Quantas letras tem o primeiro nome

'''
full_Name=input("Digite seu nome: ")
print(full_Name.upper())
print(full_Name.lower())
print(len(full_Name))

first_name = full_Name.split()[0]
total_lyrics = len(first_name)
print(total_lyrics)

'''