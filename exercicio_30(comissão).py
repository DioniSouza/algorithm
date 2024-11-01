#Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório contendo nome, valor da venda e comissão de cada um dos corretores. O relatório deve mostrar também o total de vendas da empresa

#Variáveis
corretor_1 = str(input("Digite o nome do primeiro corretor: "))
resultado_1 = float(input("Insira o resultado do primeiro corretor: "))
corretor_2 = str(input("Digite o nome do segundo corretor: "))
resultado_2 = float(input("Insira o resultado do segundo corretor: ")) 
corretor_3 = str(input("Digite o nome do terceiro corretor: "))
resultado_3 = float(input("Insira o resultado do terceiro corretor: "))
total_vendas = resultado_1 + resultado_2 + resultado_3 
#Resolução
if 