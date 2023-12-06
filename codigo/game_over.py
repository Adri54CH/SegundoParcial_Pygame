import pygame
import sys
from constantes import *
from nivel_1 import nivel_1

def mostrar_ventana_over(screen):

    flag = True
    font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",50)
    game_over = 1
    while flag:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag = False
                sys.exit()

            
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if rect_reiniciar.collidepoint(evento.pos):
                    # global nivel_actual
                    # nivel_actual = 0
                    nivel_1(game_over)
                    
            
                    
        screen.fill((241, 223, 219))

        texto_muerte = font.render("GAME OVER",True,((41, 10, 3)))
        screen.blit(texto_muerte,(ANCHO_VENTANA // 2 - 150,ALTO_VENTANA // 2 - 50))

        rect_reiniciar = pygame.Rect((330,500,300,100))
        pygame.draw.rect(screen,(0,0,0),rect_reiniciar)
        texto_reiniciar = font.render("RESTART",True,(255,255,255))
        screen.blit(texto_reiniciar,(360,520))

        pygame.display.flip()
    pygame.quit()
    sys.exit()