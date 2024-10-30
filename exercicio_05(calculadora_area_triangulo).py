#Faça um algoritmo que calcule a área de um triângulo, considerando a fórmula: ÁREA = BASE * ALTURA / 2. Utilize as variáveis AREA, BASE e ALTURA e os operadores aritméticos de multiplicação e divisão.

#Definindo variáveis
base = float(input("insira a medida da base em cm: "))
altura = float(input("insira a medida da altura em cm: "))
area = (base * altura) / 2

#Imprimindo o resultado
print("A área do triângulo é: ", area, "cm²")