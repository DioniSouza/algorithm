#Considere a seguinte situação: descontam-se inicialmente 10% do salário bruto do trabalhador como contribuição à previdência social. Após esse desconto, há um outro desconto de 5% sobre o valor restante do salário bruto, a título de um determinado imposto. Faça um algoritmo que leia o salário bruto de um cidadão e imprima o seu salário líquido.

#Variaveis
print("Calculadora de  descontos de salario.")
salario_bruto = float(input("Digite o valor do salario bruto: R$"))
inss = (salario_bruto / 100) *10
salario_inss = salario_bruto - inss
imposto = (salario_inss / 100) * 5
salario_liquido = salario_inss - imposto

#Apresentação
print(f"Salário liquido após os descontos de R${inss}, relativo a inss e R${imposto}, relativo ao imposto descontado é R${salario_liquido}")
