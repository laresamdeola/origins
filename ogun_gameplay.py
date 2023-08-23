import origins_mechanics
import odu
import orisha
import game_symbols as gs
import player_details as pd
import ogun_adventure as ogun


def ogun_gameplay():
    origins_mechanics.origins_compass()
    odu.yemoja_odu_one.print_odu()

    directions = input(f"""
    There's a mountain left from you, {orisha.agemo_the_chameleon.name} is there; 
    he would lead you to your path. The mountains are west from here, you would 
    see a tree with a single leaf. Where do you want to go? 
    """)
    if directions.lower() == "w" or directions.lower() == "west":
        gs.mountains.print_game_symbol()
        gs.leaf.print_game_symbol()
        ogun.ogun_adventure_one()
    else:
        print(f"""Don't run away from your purpose, {pd.player_one.player_name}, {orisha.ogun.name} 
        is your Orisha, fulfill your purpose """)
        ogun_gameplay()
