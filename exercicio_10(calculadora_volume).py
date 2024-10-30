#Faça um algoritmo que calcule e apresente o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME = 3,14159 * RAIO2 * ALTURA.

#reunião das variaveis
raio = float(input("Digite o raio da lata de óleo (em cm): "))
altura = float(input("Digite a altura da lata de óleo (em cm): "))

#calculo do volume
volume = 3.14159 * (raio ** 2 ) * altura

#apresentacao do resultado
print("O volume da lata de óleo é: ", volume, "cm³")
