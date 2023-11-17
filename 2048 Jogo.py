import random
import os
import keyboard
import time


def iniciar_jogo():
    return [[0] * 4 for _ in range(4)]


def adicionar_numero(tabuleiro):
    vazio = [(i, j) for i in range(4)
             for j in range(4) if tabuleiro[i][j] == 0]
    if vazio:
        i, j = random.choice(vazio)
        tabuleiro[i][j] = random.choice([2, 4])


def imprimir_tabuleiro(tabuleiro):
    os.system('cls' if os.name == 'nt' else 'clear')
    for linha in tabuleiro:
        print(' '.join(str(num) if num != 0 else '.' for num in linha))
    print()


def mover(tabuleiro, direcao):
    pontuacao = 0
    if direcao == 'cima':
        for j in range(4):
            coluna = [tabuleiro[i][j] for i in range(4)]
            coluna = fundir(coluna)
            for i in range(4):
                tabuleiro[i][j] = coluna[i]
    elif direcao == 'baixo':
        for j in range(4):
            coluna = [tabuleiro[i][j] for i in range(3, -1, -1)]
            coluna = fundir(coluna)
            for i in range(4):
                tabuleiro[i][j] = coluna[3 - i]
    elif direcao == 'esquerda':
        for i in range(4):
            linha = tabuleiro[i]
            linha = fundir(linha)
            tabuleiro[i] = linha
    elif direcao == 'direita':
        for i in range(4):
            linha = tabuleiro[i][::-1]
            linha = fundir(linha)
            tabuleiro[i] = linha[::-1]

    adicionar_numero(tabuleiro)
    return tabuleiro


def fundir(lista):
    nova_lista = [0] * 4
    index = 0
    for i in range(4):
        if lista[i] != 0:
            if nova_lista[index] == 0:
                nova_lista[index] = lista[i]
            elif nova_lista[index] == lista[i]:
                nova_lista[index] *= 2
                index += 1
            else:
                index += 1
                nova_lista[index] = lista[i]
    return nova_lista


def verificar_fim_de_jogo(tabuleiro):
    movimentos = ['cima', 'baixo', 'esquerda', 'direita']
    for movimento in movimentos:
        novo_tabuleiro = [linha.copy() for linha in tabuleiro]
        if mover(novo_tabuleiro, movimento) != tabuleiro:
            return False
    return True


def obter_direcao():
    try:
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'up':
                    return 'cima'
                elif event.name == 'down':
                    return 'baixo'
                elif event.name == 'left':
                    return 'esquerda'
                elif event.name == 'right':
                    return 'direita'
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    tabuleiro = iniciar_jogo()

    while not verificar_fim_de_jogo(tabuleiro):
        imprimir_tabuleiro(tabuleiro)
        # Adiciona um pequeno atraso para melhorar a experiência do usuário
        time.sleep(0.1)
        direcao = obter_direcao()

        if direcao in ['cima', 'baixo', 'esquerda', 'direita']:
            tabuleiro = mover([linha.copy() for linha in tabuleiro], direcao)
        else:
            print("Entrada inválida. Tente novamente.")

    print("Fim de jogo!")
