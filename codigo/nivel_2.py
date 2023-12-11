import pygame
import sys
from constantes import *
import random
from Moneda import Moneda
from clase_personaje import Personaje
from Bala import Bala
from game_over import mostrar_ventana_over
from game_win import mostrar_ventana_win
from main import cambiar_nivel
from controlar_rect_per import controlar_rect

def nivel_2(segundos):

    pygame.init()
    pygame.display.set_caption("COINRUN")
    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    # Instancia del personaje
    personaje = Personaje()


    clock = pygame.time.Clock()
    flag_run = True
    lista_balas = []
    lista_balas_2 = []
    lista_monedas = []
    fuente_score = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",30)
    background = pygame.transform.scale(pygame.image.load("game_background.png").convert(),(1000,800))
    sonido_moneda = pygame.mixer.Sound("mixkit-money-bag-drop-1989.wav")



    segundos = segundos
    fin_tiempo = False

    timer_segundos = pygame.USEREVENT
    pygame.time.set_timer(timer_segundos,1000)

    
    for i in range(5):

        
        monedas = Moneda(random.randrange(ANCHO_VENTANA - 50),random.randrange(ALTO_VENTANA - 50))
        lista_monedas.append(monedas)

    for i  in range(11):
        
            
        balas = Bala(100 + i * 200,0,50,50)
        lista_balas.append(balas)

    for i  in range(11):
        
            
        balas = Bala(ANCHO_VENTANA,100 + i * 200,35,35)
        lista_balas_2.append(balas)


    while flag_run:

        for eventos in pygame.event.get():

            if eventos.type == pygame.QUIT:

                flag_run = False
                sys.exit()

            if eventos.type == pygame.USEREVENT:

                if eventos.type == timer_segundos:

                    if fin_tiempo == False:

                        segundos = int(segundos) + 1
                        print(segundos)

                        if personaje.puntaje == 5:
                            fin_tiempo = True



        teclas_pulsadas = pygame.key.get_pressed()


        if teclas_pulsadas[pygame.K_LEFT]:

            personaje.controlar()
            personaje.isStay = False
    

        if teclas_pulsadas[pygame.K_RIGHT]:

            personaje.controlar()
            personaje.isStay = False


        if teclas_pulsadas[pygame.K_UP]:

            personaje.controlar()
            personaje.isStay = False

        if teclas_pulsadas[pygame.K_DOWN]:

            personaje.controlar()
            personaje.isStay = False


        if not teclas_pulsadas[pygame.K_LEFT] and not teclas_pulsadas[pygame.K_RIGHT] and not teclas_pulsadas[pygame.K_DOWN] and not teclas_pulsadas[pygame.K_UP]:

            personaje.stay()



        

        screen.blit(background,(0,0))


        personaje.update()
        
        # Dibujo el personaje
        personaje.draw(screen)
        
        
        for bala in lista_balas:
            bala.update(1)
            bala.draw(screen,1)

            if bala.rect.colliderect(personaje.rect):

                mostrar_ventana_over(screen)


        for bala_2 in lista_balas_2:

            bala_2.update(2)

            bala_2.draw(screen,0)

            if bala_2.rect.colliderect(personaje.rect):

                mostrar_ventana_over(screen)

        for moneda in lista_monedas:

            moneda.draw(screen)

        for moneda in lista_monedas:
            
            if personaje.rect.colliderect(moneda.rect):
                
                lista_monedas.remove(moneda)
                personaje.puntaje += 1
                sonido_moneda.play()

        if personaje.puntaje == 5:

            estado = mostrar_ventana_win(screen)
            if estado == -1:
                flag_run = False
            elif estado == 1:

                cambiar_nivel(0,segundos,0)
                    
        controlar_rect(personaje)

        # Score
        try:
            puntaje_score = fuente_score.render(f"Puntuacion: {personaje.puntaje}",True,pygame.Color("white"))
            screen.blit(puntaje_score,(790,20))
            nivel_actual = fuente_score.render(f"NIVEL ACTUAL: 1",True,pygame.Color("white"))
            screen.blit(nivel_actual,(10,20))

        except pygame.error:

            pygame.quit()
            sys.exit()
    
        texto_temporizador = fuente_score.render(f"TIEMPO DE JUEGO : {str(segundos)}",True,(255,255,255))
        screen.blit(texto_temporizador,(10,ALTO_VENTANA - 30))


        pygame.display.flip()
        clock.tick(40)
        
    

    pygame.quit()
    sys.exit()

