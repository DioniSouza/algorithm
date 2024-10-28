#jogo de advinhar numeros
import random

#definição
secret_number = random.randint(1,100)
tries = 0
limit_tries = 5

#Início
player_name = input("Qual seu nome?")
print(f"Bem-vindo, {player_name} ao jogo de adivinhação!")
print(f" Vamos lá {player_name}, tente advinhar meu número! Ele está entre 1 e 100.")

while tries < limit_tries:
    guess = int(input("Pronto? então digite um número: "))
    tries += 1

    if guess < secret_number:
        print(f"Você errou! O número secreto é maior.")
    elif guess > secret_number:
        print(f"Você errou! O número secreto é menor.")
    else:
        print(f"Parabéns {player_name}! Você acertou!")
        break