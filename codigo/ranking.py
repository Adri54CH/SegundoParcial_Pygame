import sqlite3
import sys

def game_ranking():

    import pygame
    from constantes import ANCHO_VENTANA,ALTO_VENTANA

    pygame.init()
    pygame.display.set_caption("COINRUN")
    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    flag_run = True
    font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",30)
    font_ranking = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",50)

    while flag_run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                flag_run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                x,y = pygame.mouse.get_pos()
                if rect_menu.collidepoint(x,y):
                    from main import main
                    main()
                    sys.exit()  
        
        conexion = sqlite3.connect("ranking.db")
        cursor = conexion.cursor()


        cursor.execute("SELECT nombre, tiempo FROM scores ORDER BY tiempo ASC")
        datos_jugadores = cursor.fetchall()

        screen.fill(pygame.Color("white"))

        x_pos_nombre = 200
        x_pos_tiempo = 500
        y_pos = 300
        texto_1  = font.render("NOMBRES",True,(0,0,0))
        screen.blit(texto_1,(200,250))
        texto_2  = font.render("TIEMPO",True,(0,0,0))
        screen.blit(texto_2,(500,250))
        text_ranking = font_ranking.render("RANKING COINRUNNER",True,(213, 170, 198))
        screen.blit(text_ranking,(200,50))

        rect_menu = pygame.Rect(250,700,400,60)
        pygame.draw.rect(screen,(0,0,0),rect_menu)    
        texto_menu_principal = font.render("MENU PRINCIPAL",True,(255,255,255))
        screen.blit(texto_menu_principal,(325,710))

        
        for nombre, tiempo_juego in datos_jugadores:
            
            text_nombre = font.render(f"{nombre}", True, (0, 0, 0))
            text_tiempo = font.render(f"{tiempo_juego} segundos", True, (0, 0, 0))
            
            screen.blit(text_nombre, (x_pos_nombre, y_pos))
            screen.blit(text_tiempo, (x_pos_tiempo, y_pos))
            
            y_pos += 40

        conexion.close()

        pygame.display.flip()

    pygame.quit()
    




