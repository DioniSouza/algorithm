#Faça um algoritmo que leia um número N e imprima “F1”, “F2” ou “F3”, conforme a condição:
#• “F1”, se N <= 10
#• “F2”, se N > 10 e N <= 100
#• “F3”, se n > 100

#Variáveis
n = int(input("digite um numero: "))

#Condições

if n <= 10:
    print("F1")
elif n > 10 and n <= 100:
    print("F2")
else:
    print("F3")
