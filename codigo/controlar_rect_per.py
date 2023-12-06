from constantes import ALTO_VENTANA,ANCHO_VENTANA

def controlar_rect(personaje:object):
        

    if personaje.rect.x < 0:

        personaje.rect.x = 0

    elif personaje.rect.x > ANCHO_VENTANA - 30:
        
        personaje.rect.x = ANCHO_VENTANA - 30


    elif personaje.rect.y < 0:
    
        personaje.rect.y = 0

    elif personaje.rect.y > ALTO_VENTANA - 50:

        personaje.rect.y = ALTO_VENTANA - 50