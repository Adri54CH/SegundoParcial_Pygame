import pygame
from constantes import *

def mostrar_ventana_win(screen):
    flag = True
    font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",48)
    sonido_win = pygame.mixer.Sound("mixkit-achievement-completed-2068.wav")
    sonido_win.play()
    while flag:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag = False
                retorno = -1
                
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if rectangulo_siguiente_nivel.collidepoint(evento.pos):

                    flag = False
                    retorno = 1

            
        screen.fill((241, 223, 219))
        
        
        texto_muerte = font.render("YOU WON!!!",True,((41, 10, 3)))
        screen.blit(texto_muerte,(ANCHO_VENTANA // 2 - 150,ALTO_VENTANA // 2 - 50))
    

        rectangulo_siguiente_nivel = pygame.Rect(ANCHO_VENTANA // 2 - 220,ALTO_VENTANA // 2 + 200,400,70)
        pygame.draw.rect(screen,(122,122,122),rectangulo_siguiente_nivel)
        texto_nivel = font.render("SIGUIENTE NIVEL",True,((41,10,3)))
        screen.blit(texto_nivel,(ANCHO_VENTANA // 2 - 200,ALTO_VENTANA // 2 + 200))


        pygame.display.flip()

    return retorno

