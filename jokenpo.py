from random import randint
from time import sleep
resposta = "s"
lista = [0, 1, 2]
itens = ('Pedra', 'Papel', 'Tesousa')
pontojogador = 0
pontomaquina = 0
rodadas = 0
maquina = randint(0, 2)

while resposta == 's' or resposta == 'S':
    print('=-=' * 11)
    print("Vamos jogar um jokenpô ?")
    print("Escolha entre uma das opções: \n"
                        "[0] Pedra \n"
                        "[1] Papel \n"
                        "[2] Tesoura")
    jogador = int(input("Qual a sua jogada ?: "))
    while jogador not in lista:
        jogador = int(input("Numero invalido, digite novamente: "))
    print(f'O Jogador  escolheu {(itens[jogador])}')
    print("Processando...")
    sleep(3)
    print(f'A Maquina escolheu {(itens[maquina])}')
    if maquina == 0:   #pedra#
        if jogador == 0:
            print("Foi um Empate")
        elif jogador == 1:
            print("O Jogador venceu")
            pontojogador += 1
        elif jogador == 2:
            print('O Jogador perdeu')
            pontomaquina += 1
        else:
            print('Resposta invalida')
    if maquina == 1:   #papel#
        if jogador == 0:
            print('O jogador perdeu')
            pontomaquina += 1
        elif jogador == 1:
            print('Foi um Empate')
        elif jogador == 2:
            print('O Jogador venceu')
            pontojogador += 1
        else:
            print('Resposta invalida')
    if maquina == 2:   #tesoura#
        if jogador == 0:
            print('O Jogador venceu')
            pontojogador += 1
        elif jogador == 1:
            print('O Jogador perdeu')
            pontomaquina += 1
        elif jogador == 2:
            print('Foi um Empate')
        else:
            print('Resposta invalida')

    rodadas += 1
    print(f'Placar: Jogador {pontojogador} x {pontomaquina} Máquina')

    if rodadas >= 3:
        if pontojogador > pontomaquina:
            print("Você ganhou a melhor de 3!")
        elif pontojogador < pontomaquina:
            print("A máquina ganhou a melhor de 3!")
    print('=-=' * 11)

    resposta = input("Deseja jogar novamente ? S/N: ")
print("programa encerrado ")
