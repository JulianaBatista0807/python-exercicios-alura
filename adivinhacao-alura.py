print ("*" * 33)
print ("Bem vindo ao jogo de Adivinhação!")
print ("*********************************")

numero_secreto = 13

total_de_tentativas = 3
rodada = 1

while (total_de_tentativas > 0):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = str(input("Digite o seu número: "))

    print ("Você digitou: ", chute_str)
    chute = int(chute_str)

if (chute == numero_secreto):

    print("Você acertou!")
else:
    if( chute > numero_secreto):
        print("O seu chute foi maior do que o número secreto!")
    elif(chute < numero_secreto):
        print("O seu chute foi menor do que o número secreto!")
    rodada = rodada + 1

print("Fim do jogo")