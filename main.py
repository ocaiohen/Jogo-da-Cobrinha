import pygame
from math import floor
# from pygame import mixer
import random

pygame.init()
pygame.display.set_caption("Snake")
largura, altura = 1200, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
#cores rgb
corFundo = (0,0,0)
corComida = (255,255,255)
corCobra = (0,255,0)
corTexto = (255,255,255)
#parametros cobra
tamanhoQuadrado = 20
velocidadeDeAtualizacao = 15

# mixer.init()
# mixer.music.load("./Sons/Música Bomba Patch.mpeg")
# mixer.music.set_volume(0.2)
# mixer.music.play(10)
# somComer = mixer.Sound("./Sons/Som Comer.wav")

def gerarComida():
    xComida = floor(random.randrange(10, largura - 1) / float(tamanhoQuadrado)) * float(tamanhoQuadrado)
    yComida = floor(random.randrange(10, altura - 1) / float(tamanhoQuadrado)) * float(tamanhoQuadrado)
    return xComida, yComida
def desenharComida(tamanho, coordenadasComida):
    xComida, yComida = coordenadasComida[0], coordenadasComida[1]
    pygame.draw.rect(tela, corComida, [xComida, yComida, tamanho, tamanho])
    # fonte = pygame.font.SysFont("Roboto", 35)
    # texto = fonte.render(f"X: {xComida}, Y: {yComida}", True, corTexto)
    # tela.blit(texto, [largura/2, altura/2])
def desenharCobra(tamanho, pixels):
    for i in range(len(pixels)):
        pygame.draw.rect(tela, corCobra, [pixels[i][0], pixels[i][1], tamanho, tamanho])

def desenharPontuacao(pontuacao):
    fonte = pygame.font.SysFont("Roboto", 35)
    texto = fonte.render(f"Score: {pontuacao}", True, corTexto)
    tela.blit(texto, [2,2])
# def imprimirPixels(pixels):
#     fonte = pygame.font.SysFont("Roboto", 35)
#     texto = fonte.render(f"{pixels}", True, corTexto)
#     tela.blit(texto, [largura/2, altura / 2])

def selecionarVelocidade(tecla, velocidadeX, velocidadeY):
    if(tecla == pygame.K_DOWN and velocidadeY != -tamanhoQuadrado):
        velocidadeX = 0
        velocidadeY = tamanhoQuadrado
    elif(tecla == pygame.K_UP and velocidadeY != tamanhoQuadrado):
        velocidadeX = 0
        velocidadeY = -tamanhoQuadrado
    elif(tecla == pygame.K_RIGHT and velocidadeX != -tamanhoQuadrado):
        velocidadeX = tamanhoQuadrado
        velocidadeY = 0
    elif(tecla == pygame.K_LEFT and velocidadeX != tamanhoQuadrado):
        velocidadeX = -tamanhoQuadrado
        velocidadeY = 0
    return velocidadeX, velocidadeY
def gameOver():
    fonte = pygame.font.SysFont("Roboto", 50)
    texto = fonte.render(f"GAME OVER!", True, (255,0,0))
    tela.blit(texto, [largura/2, altura/2])

def rodarJogo():
    fimDeJogo = False
    x = largura / 2
    y = altura / 2
    velocidadeX = 0
    velocidadeY = 0
    tamanhoCobra = 1
    pixelsCobra = []

    comidaX, comidaY = gerarComida()

    while fimDeJogo == False:
        tela.fill(corFundo)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fimDeJogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidadeX, velocidadeY = selecionarVelocidade(evento.key, velocidadeX, velocidadeY)

        #desenha comida
        desenharComida(tamanhoQuadrado, (comidaX,comidaY))

        if x < 0 or x >= largura or y < 0 or y >= altura:
            gameOver()
            fimDeJogo = True

        x += velocidadeX
        y += velocidadeY

        #desenha cobra
        pixelsCobra.append([x,y]) # adiciona a cabeça da cobra aos pixels

        if len(pixelsCobra) > tamanhoCobra: # apaga o rabo da cobra
            del pixelsCobra[0]

        for pixel in pixelsCobra[:-1]: # verifica se a cabeça e o corpo colidiram
            if pixel == [x,y]:
                gameOver()
                fimDeJogo = True

        desenharCobra(tamanhoQuadrado, pixelsCobra)
        # imprimirPixels(pixelsCobra)
        desenharPontuacao(tamanhoCobra - 1)
        pygame.display.update()

        if x == comidaX and y == comidaY:
            # somComer.play()
            tamanhoCobra += 1
            comidaX, comidaY = gerarComida()

        relogio.tick(velocidadeDeAtualizacao)
rodarJogo()