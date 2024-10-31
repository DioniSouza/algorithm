#Leia um código de cinco algarismos (variável Codigo) e gere o digito verificador (DigitoV) módulo 7 para o mesmo. Supondo que os cinco algarismos do código são ABCDE, uma forma de calcular o dígito desejado, com módulo 7 é: DigitoV = resto da divisão de S por 7, onde S = 6*A + 5*B + 4*C + 3*D + 2*E

#Variaveis
codigo = input("Digite os 5 digitos do codigo: ")

#Declarando os numeros
A = int(codigo[0])
B = int(codigo[1])
C = int(codigo[2])
D = int(codigo[3])
E = int(codigo[4])

#Calculando o somatorio
S = 6*A + 5*B + 4*C + 3*D + 2*E

#Calculando o resto da divisao por 7
resto = S % 7

#Calculando o digito verificador
DigitoV = 7 - resto

#Apresentando o digito verificador
print(f"O digito verificador do codigo {codigo} é: {DigitoV}")
