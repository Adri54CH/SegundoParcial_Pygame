import pygame

# from funciones import getSurfaceFromSpriteSheet

# from main import main
# ------------------------------------Clases y sus metodos---------------------------------------------------------------------------------
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
class Personaje:

    def __init__(self):
        
        # Todas las animacion de movimiento
        self.animaciones = getSurfaceFromSpriteSheet("sprite_sheet_2.png",4,4)

        # self.animaciones = getSurfaceFromSpriteSheet("dist/sprite_sheet_2.png",4,4)

        self.caminar_right = self.animaciones[12:16]
        self.caminar_left = self.animaciones[8:12]
        self.caminar_up = self.animaciones[4:8]
        self.caminar_down = self.animaciones[0:4]
        # self.stay = getSurfaceFromSpriteSheet()
        self.frame = 0
        self.animation = self.caminar_right
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.move_x = 0
        self.move_y = 0
        self.isStay = False
        self.speed_walk = 12
        self.contador = 0
        self.isStay = False
        self.puntaje = 0    
    def update(self):

        if self.frame < len(self.animation) -1 and self.isStay == False:

            self.frame += 1
            self.rect.x += self.move_x 
            self.rect.y += self.move_y
        
        else:

            self.frame = 0
    

    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def stay(self):

        self.isStay = True

    def controlar(self):

        self.move_x = 0
        self.move_y = 0

        teclas_pulsadas = pygame.key.get_pressed()


        if teclas_pulsadas[pygame.K_LEFT]:
            self.move_x = -self.speed_walk
            self.animation = self.caminar_left
            
        if teclas_pulsadas[pygame.K_RIGHT]:
            self.move_x = self.speed_walk
            self.animation = self.caminar_right

        if teclas_pulsadas[pygame.K_UP] and not teclas_pulsadas[pygame.K_RIGHT] and not teclas_pulsadas[pygame.K_LEFT]:
            self.move_y = -self.speed_walk
            self.animation = self.caminar_up
        if teclas_pulsadas[pygame.K_DOWN] and not teclas_pulsadas[pygame.K_RIGHT] and not teclas_pulsadas[pygame.K_LEFT]:
            self.move_y = self.speed_walk
            self.animation = self.caminar_down

        # Me aseguro que no hayan movimientos diagonales
        if self.move_x != 0 and self.move_y != 0:
            if teclas_pulsadas[pygame.K_LEFT]:
                self.move_x = -self.speed_walk
                self.move_y = 0
            elif teclas_pulsadas[pygame.K_RIGHT]:
                self.move_x = self.speed_walk
                self.move_y = 0
            elif teclas_pulsadas[pygame.K_UP]:
                self.move_y = -self.speed_walk
                self.move_x = 0
            elif teclas_pulsadas[pygame.K_DOWN]:
                self.move_y = self.speed_walk
                self.move_x = 0
        
