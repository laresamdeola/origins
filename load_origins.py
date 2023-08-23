#import origins_keys as keys
import origins


def load_amulets():
    with open("amulets.txt", 'r') as load_object:
        player_amulets = load_object.read()
        print(player_amulets)


def load_player_name():
    try:
        with open("name.txt", 'r') as name_object:
            player_name = name_object.read()
            print(player_name)
    except FileNotFoundError as f_error:
        print(f"The file you requested was not found. Error code: {f_error}")
    except:
        print("You're not yet a player, choose an Orisha to start playing the game.")
        origins.origins()


def load_player_color():
    try:
        with open("color.txt", 'r') as color_object:
            player_color = color_object.read()
            print(player_color)
    except FileNotFoundError as f_error:
        print(f"The file you requested was not found. Error code: {f_error}")
    except:
        print("You don't have a color yet, choose an Orisha to start playing the game.")
        origins.origins()


def load_player_day():
    try:
        with open("day.txt", 'r') as day_object:
            player_day = day_object.read()
            print(player_day)
    except FileNotFoundError as f_error:
        print(f"We can't find your favorite day! :( Select a new one :). Error code: {f_error}")
    except:
        print("You would have to begin ORIGINS from the beginning")
        origins.origins()


def load_player_elements():
    try:
        with open("elements.txt", 'r') as elements_object:
            player_elements = elements_object.read()
            print(player_elements)
    except FileNotFoundError as f_error:
        print(f"We can't find your favorite element. But you need one to play ORIGINS. Error code: {f_error}")
    except:
        print("You would have to begin ORIGINS from the beginning")
        origins.origins()


def load_player_metal():
    try:
        with open("metal.txt", 'r') as metal_object:
            player_metal = metal_object.read()
            print(player_metal)
    except FileNotFoundError as f_error:
        print(f"We can't find your precious metal. No worries, you can pick the same or another one.. Error code: {f_error}")
    except:
        print("You would have to begin ORIGINS from the beginning")
        origins.origins()


def load_player_number():
    try:
        with open("number.txt", 'r') as number_object:
            player_number = number_object.read()
            print(player_number)
    except FileNotFoundError as f_error:
        print(f"We can't find your lucky number. Apologies.. Error code: {f_error}")
    except:
        print("You would have to begin ORIGINS from the beginning")
        origins.origins()



#load_player_metal()




