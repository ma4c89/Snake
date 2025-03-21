import random
import time


# Função para simular a barra de carregamento
def barra():
    carga_maxima = 50
    print("Carregando o programa:\n[", end="")
    for b in range(carga_maxima + 1):
        time.sleep(0.1)  # Atraso de 100ms
        print("-", end="", flush=True)  # Mantém o progresso visível
    print(">]")
    print("Concluído\n")
    time.sleep(1)


# Função principal do jogo
def jogar():
    jogador = 0
    computador = 0
    continuar = 's'

    barra()

    print("\t+----------------------------------------------------+")
    print("\t|                                                    |")
    print("\t|\t\tBEM-VINDO AO JOGO 21 CONTRA O COMPUTADOR!    |")
    print("\t|                                                    |")
    print("\t+----------------------------------------------------+\n")

    while continuar.lower() == 's':
        # Jogador pega uma carta
        carta = random.randint(1, 10)
        jogador += carta
        print(f"Você recebeu uma carta: {carta}")
        print(f"Pontuação atual do jogador: {jogador}")

        if jogador > 21:
            print("Você estourou! Computador vence!")
            return

        # Computador pega uma carta
        carta = random.randint(1, 10)
        computador += carta
        print(f"O computador recebeu uma carta: {carta}")
        print(f"Pontuação atual do computador: {computador}")

        if computador > 21:
            print("O computador estourou! Você vence!")
            return

        # Pergunta ao jogador se ele quer continuar
        continuar = input("\nDeseja continuar jogando? (s/n): ")

    if jogador > computador:
        print("Você venceu!")
    elif jogador < computador:
        print("O computador venceu!")
    else:
        print("Empate!")


# Chama a função principal
jogar()
