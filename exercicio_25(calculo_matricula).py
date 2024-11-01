#Suponha que uma escola utilize, como código de matrícula, um número inteiro no formato AASDDD, onde:
#• Os dois primeiros dígitos, representados pela letra A, são os dois últimos algarismos do ano da matrícula;
#• O terceiro dígito, representado pela letra S, vale 1 ou 2, conforme o aluno tenha se matriculado no 1º ou 2º semestre;
#• Os quatro últimos dígitos, representados pela letra D, correspondem à ordem da matrícula do aluno, no semestre e no ano em questão. Crie um algoritmo que leia o número de matrícula de um aluno e imprima o ano e o semestre em que ele foi matriculado.


#Variável que armazenará o número de matrícula
matricula = input("Digite o número de matrícula:(onde AA S DDDD) ")

#Separando os algarismos da matrícula
ano = matricula[:2]
semestre = matricula[2]
ordem = matricula[3:]

#Imprimindo o ano e o semestre
print(f"O aluno foi matriculado no ano {ano} e no semestre {semestre}.")