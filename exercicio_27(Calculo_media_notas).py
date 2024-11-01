#O sistema de avaliação de determinada disciplina, é composto por três provas. Aprimeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Faça um algoritmo para calcular a média final de um aluno desta disciplina.

#Variáveis
prova_1 = float(input("Insira a nota da primeira prova: "))
prova_2 = float(input("Digite a nota da segunda prova: "))
prova_3 = float(input("Digite a nota da terceia prova: "))

#Resolução
media = ((prova_1 * 2) + (prova_2 * 3) + (prova_3 * 5)) / (2 + 3 + 5)

#Apresentação
print(f"A media do aluno é {media}.")

