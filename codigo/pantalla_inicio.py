
def inicio_game():

    import pygame
    import sys
    from constantes import ANCHO_VENTANA,ALTO_VENTANA
    pygame.init()

    pygame.display.set_caption("COINRUN")
    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    flag_run = True
    fuente_texto = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",30)
    fuente_titulo = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",60)
    while flag_run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                flag_run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if rect_jugar.collidepoint(event.pos):

                    retorno = 1
                    flag_run = False

                
                if rect_ranking.collidepoint(event.pos):

                    retorno = 2
                    flag_run = False
            
                    


        screen.fill(pygame.Color("black "))
        texto_titulo = fuente_titulo.render("COINRUNNER",True,pygame.Color("pink"))
        texto_jugar = fuente_texto.render("JUGAR",True,pygame.Color("pink"))
        texto_ranking = fuente_texto.render("RANKING",True,pygame.Color("pink"))
        rect_jugar = pygame.Rect(330,300,300,100)
        rect_ranking = pygame.Rect(330,500,300,100)
        pygame.draw.rect(screen,(97, 57, 83),rect_jugar)
        pygame.draw.rect(screen,(97, 57, 83),rect_ranking)
        screen.blit(texto_jugar,(420,330))
        screen.blit(texto_ranking,(420,530))
        screen.blit(texto_titulo,(300,100))
    

        pygame.display.flip()


    return retorno
    


