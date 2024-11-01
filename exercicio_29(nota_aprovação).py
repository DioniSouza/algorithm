#Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:
#a) o nome e as notas em cada prova do candidato
#b) a média do candidato
#c) uma informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0

#Variáveis
nome = str(input("Digite o nome do candidato: "))
nota_portugues = float(input("Digite a nota da prova de Português: "))
nota_matematica = float(input("Digite a nota da prova de matemática: "))
nota_conhecimento = float(input("Digite a nota da prova de conhecimentos gerais:"))
media = (nota_portugues + nota_matematica + nota_conhecimento) / 3

#Verificação de aprovação
aprovado = True
if media > 7 or nota_portugues < 5 or nota_matematica < 5 or nota_conhecimento < 5:
    aprovado = False

#Apresentção
print(f"Nome do candidato: {nome}")
print(f"nota em portugues: {nota_portugues}")
print(f"Nota em matemática: {nota_matematica}")
print(f"Nota em conhecimentos gerais: {nota_conhecimento}")
print(f"Sua média: {media}")

if aprovado:
     print(f"Parabéns voce está aprovado!")
else:
     print(f"Infelizmente voce está reprovado!")
