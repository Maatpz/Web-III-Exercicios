# Uma loja fornece 10% de desconto para funcionários e 5% de desconto para clientes vips. 
# Faça um programa usando while que calcule o valor total a ser pago por uma pessoa. 
# O programa deverá ler o valor total da compra efetuada e um código que identifique
#  se o comprador é um cliente comum (1), funcionário (2) ou vip(3) .

'''''
(valor_compra!=0):
 while True:
   valor_compra=float(input('valor da compra:'))
   tipo_cliente=int(input('cliente comum(1), funcionário(2) ou vip(3):'))
   if tipo_cliente==1:
     print(f'valor total: {valor_compra}')
   elif tipo_cliente==2:
     print(f"valor total: {valor_compra*0.90}")
   elif tipo_cliente==3:
     print(f"valor total: {valor_compra*0.95}")
   else:
     print("fim")
     break
'''