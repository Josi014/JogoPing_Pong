import os
import pygame
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

fundo = pygame.image.load("images/mesa.jpg")
raquete1 = pygame.image.load("images/raquete1.png")
raquete1 = pygame.transform.scale(raquete1, (50, 50))
raquete2 = pygame.image.load("images/raquete2.png")
raquete2 = pygame.transform.scale(raquete2, (50, 50))

tamanhoXRaquete1 = 50
tamanhoYRaquete1 = 50
posicaoRaquete1X = 20
posicaoRaquete1Y = 100
movimentoRaquete1Y = 0
velocidade = 10

tamanhoXRaquete2 = 50
tamanhoYRaquete2 = 50
posicaoRaquete2X = 500
posicaoRaquete2Y = 100
movimentoRaquete2Y = 0
velocidade = 10

tamanhoXBola = 15
tamanhoYBola = 15
posicaoBolaX = 278
posicaoBolaY = 148
movimentoBolaX = 0
movimentoBolaY = 0
velocidadeBola = 2
clock = pygame.time.Clock()

while jogando:
    pygame.time.delay(10)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                movimentoRaquete1Y = velocidade * -1
            elif evento.key == pygame.K_DOWN:
                movimentoRaquete1Y = velocidade
        elif evento.type == pygame.KEYUP:
            movimentoRaquete1Y = 0
    if posicaoBolaX == 0: 
        posicaoBolaX -= velocidadeBola
    if posicaoBolaX > tamanhoXBola: 
        posicaoBolaX += velocidadeBola * 1 
            
    while posicaoBolaX == 0: 
       posicaoBolaX -= velocidadeBola
       if posicaoBolaX < tamanhoXBola: 
         posicaoBolaX += velocidadeBola * 1 
    
    if posicaoRaquete1Y + movimentoRaquete1Y + tamanhoYRaquete1 < altura and posicaoRaquete1Y + movimentoRaquete1Y > 0:
        posicaoRaquete1Y = posicaoRaquete1Y + movimentoRaquete1Y

    display.blit(fundo, (0, 0))
    display.blit(raquete1, (posicaoRaquete1X, posicaoRaquete1Y))
    display.blit(raquete2, (posicaoRaquete2X, posicaoRaquete2Y))

    posicao = (posicaoBolaX, posicaoBolaY)
    bola= pygame.draw.circle(display, cor, posicao, 10)
    
    if posicaoBolaX >= 550 and posicaoBolaY >= 2:
      Bola = posicaoBolaX + velocidadeBola * -1

    pygame.display.update()
    pygame.display.flip()
    fps.tick(60)

print("Você jogou muito bem!!")