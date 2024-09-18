import random

tabuleiro = [['   ', '   ', '   '], ['   ', '   ', '   '],
             ['   ', '   ', '   ']]


def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 11)


def movimento_humano(tabuleiro):
    while True:
        try:
            linha = int(input('Escolha a linha (0, 1, 2): '))
            coluna = int(input('Escolha a coluna (0, 1, 2): '))
            if tabuleiro[linha][coluna] == '   ':
                return linha, coluna
            else:
                print('Esta casa está ocupada')
        except (ValueError, IndexError):
            print('Entrada inválida! Utilize apenas números entre 0 a 2.')


def movimento_bot(tabuleiro, bot, jogador):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '   ':
                tabuleiro[linha][coluna] = jogador
                if verifica_vencedor(tabuleiro) == jogador:
                    tabuleiro[linha][coluna] = '   '
                    return linha, coluna
                tabuleiro[linha][coluna] = '   '

    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == '   ':
            return linha, coluna


def verifica_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != '   ':
            return linha[0]

    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != '   ':
            return tabuleiro[0][col]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '   ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '   ':
        return tabuleiro[0][2]

    for linha in tabuleiro:
        if '   ' in linha:
            return None

    return 'Empate'


jogador = ' X '
bot = ' O '

while True:
    print(f'Turno do Jogador {jogador}')
    exibe_tabuleiro(tabuleiro)
    x, y = movimento_humano(tabuleiro)
    tabuleiro[x][y] = jogador

    vencedor = verifica_vencedor(tabuleiro)
    if vencedor:
        exibe_tabuleiro(tabuleiro)
        if vencedor == 'Empate':
            print('O jogo terminou em empate!')
        else:
            print(f'O jogador {vencedor} venceu!')
        break

    print(f'Turno do Bot {bot}')
    x, y = movimento_bot(tabuleiro, bot, jogador)
    tabuleiro[x][y] = bot

    vencedor = verifica_vencedor(tabuleiro)
    if vencedor:
        exibe_tabuleiro(tabuleiro)
        if vencedor == 'Empate':
            print('O jogo terminou em empate!')
        else:
            print(f'O jogador {vencedor} venceu!')
        break