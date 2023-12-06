
from clase_personaje import *
# from funciones import *
def getSurfaceFromFrame(frame):

    surface_fotograma = pygame.image.load(frame)

    surface_fotograma = pygame.transform.scale(surface_fotograma,(50,50))

    
    return surface_fotograma

class Moneda:

    def __init__(self,x,y):

        self.image = getSurfaceFromFrame("game_coin_2.png")
        self.frame = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self,screen):

        self.image = self.image
        screen.blit(self.image,self.rect)
