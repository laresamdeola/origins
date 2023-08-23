def origins_compass():
    compass = """
               NW       N     NE                          
                  \     |     /                          
                   \    |    /                         
                    \   |   /                          
                     \  |  /                           
                      \ | /                           
                       \|/                             
         W--------------|----------------E                            
                      / |\                             
                    /   | \                            
                   /    |  \                           
                  /     |   \                          
                 /      |    \                         
                /       |     \                         
               /        |      \                      
              SW        S      SE
    N = North
    NE = North-East
    E = East
    SE = South-East
    S = South
    SW = South-West
    W = West
    NW = North-West
    \n
    """
    print(compass)


def movements():
    origins_movements = input("Where would you like to go? ").lower()
    return origins_movements


# North means you want to go forward in the game.
# South means you want to go back to your abode, interaction between the player and the god/goddess
# West means you want to go and meet one of your god friends
# East means you want to go and equip/find details about your myths and legends???
