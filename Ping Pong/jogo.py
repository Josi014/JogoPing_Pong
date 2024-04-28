import os
import pygame
import time
pygame.init()
os.system("cls")
print("Começando o Jogo Ping Pong!")
largura = 556
altura = 297
tamanho = (largura, altura)
display = pygame.display.set_mode(tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("Ping Pong")
branco = (255, 255, 255)
cor = (255, 69, 0)
jogando = True
clock = pygame.time.Clock()
placarPlayer1 = 0
placarPlayer2 = 0
nome = input("Digite seu nome ")
pixel = 64
black= pygame.Color(0,0,0)


tamanhoXRaquete1 = 10
tamanhoYRaquete1 = 50
posicaoRaquete1X = 20
posicaoRaquete1Y = 100
movimentoRaquete1Y = 0
velocidadeRaquete1Y = 10

tamanhoXRaquete2 = 10
tamanhoYRaquete2 = 50
posicaoRaquete2X = 520
posicaoRaquete2Y = 100
velocidadeRaquete2Y = 5

diametro = 15
raio = diametro / 2
posicaoBolaX = 278
posicaoBolaY = 148
movimentoBolaX = 0
movimentoBolaY = 0
velocidadeBolaX = 2
velocidadeBolaY = 2
posicaoBola = posicaoBolaX, posicaoBolaY

fundo = pygame.image.load("images/mesa.jpg")


def escreverTexto(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 15)
    textoDisplay = fonte.render(texto, True, branco)
    display.blit(textoDisplay, (5, 5))


def pontoJogador1():
    fonte = pygame.font.Font("freesansbold.ttf", 25)
    textoDisplay = fonte.render("PONTOO da " + nome + "!!", True, branco)
    display.blit(textoDisplay, (150, 83))
    pygame.display.update()
    time.sleep(2)


def pontoOponente():
    fonte = pygame.font.Font("freesansbold.ttf", 25)
    textoDisplay = fonte.render("PONTOO DO OPONENTE!!", True, branco)
    display.blit(textoDisplay, (150, 83))
    pygame.display.update()
    time.sleep(2)


while jogando:
    pygame.time.delay(10)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                movimentoRaquete1Y = velocidadeRaquete1Y * -1
            elif evento.key == pygame.K_DOWN:
                movimentoRaquete1Y = velocidadeRaquete1Y
        elif evento.type == pygame.KEYUP:
            movimentoRaquete1Y = 0
    if posicaoBolaX == 0:
        posicaoBolaX -= velocidadeBolaX
    if posicaoBolaX > diametro:
        posicaoBolaX += velocidadeBolaX * 1
    if posicaoBolaY == 0:
        posicaoBolaY -= velocidadeBolaY
    if posicaoBolaY > diametro:
        posicaoBolaY += velocidadeBolaY * 1

    if posicaoRaquete1Y + movimentoRaquete1Y + tamanhoYRaquete1 < altura and posicaoRaquete1Y + movimentoRaquete1Y > 0:
        posicaoRaquete1Y = posicaoRaquete1Y + movimentoRaquete1Y
        
    
    if posicaoBolaX>400:
        if posicaoRaquete2Y == 0:
            posicaoRaquete2Y -= velocidadeRaquete2Y
        if posicaoRaquete2Y > diametro:
            posicaoRaquete2Y += velocidadeRaquete2Y * 1
        if posicaoRaquete2Y > 300:
            velocidadeRaquete2Y *= -1
        if posicaoRaquete2Y < 25:
            velocidadeRaquete2Y *= -1 
        if posicaoBolaY!=posicaoRaquete2Y:
            posicaoRaquete2Y=posicaoBolaY
    else:
        posicaoRaquete2Y = 120
    
    
   
    display.blit(fundo, (0, 0))
    
    posicao = (posicaoBolaX, posicaoBolaY)
    bola = pygame.draw.circle(display, branco, posicao, 10)
    raquete1 =pygame.draw.rect(display, cor, pygame.Rect(posicaoRaquete1X, posicaoRaquete1Y, tamanhoXRaquete1, tamanhoYRaquete1))
    raquete2 =pygame.draw.rect(display,cor, pygame.Rect(posicaoRaquete2X, posicaoRaquete2Y, tamanhoXRaquete2, tamanhoYRaquete2))
   

    if posicaoBolaX > 546:
        pontoJogador1()
        placarPlayer1 += 1
        velocidadeBolaX *= -1

    if posicaoBolaX < 18:
        pontoOponente()
        placarPlayer2 += 1
        velocidadeBolaX *= -1

    if posicaoBolaY > 300:
        velocidadeBolaY *= -1
    if posicaoBolaY < 18:
        velocidadeBolaY *= -1
    if posicaoBolaY!=posicaoRaquete2Y:
       posicaoRaquete2Y=posicaoBolaY/1.5
    if bola.colliderect(raquete1):
      velocidadeBolaX *= -1
    if bola.colliderect(raquete2):
      velocidadeBolaX *= -1

    escreverTexto("Placar "+str(placarPlayer1)+" x "+str(placarPlayer2))
    pygame.display.update()
    pygame.display.flip()
    fps.tick(60)
    print(posicaoRaquete2Y)
print("Você jogou muito bem!!")
