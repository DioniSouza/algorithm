#Faça um algoritmo que leia dois números inteiros (Int1 e Int2) e imprima o quociente e o resto da divisão inteira de Int1 por Int2.

#Variáveis
print("Calculadora de divisão com apresentação de quociente e resto.")
int1 = int(input("Digite o valor a ser dividido: "))
int2 = int(input("Digite o valor do divisor: "))

#Resolução
quociente = int1 // int2
resto = int1 % int2

#Apresentação
print(f"A solução da expressão é {quociente} e o resto {resto}.")
