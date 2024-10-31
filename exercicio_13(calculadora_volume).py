#Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do volume de uma caixa retangular. Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.

#Reunião de variáveis
print(f"Calculdora de volume de onjetos.")
comprimento = float(input("Digite um valor do comprimento em cm: "))
largura = float(input("Digite um valor da largura em cm: "))
altura = float(input("Digite um valor da altura em cm: "))

#Cálculo de volume
volume = comprimento * largura * altura

#Apresentação do resultado
print(f"O volume da caixa retangular é: ", volume, "cm³")