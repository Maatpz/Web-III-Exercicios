#2. Desenvolva um programa que pergunte a distância de uma viagem em Km.Calcule o preço da passagem, 
# cobrando R$0,50 por KM para viagens de até 200Km e R$0,45 para viagens mais longas.

'''''
distancia = float(input('distancia da viagem Km: '))
 if distancia <= 200:
    print(f"O preço e: {distancia*0.45}")
 elif distancia > 200:
    print(f"O preço e : {distancia*0.50}")
print("Boa viajem")
'''