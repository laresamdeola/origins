import colorama as color
import ascii
import orisha
import random
import game_symbols as gs
import ewi
import origins_mechanics as om
import game_animals as ga
import game_asides as gas
import yemoja_betrayal as yb
import odu
import oshun_failed_branch
import oshun_gameplay as gameplay
import threading
import origins_keys as keys
import amulets
import origins


def oshun_adventure():
    print(f"{orisha.oshun.name} says, '{color.Fore.LIGHTBLUE_EX}I have come to begin my quest for my powers, {orisha.orunmila.name}{color.Style.RESET_ALL}' \n")
    print(f"""
    {orisha.orunmila.name} replies, '{color.Fore.YELLOW}the frog stands still in the swamp till a dragonfly zips by, 
then he awakes. Go North East and meet {orisha.eshu.name}, the trickster, he would take you to where the other gods and 
goddess are. At the path where the sun kisses the tallest tree, stop and greet {orisha.agemo_the_chameleon.name} 
the chameleon, he would help you.{color.Style.RESET_ALL}'
    """)
    ascii.orunmila_symbol.print_orisha_symbol()
    om.origins_compass()

    if om.movements() == "ne" or "northeast" or "north east":
        ascii.yemoja_symbol.print_orisha_symbol()
        meet_agemo = input(f"""There's a little mountain east of you,
        it seems {orisha.agemo_the_chameleon.name} is there. Do you want to go there? 
        """)
        if meet_agemo.lower() == "y" or meet_agemo.lower() == "yes":
            ascii.agemo_symbol.print_orisha_symbol()
            print(f"""
                    {orisha.agemo_the_chameleon.name} is at the tip of the mountain,
                    it is as if he is listening to an odu 
                    the sun is saying.

                    """)
            print(f"""
                    {orisha.agemo_the_chameleon.name} sees {orisha.oshun.name} coming and immediately takes a
                    serious stance and stops listening to the sun
                    """)

            def talk_with_agemo_answer():
                talk_with_agemo = input(f"Do you want to talk with {orisha.agemo_the_chameleon.name}? y or n")

                if "yes" in talk_with_agemo.lower() or "y" in talk_with_agemo.lower() or "would talk" in \
                        talk_with_agemo.lower():
                    print("\n")
                    oshun_talk_with_agemo()
                    # print(f"You have 0 answers left \n")
                    # print(
                    # f"{orisha.agemo_the_chameleon.name}, says you are not worthy of any power, your destiny must
                    # wait.")
                else:
                    print(f"You have to talk with {orisha.agemo_the_chameleon.name}, type 'yes' instead")
                    talk_with_agemo_answer()

            talk_with_agemo_answer()

            # oshun_talk_with_agemo()

            # ewi_alt_path() ---> I am building it in the orisha_failed_branch file
            #oshun_victory()

            #oshun_adventure_two()

        elif meet_agemo.lower() != "y" or meet_agemo.lower() != "yes":
            print(f"""
                {orisha.oshun.name}, where else would you go? You have to talk with {orisha.agemo_the_chameleon.name} as
                {orisha.orunmila.name} instructed. Say 'yes' instead\n""")
            oshun_adventure()
    else:
        print(f" You don't want to fulfil your destiny? Why {orisha.oshun.name}? \n ")
        oshun_failed_branch.oshun_branch()


# Random reply generator

replies = (f"""
        Let {orisha.agemo_the_chameleon.name} know you did not come all this way to bath in the sun. Tell him 'yes'
        """, f"""
        {orisha.oshun.name} are you telling me you're not worthy? I know you are, tell {orisha.agemo_the_chameleon.name}
        that you are worthy""", f"""Let {orisha.agemo_the_chameleon.name} know you did not come all this way to bath in 
        the sun. Tell him 'yes' """)

random_replies = random.choice(replies)


def oshun_talk_with_agemo():
    print(f"""
{orisha.agemo_the_chameleon.name} says, '{color.Fore.LIGHTGREEN_EX}What brings you to my mountains, 
{orisha.oshun.name}?{color.Style.RESET_ALL}' \n
""")
    print(f"""
{color.Fore.LIGHTBLUE_EX}I have come searching for powers, {orisha.orunmila.name} told me you would have 
answers{color.Style.RESET_ALL} \n
""")
    print(f"{orisha.agemo_the_chameleon.name} takes his time to reply.")
    gs.tears.print_game_symbol()
    print(f"""
{orisha.agemo_the_chameleon.name} says, '{color.Fore.LIGHTGREEN_EX}It is not about what you want, it is about 
if you are worthy for what you want?{color.Style.RESET_ALL}' \n
    """)

    # oshun_reply_one = input("What is your answer? ")

    oshun_reply_one = input(f"{orisha.agemo_the_chameleon.name} asks, '{color.Fore.LIGHTGREEN_EX}are you worthy?' {color.Style.RESET_ALL}")

    if "yes" in oshun_reply_one.lower() or "y" in oshun_reply_one.lower() or \
            "maybe" in oshun_reply_one.lower():
        print(f"{orisha.oshun.name} says {color.Fore.LIGHTBLUE_EX}yes{color.Style.RESET_ALL} \n")
        print(f"{orisha.agemo_the_chameleon.name} says, '{color.Fore.LIGHTBLUE_EX}Then you have to prove yourself.\n'\
        You must answer this riddle after which you would be handed three pebbles which\n\
        you must throw at the groove where the owl sleeps{color.Style.RESET_ALL}\n")
        ewi.agemo_ewi.print_ewi()

        """
        def ewi_answer_loop():
            # global oshun_ewi_answer
            oshun_ewi_answer = input("What is your answer to this riddle? ")
            return oshun_ewi_answer
        """

        def ewi_answer_loop():
            answer_tries = 3
            while True:
                oshun_ewi_answer = input("What is your answer to this riddle? ").lower()
                if oshun_ewi_answer == "h" or oshun_ewi_answer == "help":
                    print("****r*a**")
                    continue
                if oshun_ewi_answer != "cockroach":
                    print(f"You have {answer_tries} answers left")
                    answer_tries -= 1
                    if answer_tries == 0:
                        print(f"you have {answer_tries} answers left \n")
                        print(f"""
                        {orisha.agemo_the_chameleon.name} says, you have proven not to be worthy {orisha.oshun.name} 
                        I am disappointed.\n""")
                        break
                    #Need to work on this path
                # print game map
                # go back to the north to meet orunmila
                # create a failed branch in orisha_adventure called failed_agemo_quest(),
                # Orunmila would ask another riddle
                # if success, come back here and start the orisha_adventure from the beginning
                # if no/failure then game ends. print an odu before ending the game
                # then create a sort of outro for game endings.
                # should be hints/tips? there should be hints/tips

                # call the orisha_failed_branch function
                elif oshun_ewi_answer == "cockroach":
                    print(f"O kare {orisha.oshun.name}!")
                    break
                else:
                    print(f"{orisha.oshun.name} you have failed!")
                    oshun_failed_branch.oshun_branch()

        ewi_answer_loop()

        oshun_victory()

    elif "no" in oshun_reply_one.lower() or "not sure" in oshun_reply_one.lower() or \
            "nothing" in oshun_reply_one.lower():
        print(f"{orisha.oshun.name} says, {color.Fore.LIGHTBLUE_EX}{oshun_reply_one}{color.Style.RESET_ALL} \n")
        print(random_replies)
        oshun_talk_with_agemo()
    else:
        print(random_replies)
        oshun_talk_with_agemo()


def oshun_yemoja_scene():
    om.origins_compass()
    print(f"{orisha.erinle.name} is South from here \n")
    om.movements()
    if "s" or "south" in om.movements():
        gs.leaf.print_game_symbol()
        print("\n")
        gs.mountains.print_game_symbol()
        print("\n")
        gs.huts.print_game_symbol()
        print("\n")
        print(f"""
            {orisha.yemoja.name} has seen Oshun making a delicate turn by the mountain pass. 
            The leaves sing a beautiful song and everything that's light is in a dark trance
            """)
        print(f"{orisha.yemoja.name}, {color.Fore.GREEN}you are more beautiful than the sun; you are welcome.{color.Style.RESET_ALL} \n")
        # print("it's good to hear that you have gone far in your journey.")
        print(f"""
{orisha.oshun.name} says, '{color.Fore.LIGHTBLUE_EX}you remind me of the bluest ocean whose gaze Olodumare rests 
upon'{color.Style.RESET_ALL} \n
""")
        print(f"""
{orisha.yemoja.name} says, '{color.Fore.GREEN}the sugar on your lips today would make ants dance.
{color.Style.RESET_ALL}' \n
""")
        print(f"""
        {orisha.oshun.name} says, '{color.Fore.LIGHTBLUE_EX}I am just passing by and wanted to inform a good friend 
and sister of my progress in getting my powers{color.Style.RESET_ALL}'\n
        """)
        print(f"{orisha.yemoja.name} says, '{color.Fore.GREEN}May Olodumare guide and protect you{color.Style.RESET_ALL}' \n")
        print("Ase!")
        gs.foot_steps.print_game_symbol()
    else:
        alt_choice = input("Where else would you rather go? ")
        print(f"""
        You cannot go to {alt_choice}. {orisha.erinle.name} is South from here and that's where destiny is waiting.
        """)
        oshun_yemoja_scene()


def black_peacock():
    print(f"""
{orisha.orunmila.name} is dumbfounded. This act of betrayal is exactly what {orisha.agemo_the_chameleon.name}
spoke aboke.{orisha.orunmila.name} cannot believe that his convictions and expectations have been broken so easily
""")
    ga.dove.print_animal_symbol()
    print("\n")
    print(f"""
{orisha.yemoja.name} says,{color.Fore.GREEN} {orisha.orunmila.name} whose flock the clouds clean, whose wisdom 
knows no end I have come with the Black Peacock, devoid of any colors, a rarity for you.{color.Style.RESET_ALL}\n
""")
    print(f"""
{orisha.orunmila.name} says, '{color.Fore.YELLOW}And who told you to bring the Black Peacock here? Have you met 
{orisha.oshun.name}? Did you kill {orisha.oshun.name}, {orisha.yemoja.name}?{color.Style.RESET_ALL}\n
    """)
    print(f"""
{color.Fore.GREEN}{orisha.oshun.name} is a friend I hold dear, for a 1000 years, we have known each other, we have 
watched mountains grow from debris till it reaches the sky; but when rain is falling from the heavens, even the oceans 
overflow.\n{color.Style.RESET_ALL}""")
    ascii.orunmila_symbol.print_orisha_symbol()
    print("\n")
    ascii.yemoja_symbol.print_orisha_symbol()

    i = 0
    while i < 5:
        print(gs.foot_steps.print_game_symbol())
        i += 1

    # Pass the function for help, save or exit option here. You would listen for Keypress: h for help, s for save, x\
    # for exit, c for continue.

    gs.mountains.print_game_symbol()

    print(f"""
{orisha.oshun.name} makes her way towards the mountains. She has searched everywhere for the {ga.peacock.animal_name}. 
She is devastated.
""")
    print(f"""
With a high-pitched voice, {orisha.oshun.name} wails, her cries pepper the leaves, flattens the grass and it is 
believed this was how the vegetable Pepper came to be. {orisha.orunmila.name} wears an expressionless face. 
Is this another deceit?
""")
    odu.orunmila_odu_one.print_odu()
    print("\n")
    print(f"""
{orisha.orunmila.name}, {color.Fore.LIGHTBLUE_EX}I have gone to the forests to search for {orisha.erinle.name}, 
but {orisha.erinle.name} is not there I have with palms out, knees bent and throat dry, {orisha.orunmila.name}, I have 
failed you{color.Style.RESET_ALL} \n
""")
    print(f"""
{orisha.orunmila.name} says, {color.Fore.LIGHTBLUE_EX}it is I who has failed you all. I should have known that 
having special abilities would create rancour, bitterness and betrayal amongst you Orishas{color.Style.RESET_ALL}""")

    for i in range(1):
        for j in range(2):
            print("\\" * 200)
            print("/" * 200)

    print("\n")
    print(f"""
The grasses swoon a graceful yet suspenseful song, swinging to the left then to the right like a delirious choir. 
The air is tight. {orisha.oshun.name} sees {orisha.yemoja.name} and her face says it all. She sees the Black Peacock 
with no colors in the grasps of {orisha.yemoja.name}
""")


def oshun_gratitude():
    oshun_gratitude_reply = input(f"{orisha.oshun.name} says, \n")
    if oshun_gratitude_reply != "" and oshun_gratitude_reply.isalpha() is True and\
            oshun_gratitude_reply.isnumeric() is False:
        return oshun_gratitude_reply.lower()
    elif oshun_gratitude_reply == "":
        print(f"Say something to {orisha.orunmila.name}, so he would be kind to you")
        oshun_gratitude()
    elif oshun_gratitude_reply.isnumeric() is True or oshun_gratitude_reply.isalpha() is False:
        print(f"Your words are your bond, not numbers or anything else {orisha.oshun.name}")
        oshun_gratitude()
    else:
        oshun_gratitude()


def oshun_victory():
    def pebbles():
        pebbles_drop = input("Do you want to drop the pebbles in the river? ")
        return pebbles_drop.lower()

    odu.oshun_odu_two.print_odu()
        # print a sort of intro for the quest/ an odu or dialogue
    om.origins_compass()
        # print the compass
    oshun_groove_choice = input(
        "The Groove where the Owl sleeps is South-West from here.\n Do you want to go there?")
    if oshun_groove_choice.lower() == "yes" or oshun_groove_choice.lower() == "y":
        print(f"{orisha.oshun.name} are you sure you're ready to go to the Groove where the Owl sleeps? \n")
        oshun_groove_sure = input("Are you sure? ")
        if oshun_groove_sure.lower() == "yes" or oshun_groove_sure.lower() == "y":
            print("The Groove where the Owl sleeps is South-West from here. May Olodumare guide you.")
        else:
            pass

    i = 0
    while i < 4:
        gs.foot_steps.print_game_symbol()
        i += 1
        # print the foot walk ascii art
    gs.tears.print_game_symbol()  # I am meant to display the may for the game and not the tears symbol
        # print a map showing the groove
    gs.huts.print_game_symbol()

    def compel_question_function():
        compel_question = input("You must need water after such a long day?")
        while compel_question.lower() == "yes" or compel_question.lower() == "y":
            break
        else:
            compel_question_function()

    compel_question_function()

    print("""
    I am glad you want to rest.\n The african pelican bird does not migrate without enough food and water.
    Drink lots of water, your destiny awaits you
    """)

        # branch to a hut to get water
    print("Who's there?")

    oshun_reply_oya_one = input(f"What brings you here {orisha.oshun.name} \n")
    if oshun_reply_oya_one.lower() == "groove" or oshun_reply_oya_one.lower() == "the groove where the owl sleeps" or \
            oshun_reply_oya_one.lower() == "the groove":
        print(f"{orisha.oya.name}, {color.Fore.LIGHTBLUE_EX}{oshun_reply_oya_one}{color.Style.RESET_ALL}")
        print(f"O kare!, but before you go {orisha.oshun.name}")

    def thinking_activity():
        print((".") * 3)

    i = 0
    while i < 3:
        thinking_timer = threading.Timer(4.0, thinking_activity)
        thinking_timer.start()
        i += 1

    def first_line():
        ewi.aje_riddle.print_ewi()
        orange_riddle = input("What happened to my oranges?\n  ")
        if "ate" or "eat" in orange_riddle.lower():
            print(f"""
{color.Fore.CYAN}O kare {orisha.oshun.name}, take this Eternal Flame and may it help you find 
your powers\n{color.Style.RESET_ALL}
""")
            gs.eternal_flame.print_game_symbol()
            keys.save.key_action("Eternal Flame")
            print("\n")
            print(f"{orisha.oshun.name} replies, {color.Fore.LIGHTBLUE_EX}Ase Oya!{color.Style.RESET_ALL}")
        else:
            first_line()

    first_line()

    odu.oshun_odu_three.print_odu()

    ga.owl.print_game_symbol()

    gs.river.print_game_symbol()

    pebbles()

    if "yes" or "y" in pebbles():
        gs.pebbles.print_game_symbol()
        print("\n")
        gs.river.print_game_symbol()
        print("\n")
        print(f"O kare {orisha.oshun.name} you have completed Stage 1 of your quest to get your powers.")
        oshun_adventure_two()
    else:
        print("Why don't you want to drop the pebbles?\n")
        print(f"{orisha.oshun.name}, you are an enigma. Your pebbles have been dropped for you\n")
        oshun_adventure_two()


def oshun_adventure_two():
    ascii.orunmila_symbol.print_orisha_symbol()
    gs.mountains.print_game_symbol()

    print(f"""{orisha.orunmila.name} says, '{color.Fore.YELLOW}You have done your first quest {orisha.oshun.name}?
{color.Style.RESET_ALL}' \n""")
    print(f"""
{orisha.oshun.name} says,{color.Fore.LIGHTBLUE_EX} yes {orisha.orunmila.name}. I have dropped the three pebbles 
inside the river close to the groove where the owl sleeps{color.Style.RESET_ALL}
""")

    ga.dove.print_game_symbol()

    print(f"""
{orisha.orunmila.name} says, '{color.Fore.YELLOW}Your next and final task is to find the 
{amulets.black_peacock.amulet_name}{color.Style.RESET_ALL}'
""")

    ga.dove.print_game_symbol()

    print(f"""
{orisha.orunmila.name} says, {color.Fore.YELLOW}go to {orisha.erinle.name} who already has the powers of the 
Elephant and tell him all I have told you{color.Style.RESET_ALL}
""")

    oshun_gratitude()
    oshun_yemoja_scene()
    gas.orunmila_and_agemo.asides_play()
    yb.yemoja_betrayal()
    odu.oshun_odu_three.print_odu()
    black_peacock()

    print(f"""
{orisha.oshun.name} says, {color.Fore.LIGHTBLUE_EX}{orisha.orunmila.name} it would be unfair for my sister, {orisha.yemoja.name}, 
to receive the Eye of the Storm without first passing the test. Let her answer {orisha.agemo_the_chameleon.name}'s 
riddle then I would accept defeat{color.Style.RESET_ALL}\n
""")
    print(f"{color.Fore.GREEN}How dare you tell {orisha.orunmila.name} what to do?, {orisha.yemoja.name} retorts.\
    {color.Style.RESET_ALL}\n")
    print(f"{color.Fore.YELLOW}Quiet!\n{color.Style.RESET_ALL}")
    print(f"""
{color.Fore.YELLOW}{orisha.yemoja.name}, your betrayal stinks to the Heavens, Oshun is your sister and she 
confided in you yet you have set your foot as she was about to run. Whomever answers this riddle shall 
get{amulets.eye_of_the_storm.amulet_name}.{color.Style.RESET_ALL}\n
    """)

    ewi.orunmila_ewi_for_yemoja.print_ewi()

    def endgame_ewi():
        endgame = input("What am I? press h for hint ")
        if endgame.lower() == "tears":
            # pass a function here for outro
            print(f"""
            You have won the game {orisha.oshun.name}. You have received the power to control the Water Elements.
            """)
            gs.tears.print_game_symbol()
            keys.save.key_action_three(amulets.eye_of_the_storm.amulet_name)
            play_again = input("Do you want to start again with a different Orisha? ")
            if play_again.lower() == "yes" or play_again.lower() == "y":
                print("Make sure you select a different element. May the Orishas guide you on your way...")
                origins.origins()
            else:
                keys.exit.key_action()
        elif endgame.lower() == "h" or endgame.lower() == "help":
            print("****s")
            endgame_ewi()
        else:
            print(f"You failed the ewi {orisha.oshun.name}")
            odu.oshun_odu_four.print_odu()
            gameplay.oshun_gameplay()

    endgame_ewi()




#oshun_adventure_two()