import origins_mechanics
import orisha
import ascii
import oshun_adventure as oshun
import odu
import origins_keys as keys
import oshun_failed_branch
import training
import colorama as color


def oshun_gameplay():
    origins_mechanics.origins_compass()
    directions = input(f"""
    You have to go and meet {orisha.orunmila.name} to begin your quest. {orisha.orunmila.name} 
    is North from here. Where would you like to go? 
    """)
    if directions.lower() == "n" or directions.lower() == "north":
        print(f"We are going to meet {orisha.orunmila.name} - the first son of Olodumare \n")
        ascii.orunmila_symbol.print_orisha_symbol()
        print(f"""
        {orisha.oshun.name} meets {orisha.orunmila.name} in a beautiful abode of flowing water and resplendent beauty.
        He wears a white gown and has a face full of white beards - there are as soft as the clouds. {orisha.oshun.name}
        is speechless. \n
        """)
        print(f"{color.Fore.YELLOW}{orisha.oshun.name} my beloved, what brings you here today? {color.Style.RESET_ALL}")
        reply_one = input("""
        Type the number of your choice:
        1. I have come to begin my adventure, Orunmila \n
        destiny is a bird with wings.
        2. I am here to bask in your presence and glory. \n
        3. I am just passing through.\n
        4. I am here to continue my adventure
        """)
        if reply_one == "1":
            oshun.oshun_adventure()
        elif reply_one == "4" and oshun.oshun_victory().pebbles() == "yes" or oshun.oshun_victory().pebbles() == "y":
            oshun.oshun_adventure_two()
        else:
            print(f"{orisha.orunmila.name} says, '{color.Fore.YELLOW}Let me know when you are serious{color.Style.RESET_ALL}'")
            oshun_gameplay()
    elif directions.lower() == "i" or directions.lower() == "info" or directions.lower() == "h" or\
            directions.lower() == "help" or directions.lower() == "t" or directions.lower() == "translation":
        keys.info.key_action()
        oshun_gameplay()
    elif directions.lower() == "x" or directions.lower() == "save" or directions.lower() == "q" or\
            directions.lower() == "quit":
        quit_game = input("Are you sure you want to quit the game? ")
        if quit_game.lower() == "yes" or quit_game.lower() == "y":
            print(f"{orisha.oshun.name} it's sad to see you go, may Olodumare guide you.")
            keys.exit.key_action()
        else:
            oshun_gameplay()
    elif directions.lower() == "t" or directions.lower() == "training":
        print("You need some training?")
        training.training_ground_one()
    else:
        odu.oshun_odu_one.print_odu()
        print(f"{orisha.oshun.name}, you don't want to fulfill your destiny, why? A flowing river cannot stop mid-way!")
        oshun_failed_branch.oshun_branch()