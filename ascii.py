# ASCII ART CODE
import colorama as color

class OrishaSymbols:
    def __init__(orisha, ascii_art):
        orisha.ascii_art = ascii_art

    def print_orisha_symbol(orisha):
        print(orisha.ascii_art)


orunmila_symbol = OrishaSymbols(f"""{color.Fore.YELLOW}
||  ||  ||  ||  |
||  ||  ||  |\  |
| --  --  --  --|
|               |
|      @        |
|               |
\_______________/
 {color.Style.RESET_ALL}""")

ogun_symbol = OrishaSymbols(f"""{color.Fore.MAGENTA}
                    \                                                 
                   / \ \  /                                             
                \ /   \ \/                                              
                     / \      /                                        
                   \/   \ \  /                                          
                       / \  \                                          
                    \ /   |     /                                      
                        / |  \ /                                        
                     \ /  | | \                                        
                          | |                                          
                        \/ \ \                                        
                            \ \                                        
                             \ \                                       
{color.Style.RESET_ALL}""")

eshu_symbol = OrishaSymbols(f"""{color.Fore.BLACK}{color.Back.WHITE}
 |    |    |
 \    |    /
  \___|___/
      |        
      |    
----- |------      
      |
      |
|     |
|_____|_______
      |      |
      |      |

{color.Style.RESET_ALL}""")

yemoja_symbol = OrishaSymbols(F"""{color.Fore.GREEN}
(((
)))      
(((    
)))      
(((      /
)))     /  
     < /    \ >
      / \  / 
     /   \/   
{color.Style.RESET_ALL}""")

ibeji_symbol = OrishaSymbols("""
         |    
|\       |     
| \      |      
|   \    |       
(     \   \       
 (      )   \      
  (       )  \      
   (        ) ) @    )               
    (  @    ) )    )                  
     \     ) )   )
      \   ) )  )
       \/   \/
""")

obaluaye_symbol = OrishaSymbols("""
          ^                      
        ) |  (           
      )   |    (           
     <    |    >           
      )   |   (              
       )  |  (               
        ) | (              
         \ /
          v  
""")

obatala_symbol = OrishaSymbols("""
          ^                      
        ) |  (           
      )   |    (           
     <    |    >           
      )   |   (              
       )  |  (               
        ) | (              
         \ /
          v  
""")

sango_symbol = OrishaSymbols("""
   -------                    --------       
   |         \                /        |
   |           \____________/          |
   |                                   |
   |                                   |
    --------                  -------- | 
             \               /
               \___________ /
                 |      |            
                 |      |                
                 |      |             
                 |      |                  
                 |      |               
                 |      |                    
                 |      |                  
                 |      |                     
                 |      |                    
                 |      |                       
                 |______|                                    
""")

osanyin_symbol = OrishaSymbols("""
   O        O        O            
      \  \    |    /  /
       \  \   |   /  /
        \  \  |  /  /
       / \- \ - /  /  
      /   \       /    
     |     \     /      |
    ---------    ---------                      
    |________    ________|               

""")

oya_symbol = OrishaSymbols("""
    ^                              
     \                /
       \             /      ^
         \          /      /
           \       /     /
             \    /    /
      ________ \/ ____/
     /        /  
    /        /     
   /        /        
  ^           \----     
          \____\______
                          ^        
                        /    
                       |/    \|
""")

agemo_symbol = OrishaSymbols(f"""{color.Fore.LIGHTGREEN_EX}
         -------------------                             
        (                   )         
        |                   |         
        |                   |         
        |                   |         
        |                   |         
        |                   |         
        (                   )             
         (                 )           
         |                 |           
         |                 |           
    -----                  -----  
{color.Style.RESET_ALL}""")

oshun_symbol = OrishaSymbols(f"""{color.Fore.LIGHTBLUE_EX}
(((
)))      
(((    
)))      
(((      /
)))     /  
     < /    \ >
      / \  / 
     /   \/   
{color.Style.RESET_ALL}""")



# ----------------------------------------------------> ASCII ART FUNCTION FOR TESTING -------------------------------------------------------------->


def is_orunmila_string():
    if orunmila_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_ogun_string():
    if ogun_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_eshu_string():
    if eshu_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_yemoja_string():
    if yemoja_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_ibeji_string():
    if ibeji_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_obaluaye_string():
    if obaluaye_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_obatala_string():
    if obatala_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_sango_string():
    if sango_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_osanyin_string():
    if osanyin_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_oya_string():
    if oya_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_agemo_string():
    if agemo_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


def is_oshun_string():
    if oshun_symbol.ascii_art.isascii() is True:
        return True
    else:
        return False


