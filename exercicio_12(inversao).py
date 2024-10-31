#Faça um algoritmo que leia dois valores para as variáveis A e B e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresente os valores trocados.

#Reunião de dados
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))

#Troca de valores
a, b = b, a

#Apresentação dos dados
print("Os valores trocados são: A =", a, "e B =", b)
