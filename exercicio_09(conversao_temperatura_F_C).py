#Faça um algoritmo que leia uma temperatura em Fahrenheit e a apresente convertida em graus Celsius. A fórmula de conversão é C = (F – 32) * ( 5 / 9), na qual F é a temperatura em Fahrenheit e C é a temperatura em Celcius.

#Coleta de dados
f = float(input("Digite a temperatura em Fahrenheit: "))

#Conversão de temperatura
c = (f - 32) * (5 / 9)

#Apresentação dos dados
print(" Atemperatura em ºC é: ", c)