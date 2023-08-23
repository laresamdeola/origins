import sys
import orisha
import ascii
import amulets
import origins_intro as intro
import origins
import load_origins as load


class OriginKeys:
    def __init__(keys, key_press, key_action, key_action_two, key_action_three, key_message, key_message_two):
        keys.key_press = key_press
        keys.key_action = key_action
        keys.key_action_two = key_action_two
        keys.key_action_three = key_action_three
        keys.key_message = key_message
        keys.key_message_two = key_message_two

    def keys(keys):
        key_pressed = input(
            "What do you want to do? \n1. save(s)\n2. info(i)\n3. help(h)\n4. amulets(a)\n5. translate(t)\n6. exit(e) \n7. play(p)\n").lower()
        if key_pressed == "s" or key_pressed == "save":
            keys.key_action(amulets.black_peacock.amulet_name)
        elif key_pressed == "a" or key_pressed == "amulets":
            keys.key_action_two()
        elif key_pressed == "p" or key_pressed == "play":
            keys.key_action()
        elif key_pressed == "i" or key_pressed == "info":
            keys.key_action()
        elif key_pressed == "t" or key_pressed == "translate":
            keys.key_action()
        elif key_pressed == "h" or key_pressed == "help":
            keys.key_action()
        elif str(["e", "exit", "q", "quit"]) in key_pressed:
            keys.key_action()


def save_amulets(amulet):
    with open("amulets.txt", 'w') as amulets_object:
        amulets_object.write(amulet)


def save_amulets2(amulet2):
    with open("amulets.txt", 'a') as amulets2_objects:
        amulets2_objects.write(amulet2)


def save_stage(stage):
    with open("amulets.txt", 'w') as amulets_object:
        amulets_object.write(stage)


def exit_game():
    exit_sure = input("Are you sure you want to exit ORIGINS?").lower()
    if exit_sure == "yes" or exit_sure == "y":
        sys.exit("Sad to see you go. Odabo!")
    elif exit_sure == "no" or exit_sure == "n":
        origins.origins()
    else:
        info.keys()


def info():
    game_info = int(input(
        "Type the number to select your choice:\n1. Background to the game\n2. Translations/Meanings\n3. Orisha Story\n4. How To Play Origins \n5. Load Game"))
    if game_info == 1:
        intro.intro()
    elif game_info == 2:
        translate = input("What Yoruba word do you need explanation on? ").lower()
        if translate.lower() == "orisha":
            ascii.obatala_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.orisha.translation)
        elif translate.lower() == "oshun":
            ascii.yemoja_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.oshun.translation)
        elif translate.lower() == "yemoja":
            ascii.yemoja_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.yemoja.translation)
        elif translate.lower() == "ogun":
            ascii.ogun_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.ogun.translation)
        elif translate.lower() == "orunmila":
            ascii.orunmila_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.orunmila.translation)
        elif translate.lower() == "agemo":
            ascii.agemo_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.agemo_the_chameleon.translation)
        elif translate.lower() == "ase":
            print("Ase is synonymous to 'Amen' in English. It is a declarative phrase used to end prayers in Yoruba \
            land.")
        elif translate.lower() == "kare" or translate.lower() == "o kare":
            print("O kare means 'well done'. It's a sort of praise.")
        else:
            print(f"The word '{translate}' was not used in this game. Pele!")
    elif game_info == 3:
        tales = input("Which Orisha do you want to know more about? ").lower()
        if "oshun" or "osun" in tales:
            ascii.oshun_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.oshun.origin_story)
        elif "yemoja" in tales:
            ascii.yemoja_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.yemoja.origin_story)
        elif "ogun" in tales:
            ascii.ogun_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.ogun.origin_story)
        elif "orunmila" in tales:
            ascii.orunmila_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.orunmila.origin_story)
        elif "oya" in tales:
            ascii.oya_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.oya.origin_story)
        elif "eshu" in tales:
            ascii.eshu_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.eshu.origin_story)
        elif "erinle" in tales:
            ascii.oya_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.erinle.origin_story)
        elif "agemo" in tales:
            ascii.agemo_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.agemo_the_chameleon.origin_story)
        elif "obatala" in tales:
            ascii.obatala_symbol.print_orisha_symbol()
            print("\n")
            print(orisha.obatala.origin_story)
        else:
            print(f"Are you sure {tales} is a Yoruba Orisha? If yes then you can check online sources. Pele!")
            # info()
    elif game_info == 4:
        pass
    elif game_info == 5:
        load_choice = int(input("What part of your game progress do you want to load? \n1. amulets \n2. name \n3. color \n4. day \n5. elements \n6. metal \n7. number "))
        if load_choice == 1:
            load.load_amulets()
        elif load_choice == 2:
            load.load_player_name()
        elif load_choice == 3:
            load.load_player_color()
        elif load_choice == 4:
            load.load_player_day()
        elif load_choice == 5:
            load.load_player_elements()
        elif load_choice == 6:
            load.load_player_metal()
        elif load_choice == 7:
            load.load_player_number()
        else:
            print("You did not select any of the numbers 1 - 7")
            info()



save = OriginKeys("s" or "save", save_amulets, save_amulets2, save_stage, "save all your amulets or charms",
                  "save your current stage")

info = OriginKeys("i" or "info" or "h" or "help" or "t" or "translation", info, None, None, "more information", None)

exit = OriginKeys("e" or "exit" or "q" or "quit", exit_game, None, None, "exit/quit game", None)


# play.key_action()


#info.key_action()

# ----------------------------------------------------> ORIGIN KEYS  FUNCTION FOR TESTING -------------------------------------------------------------->

#info

def is_game_info_int():
    game_info = int(input("Type the number to select your choice:\n1. Background to the game\n2. Translations/Meanings\n3. Orisha Story\n4. How To Play Origins \n5. Load Game"))
    if game_info:
        return True
    else:
        return False


def is_game_info_str():
    game_info = int(input(
        "Type the number to select your choice:\n1. Background to the game\n2. Translations/Meanings\n3. Orisha Story\n4. How To Play Origins \n5. Load Game"))
    if game_info is type(str):
        return True
    else:
        return False


def is_translate_lower():
    translate = input("What Yoruba word do you need explanation on? ").lower()
    return translate


def is_translate_mix_characters():
    translate = input("What Yoruba word do you need explanation on? ").lower()
    return translate


def is_translate_with_numbers():
    translate = input("What Yoruba word do you need explanation on? ").lower()
    return translate


def is_tales_lower():
    tales = input("What Yoruba word do you need explanation on? ").lower()
    return tales


def is_tales_mix_characters():
    tales = input("What Yoruba word do you need explanation on? ").lower()
    if tales:
        return True
    else:
        return tales


def is_tales_with_numbers():
    tales = input("What Yoruba word do you need explanation on? ").lower()
    if tales:
        return True
    else:
        return tales








