import pygame 
from funciones import getSurfaceFromSpriteSheet_2
from constantes import *


class Bala:

    def __init__(self,x,y,velocidad_mov,velocidad_mov_2):


        self.animacion_bala = getSurfaceFromSpriteSheet_2("cannon_spritesheet.png",8,1)
        self.frame = 0
        self.image = self.animacion_bala[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador_1 = 0
        self.velocidad_movimiento = velocidad_mov
        self.velocidad_movimiento_2 = -velocidad_mov_2


    def update(self,tipo_bala):

        if self.frame < len(self.animacion_bala) -1 and self.contador_1 == 4:
                    
            self.frame += 1
            # self.rect.x += self.velocidad_movimiento

            if tipo_bala == 1:

                self.rect.y += self.velocidad_movimiento
                # print(self.frame)
        
                self.contador_1 = 0

            elif tipo_bala == 2:

                self.rect.x  += self.velocidad_movimiento_2

                self.contador_1 = 0
        else:
            self.contador_1 += 1


        if self.frame == len(self.animacion_bala)-1:

            self.frame = 0


        if self.rect.y > 900:

            self.rect.y = 0

        if self.rect.x < -100:
            self.rect.x = ANCHO_VENTANA

    def draw(self,screen,estado_rotacion):

        if estado_rotacion == 0:

            self.image = self.animacion_bala[self.frame]
            screen.blit(self.image,self.rect)
            
    
        else:
            self.image = pygame.transform.rotate(self.animacion_bala[self.frame],90)
            screen.blit(self.image,self.rect)


