def nivel_4(segundos):

    import pygame
    import sys
    from clase_personaje import Personaje
    from Moneda import Moneda
    import random
    from Bala import Bala
    from constantes import ANCHO_VENTANA,ALTO_VENTANA
    from game_over import mostrar_ventana_over
    from ultima_pantalla import mostrar_ventana_win_final
    from controlar_rect_per import controlar_rect
    pygame.init()

    pygame.display.set_caption("COINRUN")
    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    # Instancia del personaje
    personaje = Personaje()

    # Instancia del cañon
    # bala = Bala()
    clock = pygame.time.Clock()
    flag_run = True
    lista_balas = []
    lista_balas_2 = []
    lista_monedas = []
    fuente_score = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",30)
    background = pygame.transform.scale(pygame.image.load("game_background.png").convert(),(1000,800))
    contador_bale = 0
    sonido_moneda = pygame.mixer.Sound("mixkit-money-bag-drop-1989.wav")

    segundos = segundos
    fin_tiempo = False

    timer_segundos = pygame.USEREVENT
    pygame.time.set_timer(timer_segundos,1000)

    for i in range(8):

        
        monedas = Moneda(random.randrange(ANCHO_VENTANA - 50),random.randrange(ALTO_VENTANA - 50))
        lista_monedas.append(monedas)


    for i  in range(14):
        
            
        balas = Bala(50 + i * 200,0,55,55)
        lista_balas.append(balas)


    for i  in range(14):
        
            
        balas = Bala(ANCHO_VENTANA - 100,100 + i * 200,55,55)
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


                        if personaje.puntaje == 8:
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
            # print(personaje.isStay)

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
            if contador_bale == 10:
                
                bala_2.draw(screen,0)
            else:
                contador_bale += 1

            if bala_2.rect.colliderect(personaje.rect):

                mostrar_ventana_over(screen)

        for moneda in lista_monedas:

            moneda.draw(screen)

        for moneda in lista_monedas:
            
            if personaje.rect.colliderect(moneda.rect):
                
                lista_monedas.remove(moneda)
                personaje.puntaje += 1
                sonido_moneda.play()

        if personaje.puntaje == 8:
            mostrar_ventana_win_final(screen,segundos)
            sys.exit()

        controlar_rect(personaje)

        # Score
        puntaje_score = fuente_score.render(f"Puntuacion: {personaje.puntaje}",True,pygame.Color("white"))
        screen.blit(puntaje_score,(790,20))
        nivel_actual = fuente_score.render(f"NIVEL ACTUAL: 4",True,pygame.Color("white"))
        screen.blit(nivel_actual,(10,20))

        texto_temporizador = fuente_score.render(f"TIEMPO DE JUEGO : {str(segundos)}",True,(255,255,255))
        screen.blit(texto_temporizador,(10,ALTO_VENTANA - 30))

        pygame.display.flip()
        clock.tick(40)

        
    pygame.quit()
    sys.exit()
