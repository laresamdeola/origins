import origins_intro
import player_details as player
import orisha_selection as orisha

# Entry point for the game. Call this method in the python console to start playing the game. You must clone this repository first.

def origins():
    origins_intro.intro()
    player.player_name_details()
    player.player_elements_details()
    player.player_color_details()
    player.player_number_details()
    player.player_day_details()
    player.player_metal_details()
    orisha.orisha_selection()


#origins()

