import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Jogo Snake")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
azul = (0, 0, 255)
cinza = (169, 169, 169)

tamanho_quadrado = 10
velocidade_jogo = 15
vidas = 3

tipos_comida = {
    "normal": (verde, 0),
    "extra": (amarelo, 2),
    "velocidade": (azul, -1)
}

def gerar_obstaculos(qtd):
    obstaculos = []
    while len(obstaculos) < qtd:
        obs_x = random.randint(0, (largura // tamanho_quadrado) - 1) * tamanho_quadrado
        obs_y = random.randint(0, (altura // tamanho_quadrado) - 1) * tamanho_quadrado
        if [obs_x, obs_y] not in obstaculos:
            obstaculos.append([obs_x, obs_y])
    return obstaculos

def gerar_comida():
    while True:
        tipo = random.choice(list(tipos_comida.keys()))
        comida_x = random.randint(0, (largura // tamanho_quadrado) - 1) * tamanho_quadrado
        comida_y = random.randint(0, (altura // tamanho_quadrado) - 1) * tamanho_quadrado
        return comida_x, comida_y, tipo

def desenhar_comida(tamanho, comida_x, comida_y, tipo):
    cor, efeito = tipos_comida[tipo]
    pygame.draw.rect(tela, cor, [comida_x, comida_y, tamanho, tamanho])
    return efeito

def desenhar_cobra(tamanho, pixels, invencivel=False):
    for pixel in pixels:
        if invencivel:
            pygame.draw.rect(tela, (255, 165, 0), [pixel[0], pixel[1], tamanho, tamanho])
        else:
            pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, cinza, [obstaculo[0], obstaculo[1], tamanho_quadrado, tamanho_quadrado])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 15)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [10, 10])

def desenhar_tempo(tempo_inicial):
    tempo_atual = int(time.time() - tempo_inicial)
    fonte = pygame.font.SysFont("Helvetica", 15)
    texto = fonte.render(f"Tempo {tempo_atual}s", True, vermelha)
    tela.blit(texto, [largura - 100, 10])

def desenhar_vidas(vidas):
    fonte = pygame.font.SysFont("Helvetica", 15)
    texto = fonte.render(f"Vidas: {vidas}", True, vermelha)
    tela.blit(texto, [10, 28])

def selecionar_velocidade(tecla, velocidade_atual):
    if tecla == pygame.K_DOWN and velocidade_atual != (0, -tamanho_quadrado):
        return 0, tamanho_quadrado
    elif tecla == pygame.K_UP and velocidade_atual != (0, tamanho_quadrado):
        return 0, -tamanho_quadrado
    elif tecla == pygame.K_RIGHT and velocidade_atual != (-tamanho_quadrado, 0):
        return tamanho_quadrado, 0
    elif tecla == pygame.K_LEFT and velocidade_atual != (tamanho_quadrado, 0):
        return -tamanho_quadrado, 0
    return velocidade_atual

def rodar_jogo():
    global vidas, velocidade_jogo
    fim_jogo = False

    x = largura // 2
    y = altura // 2

    velocidade_x, velocidade_y = 0, 0
    tamanho_cobra = 1
    pixels = []
    obstaculos = gerar_obstaculos(8)
    comida_x, comida_y, tipo_comida = gerar_comida()

    tempo_inicial = time.time()
    tempo_invencivel = 0

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, (velocidade_x, velocidade_y))

        efeito_comida = desenhar_comida(tamanho_quadrado, comida_x, comida_y, tipo_comida)
        desenhar_obstaculos(obstaculos)

        if x < 0 or x >= largura or y < 0 or y >= altura:
            if tempo_invencivel <= time.time():
                vidas -= 1
                tempo_invencivel = time.time() + 10
                if vidas <= 0:
                    fim_jogo = True
                else:
                    x = largura // 2
                    y = altura // 2
                    velocidade_x, velocidade_y = 0, 0
                    pixels = []

        if [x, y] in obstaculos:
            if tempo_invencivel <= time.time():
                vidas -= 1
                tempo_invencivel = time.time() + 2
                if vidas <= 0:
                    fim_jogo = True
                else:
                    x = largura // 2
                    y = altura // 2
                    velocidade_x, velocidade_y = 0, 0
                    pixels = []

        x += velocidade_x
        y += velocidade_y

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                if tempo_invencivel <= time.time():
                    vidas -= 1
                    tempo_invencivel = time.time() + 2
                    if vidas <= 0:
                        fim_jogo = True
                    else:
                        x = largura // 2
                        y = altura // 2
                        velocidade_x, velocidade_y = 0, 0
                        pixels = []

        invencivel = tempo_invencivel > time.time()
        desenhar_cobra(tamanho_quadrado, pixels, invencivel)
        desenhar_pontuacao(tamanho_cobra - 1)
        desenhar_tempo(tempo_inicial)
        desenhar_vidas(vidas)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            if efeito_comida == 2:
                tamanho_cobra += 1
            elif efeito_comida == -1:
                velocidade_jogo += 2
            comida_x, comida_y, tipo_comida = gerar_comida()

        relogio.tick(velocidade_jogo)

    pygame.quit()

rodar_jogo()
