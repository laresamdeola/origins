import colorama as color


class GameSymbols:
    def __init__(game_symbol, game_ascii_art):
        game_symbol.game_ascii_art = game_ascii_art

    def print_game_symbol(game_symbol):
        print(game_symbol.game_ascii_art)



eternal_flame = GameSymbols(f"""{color.Back.YELLOW}
             / \ 
            /   \ 
           /      \ 
          /        \ 
         /          \ 
        /            \ 
      /               \ 
     /                  \ 
    |                   |           
     \                 /
       \              /
         \__________/ 
{color.Style.RESET_ALL}""")


tears = GameSymbols(f"""{color.Fore.YELLOW}{color.Back.LIGHTWHITE_EX}
             / \ 
            /   \ 
           /      \ 
          /        \ 
         /          \ 
        /            \ 
      /               \ 
     /                  \ 
    |                   |           
     \                 /
       \              /
         \__________/ 
{color.Style.RESET_ALL}""")


foot_steps = GameSymbols(f"""{color.Fore.YELLOW}
              ()   ()                            
           ()    ()                                 
        ()  _______/ \                         
          (          /                         
           \        /                          
            \       \                        
             \        --                        
              \          \                    
               \          \                   
                \         /                    
                 --------/                            
                      \ \                      
                       \ \                     
                        / /                    
                       / /                       
                      / /                      
                     / /                     
                     \ \                       
                      \ \                      
                       \ \                     
{color.Style.RESET_ALL}""")

mountains = GameSymbols(f"""{color.Fore.YELLOW}
                          /\                
                     /\  /| \                   
           /\     /\/  \//   \  /\                  
          |   \ \/       |    \/  \               
         /     \         |    /     \             
       /        /  /\   /    /       \               
     /         / /    \/    /         \               
    /          |/         /            \         
   --------------------------------------      
{color.Style.RESET_ALL}""")

huts = GameSymbols(f"""{color.Fore.YELLOW}
                ^                   
              /   \                     
             /     \                  
            /       \                
           /_________\                  
           |         |                 
           |         |                  
           |   ___   |                  
           )  |   |  (                  
           |_________|                           
{color.Style.RESET_ALL}""")

leaf = GameSymbols(f"""{color.Fore.YELLOW}
                  ^                                     
                /   \                        
               /     \                         
              /   ||  \                      
             /    ||   \                     
            (     ||    )                    
              \__/||\__/                              
                  ||                        
                  ||                         
{color.Style.RESET_ALL}""")

pebbles = GameSymbols(f"""{color.Fore.YELLOW}
               _______                                                    
             /        \_____                                              
            (               \                                        
             \               |                                      
               \___________ %                                       
                  
               _______                                                    
             /        \_____                                              
            (               \                                        
             \               |                                      
               \___________ %                                       
                                                                                  
              _______                                                    
             /        \_____                                              
            (               \                                        
             \               |                                      
               \___________ %                                       
{color.Style.RESET_ALL}""")

river = GameSymbols(f"""{color.Fore.BLUE}
         -----      ------      -------         -----                           
        / ___ \____/  ____ \____/ _____ \_______/ ----                              
         / ___ \_____/ ____ \______/ ____ \_________/                               
          /   \_______/    \________/    \___________/                                      
{color.Style.RESET_ALL}""")

groove_map = GameSymbols("""
----=
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


