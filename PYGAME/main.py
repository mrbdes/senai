# Pygame:
#   pip install pygame

# 1. IMPORT ------------------------------------------
import pygame
import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot

# 2. INICIALIZACAO -----------------------------------

# 2.1. Iniciar o Pygame
pygame.init()

# 2.2 Iniciar a janela com a configuracao de resolução de 840x480

# 2.2.1 Constantes de Largura e Altura da Tela
WIDTH_SCREEN = 840          # Largura
HEIGHT_SCREEN = 480         # Altura

# 2.2.2 Criar a janela
display = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])

# 2.2.3 Preencher o fundo da janela com uma cor RGB
display.fill([145, 107, 87])
#display.fill("#32b1e3")

# 2.2.4 Mudar o título da janela
pygame.display.set_caption("Game SENAI - Python")

# 2.2.5 Carregar a imagem para criar o icone
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)

# 3. ELEMENTOS DE TELA -------------------------------

# 3.1 Personagens

# Criar um grupo de imagens para carregar todas imagens e 
#desenhar de uma unica vez
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

# criar um cenario (bachgroud ) para o fantasma
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image,[840,480])
bg.rect = bg.image.get_rect()


# Criar um objeto Sprite para manipular a imagem - fantasma
ghost = Ghost(objectGroup)


#ghost = pygame.sprite.Sprite(drawGroup)

# 3.2 Fontes........
score_font = pygame.font.Font("font/Pixeltype.ttf", 50)
GAMEOVER_font = pygame.font.Font("font/Pixeltype.ttf", 200)

# 3.3 Música.............
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1)

# 3.4 som (spx).............
attack = pygame.mixer.Sound("data/magic1.wav")


# 4. VARIAVEIS GLOBAIS -------------------------------
gameLoop = True
gameOver = False
timer = 20
pontos = 0

# 4.1 Criar um clock para ajudar os frames por segundo (FPS)
clock = pygame.time.Clock()

# 5. FUNCAO PRINCIPAL --------------------------------

def main():
    global gameLoop
    global gameOver
    global timer
    global pontos 

    # Criar o Game Loop
    while gameLoop:

        #Clock para 60fps
        clock.tick(60)

        # Verificacao dos eventos possíveis
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   newShoot = Shoot(objectGroup, shootGroup)
                   newShoot.rect.center = ghost.rect.center
                   attack.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                   newShoot = Shoot(objectGroup, shootGroup)
                   newShoot.rect.center = ghost.rect.center
                   attack.play()

                   
        if not gameOver:
            display.fill([145, 107, 87])

            # criar os varios morcegos
            timer += 1    
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup)

            # colisao dos Morcegos com  fantasma
            colisao = pygame.sprite.spritecollide(ghost, batGroup, False, pygame.sprite.collide_mask)
            if colisao:
                print("GAME OVER!!!")
                gameOver =True

            # colisão do tiro com o morcego
            tiros = pygame.sprite.groupcollide(shootGroup,batGroup,True,True, pygame.sprite.collide_mask)
                        
                        # contagen de morcegos mortos
            if tiros:
                pontos += 1
                print("Score:", pontos)

            objectGroup.update()
  
       

        # Desenhando os elementos dos grupos na minha jenela

        objectGroup.draw(display)

        score_render = score_font.render(f'Socore:{pontos}',False, 'White')
        display.blit(score_render,(650, 50))

        # incerindo o game over na tela
        if gameOver:
            gameOverMsg = GAMEOVER_font.render ('GAME OVER', False, 'white') 
            display.blit(gameOverMsg, (100,150))

        # Atualização de tela
        pygame.display.update()

if __name__ == "__main__":
    main()