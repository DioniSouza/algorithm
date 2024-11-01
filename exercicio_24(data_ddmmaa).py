#Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não em uma variável do tipo data, crie um algoritmo que leia uma data no formato DDMMAA e imprima essa data no formato AAMMDD, onde:
#• A letra D corresponde a dois algarismos representando o dia;
#• A letra M corresponde a dois algarismos representando o mês;
#• A letra A corresponde aos dois últimos algarismos representando o ano.


#Variável que armazenará a data no formato DDMMAA
data= int(input("Digite a data no formato DDMMAA: "))

#Separando os algarismos da data
dia = data//10000
mes = (data%10000)//100
ano = data%100
#Calculando a data no formato AAMMDD
print(f"A data apresenta da é {dia}/{mes}/{ano}.")


