#uma  empresa  produz  três  tipos  de  peças  mecânicas:  parafusos,  porcas  e  arruelas.  Têm-se  os  preços  unitários  de  cada  tipo  de peça  e  sabe-se  que  sobre estes preços incidem descontos de 10% para porcas, 20% para parafusos e 30% para  arruelas.  Escreva  um  algoritmo  que  calcule  o  valor  total  da  compra  de  um cliente.  Deve  ser  mostrado  o  nome  do  cliente.  O  número de  cada  tipo  de  peça que o mesmo comprou, o total de desconto e o total a pagar pela compra. 


#variaveis
cliente = input("Digite o nome do cliente: ")
qtd_parafuso = int(input("Digite a quantidade de parafusos: "))
qtd_porca = int(input("Digite a quantidade de porcas: "))
qtd_arruela = int(input("Digite a quantidade de arruelas: "))

#precos unitarios
preco_parafuso = 1.00
preco_porca = .50
preco_arruela = .25

#total precos
total_parafuso = qtd_parafuso * preco_parafuso
total_porca = qtd_porca * preco_porca
total_arruela = qtd_arruela * preco_arruela

#descontos
desconto_parafuso = total_parafuso * 0.20
desconto_porca = total_porca * 0.10
desconto_arruela = total_arruela * 0.30

#total compras
total_compra = total_parafuso + total_porca + total_arruela
total_descontos = (total_parafuso - desconto_parafuso) + (total_porca - desconto_porca) + (total_arruela - desconto_arruela)

#total a pagar
total_a_pagar = total_compra - total_descontos

#apresentacao
print(f"Cliente: {cliente}")
print(f"Total de parafusos: {qtd_parafuso} unidades")
print(f"Total de parafusos: R${total_parafuso}")
print(f"Total de descontos no parafuso{desconto_parafuso}: ")
print(f"Total de porcas: {qtd_porca} unidades")
print(f"Total de porcas: {qtd_porca}")
print(f"Total de descontos no porca: {desconto_porca}: ")
print(f"Total de arruelas: {qtd_arruela} unidades")
print(f"Total de arruelas: {qtd_arruela}")
print(f"Total de descontos nas arruelas{desconto_arruela}: ")
print(f"Total de compra: R${total_compra}")
print(f"Total de descontos: R${total_descontos}")
print(f"Total a pagar: R${total_a_pagar}")
