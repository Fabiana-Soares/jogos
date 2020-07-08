import random  #Para gerar um número aleatório no nosso jogo, a primeira coisa que devemos fazer é importar o seu módulo,

print("##################################")
print("Bem vindo ao jogo de adivinhacao!")
print("##################################")

numero_secreto = random.randrange(1,101)
## numero_secreto = 42 ##decomentar quando nao estiver usando o RANDOM
total_de_tetativas = 3
##rodada = 1 ##caso use o while descomentar

print(numero_secreto)

##while(rodada <= total_de_tetativas): ##pode usar o FOR tambem. Caso for usar o FOR. Pesquisar>> for rodada in range(1, total_de_tetativas + 1)
    ##print("Tetativa", rodada, "de", total_de_tetativas) podemos usar outra forma de escrever o print. Colocando string interpolation(uma funcao chamada .format, para fazer uma substituicao). Veja o exemplo abaixo:
  ##  print("Tetativa {} de {}" .format(rodada, total_de_tetativas))
  ##  chute_str = input("Digite o seu numero: ")
  ##  print("Voce digitou ", chute_str)
  ## chute = int(chute_str)

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
        break ## sai do laco, nao continua rodando depois que acertou e funciona com o WHILE tambem.
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce errou! O seu chute foi menor do que o numero secreto")
   ## rodada = rodada + 1 ## caso use o WHILE descomentar

    print("Fim do Jogo!!!")

    ##Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.

    ##O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.