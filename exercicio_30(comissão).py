#Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório contendo nome, valor da venda e comissão de cada um dos corretores. O relatório deve mostrar também o total de vendas da empresa

#lista de corretores
corretores = []

#loop
for i in range(3):
    nome = str(input(f"Digite o nome do corretor {i+1}: "))
    valor_venda = float(input(f"Digite o resultado do Corretor {i+1}: "))

#Calcúlo
if valor_venda > 50000:
    comissao = valor_venda * 0.12
elif valor_venda >=30000:
    comissao = valor_venda * 0.095
else:
    comissao = valor_venda * 0.075
    
#Adicionar os dados do corretor a lista
corretores.append({"nome":nome, "valor_venda": valor_venda, "comissao": comissao})

#total de vendas
total_vendas = 0
for corretor in corretores:
    total_vendas += corretor["valor_venda"]
    
#imprimindo resultado
print("Relatório de Vendas:")
print("-" * 30)
print("Corretor | Valor da Venda | Comissão")
print("-" *30)
for corretor in corretores:
    print(f"{corretor['nome']} | R$ {corretor['valor_venda']:.2f} | R$ {corretor['comissao']:.2f}")
    print("-" * 30)
    print(f"Total de Vendas: R$ {total_vendas:}")
