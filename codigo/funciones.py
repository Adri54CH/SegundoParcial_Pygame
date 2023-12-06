
import pygame
from constantes import *


# ---------------------------------------------Funciones apartes------------------------------------------------------

def getSurfaceFromSpriteSheet(path,columnas,filas):

    listaFotogramas = []

    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen,(120,220))
    fotograma_ancho = surface_imagen.get_width() / columnas
    fotograma_alto = surface_imagen.get_height() / filas


    for fila in range(filas):

        for columna in range(columnas):

            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            listaFotogramas.append(surface_fotograma)

    return listaFotogramas


def getSurfaceFromSpriteSheet_2(path,columnas,filas):

    listaFotogramas = []

    surface_imagen = pygame.image.load(path)
    # Redimensionamiento de la imagen 
    surface_imagen = pygame.transform.scale(surface_imagen,(300,50))

    fotograma_ancho = surface_imagen.get_width() / columnas
    fotograma_alto = surface_imagen.get_height() / filas


    for fila in range(filas):

        for columna in range(columnas):

            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            listaFotogramas.append(surface_fotograma)

    return listaFotogramas

def getSurfaceFromSpriteSheet_3(path,columnas,filas):

    listaFotogramas = []

    surface_imagen = pygame.image.load(path)
    # Redimensionamiento de la imagen 
    # surface_imagen = pygame.transform.scale(surface_imagen,(100,200))

    fotograma_ancho = surface_imagen.get_width() / columnas
    fotograma_alto = surface_imagen.get_height() / filas


    for fila in range(filas):

        for columna in range(columnas):

            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            listaFotogramas.append(surface_fotograma)

    return listaFotogramas


def getSurfaceFromPath(path,nombreParcial,cantidad):

    listaFotogramas = []

    for i in range(cantidad):

        img = pygame.image.load(path + nombreParcial + str(i) + ".png")
        print(path + nombreParcial + str(i) + ".png")
        listaFotogramas.append(img)
    # for i in range(cantidad):

    #     imgs  = pygame.image.load(path + nombreParcial + i + ".png")

    #     listaFotogramas.append(imgs)

    # return listaFotogramas

    return listaFotogramas


def getSurfaceFromFrame(frame):

    surface_fotograma = pygame.image.load(frame)

    surface_fotograma = pygame.transform.scale(surface_fotograma,(50,50))

    
    return surface_fotograma



