#9. Faça um algoritmo que:
#a) Leia o nome;
#b) Leia o sobrenome;
#c) Concatene o nome com o sobrenome;
#) Apresente o nome completo.

#desenvolvimento
nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
nome_completo = nome + " " + sobrenome

#Apresentação dos dados
print("Nome completo: ", nome_completo)