
from constantes import *
from nivel_1 import nivel_1
from pantalla_inicio import inicio_game
from ranking import game_ranking

# ------------ ------------ ------------ ------------Codigo main ------------ ------------ ------------ ------------

nivel_actual = 1

def cambiar_nivel(segundos_nivel_1=0,segundos_nivel_2=0,segundos_nivel_3=0,game_over=0):

    global nivel_actual
    nivel_actual += 1  

    if game_over == 1:

        nivel_actual = 2

    if nivel_actual == 2:
        from nivel_2 import nivel_2

        nivel_2(segundos_nivel_1)
    
    if nivel_actual == 3:
        from nivel_3 import nivel_3

        nivel_3(segundos_nivel_2)

    if nivel_actual == 4:
        from nivel_4 import nivel_4
        nivel_4(segundos_nivel_3)
    
def main():

    retorno = inicio_game()

    if retorno == 1: #Inicio del juego
    
        if nivel_actual == 1:
            
            nivel_1()

    elif retorno == 2:
        game_ranking()
    
if  __name__ == "__main__":

    main()


