import random

print("##################################")
print("Bem vindo ao jogo de adivinhacao!")
print("##################################")

numero_secreto = random.randrange(1,101)
total_de_tetativas = 0

print("Qual o nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input ("Define um nivel: "))

if(nivel == 1):
    total_de_tetativas = 5
elif(nivel == 2):
    total_de_tetativas = 3
else:
    total_de_tetativas = 2

for rodada in range(1, total_de_tetativas + 1):
    print("Tetativa {} de {}".format(rodada, total_de_tetativas))
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero ente 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Voce acertou!!")
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce errou! O seu chute foi menor do que o numero secreto")

    print("Fim do Jogo!!!")
