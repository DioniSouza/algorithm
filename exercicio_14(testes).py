#Faça um algoritmo que leia quatro números e apresente os resultados de adição e multiplicação dos valores entre si, baseando-se na utilização da propriedade distributiva, ou seja, se forem lidas as variáveis A, B, C e D, devem ser somadas e multiplicadas A com B, A com C e A com D; B com C, B com D e por último C com D.

#Coleta de dados
print ("Calculadora de propiedade distribuitiva.")
a = int(input("Digite um número para A: "))
b = int(input("Digite outro número B: "))
c = int(input("Digite um outro número C: "))
d = int(input("Digite o último número D: "))

#Cálculos
soma = (a + b) + (a + c) + (a + d) + (b + c) + (b + d) + (c + d)
mult = (a * b) + (a * c) + (a * d) + (b * c) + (b * d) + (c * d)

#Apresentação dos dados
print ("A soma dos resultados da propiedade distributiva de soma é: ", soma)
print ("A multiplicação dos resultados da propiedade distributiva de multiplicação é: ", mult)
