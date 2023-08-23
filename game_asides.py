import ascii
import game_symbols as gs
import orisha
#import ewi


class OriginAsides:
    def __init__(asides, asides_name, asides_play):
        asides.asides_name = asides_name
        asides.asides_play = asides_play

    def orisha_play(asides):
        asides.asides_play()


def orunmila_agemo():
    gs.leaf.print_game_symbol()
    gs.mountains.print_game_symbol()
    gs.river.print_game_symbol()
    gs.river.print_game_symbol()
    gs.mountains.print_game_symbol()
    print(f"{orisha.orunmila.name} is in a deep state, we can see {orisha.agemo_the_chameleon.name} by his side.")
    print(
        f"{orisha.agemo_the_chameleon.name} says, '{orisha.orunmila.name} you must not give in to the demands of the Orishas, you know that inequality always breeds contempt, rivalry, jealousy, envy and many vices \n")
    print("The Chicken that has been eating from the same corn does not care about the maize field' \n")
    ascii.orunmila_symbol.print_orisha_symbol()
    print(
        f"{orisha.orunmila.name} replies, '{orisha.agemo_the_chameleon.name}, my old friend, how long can the moon stop the sun? When the day breaks, it must give way whether it wants or not'\n")
    print(f"{orisha.agemo_the_chameleon.name} asks, 'who is the moon and who is the sun? This would tear the Orisha's apart'")

    for i in range(3):
        gs.river.print_game_symbol()

    print(
        f"{orisha.orunmila.name} says, 'it is not the nature for snakes to hunt alone, it is their resolve for them to hunt alone' \n")
    print(
        f"{orisha.agemo_the_chameleon.name} finally agrees, 'Please old friend, send the Orisha's my way before you give them any special powers, fire must test itself against water before it can lay claim to strength' \n")
    print(f"{orisha.orunmila.name} replies, 'From your lips to my ears' \n")



def ogun_sango():
    gs.river.print_game_symbol()
    ascii.sango_symbol.print_orisha_symbol()

    #1. Ogun meets the Owl that does not sleep singing in a high pitched voice
    #2. Ogun is furious but chooses to increase his pace so he can leave where he is
    #3. The Owl that never sleeps hovers over Ogun's head, he's teasing Ogun
    #4. Ogun searched for any item to aim at the Owl
    #5. The Owl dodges ogun's aim then laughs
    #6. Then the owl challenges Ogun to a riddle
    #7. Ogun this time insists that he asks the riddle
    #8. the player asks the riddle, the owl misses it then leaves Ogun alone.



orunmila_and_agemo = OriginAsides("Orunmila and Agemo", orunmila_agemo)

#orunmila_and_agemo.asides_play()

# orunmila_and_agemo.orunmila_agemo()
# ogun_resolve = OriginAsides("Ogun Resolve")
# ogun_resolve.orunmila_agemo()
# 1. Orunmila and Agemo contemplate the requests of the Orishas.
# 2. Ogun discovers his love for iron, metals and tools
# 3. The creation of the Earth - Yoruba Pantheon Creation Story
# 4. Oshun begins to suspect her love for the element: water

