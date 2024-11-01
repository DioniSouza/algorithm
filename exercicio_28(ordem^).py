#Construa um algoritmo que receba como entrada três valores e os imprima em ordem crescente.

#Variáveis
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

#Resolução
valores = [numero_1,numero_2, numero_3]
valores.sort()

#Apresentação
print(f"Os valores digitados em ordem crescente são: {valores[0]}, {valores[1]}, {valores[2]}")