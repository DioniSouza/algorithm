#Dado um número de três algarismos N = CDU (onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é, M = UDC. Gerar M a partir de N (p.ex.: N = 123 -> M = 321).

#Variaveis
n = int(input("Digite um numero de três algarismos: "))

#Separando os algarismos
c = n // 100
d = (n // 10) % 10
u = n % 10  

#Gerando M
m = u * 100 + d * 10 + c
#Apresentando M
print(f"O numero invertido é: {m}")
