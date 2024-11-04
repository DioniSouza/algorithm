#Escreva um algoritmo que determine o número de dias que uma pessoa já viveu. Considere que um mês tenha 30 dias.
from datetime import date

# Variáveis
dia_nasc = int(input('Digite seu dia de nascimento: '))
mes_nasc = int(input('Digite seu mês de nascimento: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))



# Calculando o dia, mês e ano atual
dia_atual = date.today().day
mes_atual = date.today().month
ano_atual = date.today().year

# Calculando a idade em dias
idade_dias = (ano_atual - ano_nasc) * 365 + (mes_atual - mes_nasc) * 30 + (dia_atual - dia_nasc)

# Apresentando a idade em dias
print('Você já viveu', idade_dias, 'dias.')
