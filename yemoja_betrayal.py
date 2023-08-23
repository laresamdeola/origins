import ascii
import game_symbols as gs
import odu
import origins_mechanics as gm
import orisha


def yemoja_betrayal():
    odu.yemoja_odu_one.print_odu()
    gm.origins_compass()
    print(f"{orisha.yemoja.name} says, 'Orunmila would be South-East from here.'")
    gs.foot_steps.print_game_symbol()
    gs.river.print_game_symbol()
    print("\n")
    ascii.orunmila_symbol.print_orisha_symbol()
    odu.orunmila_odu_one.print_odu()
    print("\n Orunmila's face wears a heavy look. Orunmila is bothered, concerned about something that affects him deeply \n")
    print("The first son of Olodumare, Orunmila I greet you \n")
    print("Orunmila heard Yemoja but the texture of his gaze remains unchanged. He can smell the air \n")
    print("The maker of a thousand kingdoms, I greet you. You must know why I am here \n")
    print("Orunmila is still quiet, he has not set his sights on Yemoja \n")
    print("Yemoja is perplexed, unsure of what to do. I am here for my powers great Orunmila. \n")
    print("Orunmila is quiet \n")
    print("Yemoja says, 'Give me a riddle so I may throw my own pebbles into the river' \n")
    print("Orunmila is quiet")
    print("Yemoja goes closer to Orunmila, he is at the tip of the hill, she continues to climb, one foot and pant and stretch at a time")
    print("Then a heavy rain begins to fall, the rain falls down to earth and sounded like a thousand malimba birds were in the sky. It fell all over the hill, only over the hill")
    print("Yemoja is wet, but Orunmila is still far ahead, she looks down the hill and sees she has climbed a good distance")

    i = 0
    while i < 7:
        print("ORUNMILA")
        ascii.yemoja_symbol.print_orisha_symbol()
        i += 1

    gs.tears.print_game_symbol()
    ascii.orunmila_symbol.print_orisha_symbol()

    print("Orunmila's gaze finally touches Yemoja, and then she knew her fate")

    # Continue to build the scene from here.

    #Logic for while Loop Counter

"""
    answer_tries = 2
    while answer_tries >= 0:
        question_one = input("What is your name? ")
        if question_one == "Lare":
            print("Well done")
            break
        print(f"You have {answer_tries} tries left.")
        answer_tries -= 1

    answer_tries = 9
    while answer_tries >= 0:
        question_two = input("What's the name of your favorite Football Team? ")
        if question_two == "Liverpool":
            print("You are correct!")
            break
        if answer_tries == 1:
            print("This is your last guess, please make it count")
        print(f"You have {answer_tries} tries left")
        answer_tries -= 1

"""

