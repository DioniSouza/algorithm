#Faça um algoritmo que leia a velocidade de um veículo em km/h e calcule e imprima a velocidade em m/s (metros por segundo).

#Variáveis
print(f"Calculdora de conversçao de KM/h para M/s")
kmh = float(input("Digite a velocidade do veículo em KM/h: "))

#Resolução
ms = kmh / 3.6

#Apresentação
print(f"{kmh} km/h é equivalente a {ms} metros por segundo.")