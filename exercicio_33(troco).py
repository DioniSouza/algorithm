#Suponha que um caixa disponha apenas de notas de 1, 10 e 100 reais. Considerando que alguém está pagando uma compra, escreva um algoritmo que mostre o número mínimo de notas que o caixa deve fornecer como troco. Mostre também: o valor da compra, o valor do troco e a quantidade de cada tipo de nota do troco. Suponha que o sistema monetário não utilize moedas.

#variaveis
valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor que o cliente pagou: "))
valor_troco = valor_pago - valor_compra

#notas de 100 reais
quant_100 = int(valor_troco // 100)
int(valor_troco % 100)

#notas de 10 reais
quant_10 = valor_troco // 10
valor_troco % 10

#notas de 1 reais
quant_1 = int(valor_troco // 1)

#apresentacao
print(f"Valor da compra: R${valor_compra}")
print(f"Valor do troco: R${valor_troco}")
print("Trocos possiveis")
print(f"Notas de 100 reais: {quant_100}")
print(f"Notas de 10 reais: {quant_10}")
print(f"Notas de 1 reais: {quant_1}")