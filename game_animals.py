from game_symbols import GameSymbols


class Animals(GameSymbols):
    def __init__(animal, animal_name, orisha_animal, game_ascii_art):
        super().__init__(game_ascii_art)
        animal.animal_name = animal_name
        animal.orisha_animal = orisha_animal

    def print_animal_symbol(animal):
        print(animal.game_ascii_art)


dove = Animals("Dove", "Obatala", "////----///----")


peacock = Animals("Peacock", "Oshun", """""
         o 0 0                                       
          \|/                                      
           ^                                         
         /  \       % ^  % ^                          
        /% ^ \     /  / /  /                                                   
           /  /   / (  /  (                              
         /     )  \ /  \ /                                   
       /        )  \    \                              
        \        \       \                            
          \       )                               
            )     /                               
             \   /                                 
               \                                 
""")


vulture = Animals("Vulture", "Oshun", """""
                               ^          
                ____          /  \              
               / *  )       /     \           
          --/--    )      /        \                   
        / -----   (____/           /               
                \                   \     
                 \                   \    
                 |                    \   
                /                      \           
                \                      \        
                 \                 / \/       
                  \_____/ \_________/                
                     |         |          
                     |         |          
                     |         |              
                     |         |              
                  __/        __/          
                 |          |           
""")


owl = Animals("Owl", "", """
           %\           %\                                       
           \  \  ----- / /                                           
             \  \     / /                                         
            (     V      )                                    
           /    @     @   \                                  
          (        V       )                                 
           \              /                                    
            \ ___________/                                    
""")


"""
i = 0
while i < 1:
    print("." + " " + "." + " " + ".")
    i += 1

"""

"""
Timers

import threading


def num_timer_call():
    print(1)

def num_timer_call_2():
    print(2)

def num_timer_call_3():
    print(3)

num_timer = threading.Timer(1.0, num_timer_call)
num_timer_2 = threading.Timer(1.0, num_timer_call_2)
num_timer_3 = threading.Timer(1.0, num_timer_call_3)

num_timer.start()
num_timer_2.start()
num_timer_3.start()

"""



