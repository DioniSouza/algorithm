#Faça um algoritmo que calcule a quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

#coleta de variaveis
tempo = int(input("Insira o tempo decorrido no percursso: "))
velo = int(input("Digite a velocidade media durante o percursso, em quilometros: "))
lkm = int(input("Digite a media de consumo de seu veiculo em litros: ")) #mudei para o usuario colocar a media de seu veiculo
dist = tempo * velo
litros = dist / lkm

#Apresentação
print("A distancia percorrida foi: ", dist)
print("Sua media de consumo de combustivel foi: ",litros)