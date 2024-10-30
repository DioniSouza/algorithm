#Faça um algoritmo que:
#a) Obtenha o valor para a variável HT (horas trabalhadas no mês);
#b) Obtenha o valor para a variável VH (valor hora trabalhada):
#c) Obtenha o valor para a variável PD (percentual de desconto);
#d) Calcule o salário bruto => SB = HT * VH;
#e) Calcule o total de desconto => TD = (PD/100)*SB;
#f) Calcule o salário líquido => SL = SB – TD;
#g) Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário Liquido.

#Coleta das variaveis
HT = float(input("Digite a quantidade de horas trabalhadas no mês: "))
VH = float(input("Digite o valor da hora trabalhada: "))
PD = float(input("Digite o percentual de desconto: "))

#Calculo do salario bruto
SB = HT * VH

#Calculo do total de desconto
TD = (PD/100) * SB

#Calculo do salario liquido
SL = SB - TD

#Apresentacao dos dados
print("Horas trabalhadas: ", HT)
print("Salário Bruto: ", SB)
print("Desconto: ", TD)
print("Salário Liquido: ", SL)

