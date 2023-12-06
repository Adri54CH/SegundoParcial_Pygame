import pygame
import sys
from constantes import *
import sqlite3
from main import main

def crear_tabla_si_no_existe(conexion):
    # Crea la tabla si no existe
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            nombre TEXT,
            tiempo INTEGER
        )
    """)
    conexion.commit()

def guardar_score(conexion, nombre, tiempo):
    # Guarda el score y el nombre en la base de datos
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO scores (nombre, tiempo) VALUES (?, ?)", (nombre, tiempo))
    conexion.commit()

def mostrar_ventana_win_final(screen,tiempo_juego=0):
    flag = True
    font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf",48)
    nombre_ingresado = ""
    while flag:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag = False
                retorno = -1
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                x,y = pygame.mouse.get_pos()
                if rect_menu.collidepoint(x,y):

                    main()
                    sys.exit()  
                    

            if evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_RETURN:

                    nombre = nombre_ingresado
                    nombre_ingresado = ""
                    
                    conexion = sqlite3.connect("ranking.db")

                    crear_tabla_si_no_existe(conexion)

                    nombre_jugador = nombre
                    tiempo_final = tiempo_juego   # Score del jugador 

                    guardar_score(conexion,nombre_jugador,tiempo_final)

                elif evento.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]
                else:
                    nombre_ingresado += evento.unicode
                
                    
                    
        screen.fill((241, 223, 219))
        
        texto_entrada = font.render("INGRESE SU NICK: ",True,(41, 10, 3))
        screen.blit(texto_entrada,(100,200))
        texto_nombre = font.render(nombre_ingresado, True, (0,0,0))
        screen.blit(texto_nombre,(500,200))
        texto_muerte = font.render("YOU WON!!!",True,((41, 10, 3)))
        screen.blit(texto_muerte,(ANCHO_VENTANA // 2 - 150,ALTO_VENTANA // 2 - 50))
    
        rect_menu = pygame.Rect(250,700,400,60)
        pygame.draw.rect(screen,(0,0,0),rect_menu)    
        texto_menu_principal = font.render("MENU PRINCIPAL",True,(255,255,255))
        screen.blit(texto_menu_principal,(300,700))

        

    
        # rect_reiniciar = pygame.Rect((330,500,300,100))
        # pygame.draw.rect(screen,(0,0,0),rect_reiniciar)
        # texto_reiniciar = font.render("RESTART",True,(255,255,255))
        # screen.blit(texto_reiniciar,(360,520))

        
    
        pygame.display.flip()

    # conexion = sqlite3.connect("ranking.db")

    # crear_tabla_si_no_existe(conexion)

    # nombre_jugador = input("Ingresa tu nombre: ")
    # puntaje = int(input("Ingresa tu puntaje: "))

    # guardar_score(conexion,nombre_jugador,puntaje)

    pygame.quit()


    return retorno

