import orisha
import ascii
import odu
import game_symbols as gs
import ewi
import oshun_failed_branch as ofb
import amulets
import origins_keys as keys
import ogun_gameplay as ogun
import colorama as color


def ogun_adventure_one():
    print(f"{orisha.ogun.name} just passed the tree with a single leaf.\n")
    ascii.agemo_symbol.print_orisha_symbol()
    print(f"""
            {orisha.agemo_the_chameleon.name} sees {orisha.ogun.name} coming. Nothing can be read from 
            {orisha.agemo_the_chameleon.name}\n""")
    print(f"""
            With a thunderous and firm voice, {orisha.ogun.name} says, '{color.Fore.MAGENTA}{orisha.agemo_the_chameleon.name}, 
            I have come so you might direct me on my quest to get my powers!{color.Style.RESET_ALL}'
            """)
    print(f"{color.Fore.LIGHTGREEN_EX}Is that why you sound like red hot iron thrust into water?{color.Style.RESET_ALL}, says {orisha.agemo_the_chameleon.name}\n")
    print(f"""
            {orisha.ogun.name} is silent, but not the silence of cowardice or fear, but that of a panther's eyes, 
            piercing through the night, watching the beating heart of its prey
            """)
    print(f"""{color.Fore.LIGHTGREEN_EX}
            The destiny that awaits you is that of WAR! Are your legs still curious? Is your voice still thunderous?
            {color.Style.RESET_ALL}""")

    odu.ogun_odu_one.print_odu()

    steps = 8
    while steps >= 0:
        gs.foot_steps.print_game_symbol()
        if steps == 5:
            print(f"{orisha.ogun.name} is trotting up and down the mountains, he is displaying his energy and \
                    tenacity to {orisha.agemo_the_chameleon.name}. The message is read\n")
        steps -= 1

    ewi.agemo_ewi_two.print_ewi()

    answer_tries_one = 3
    while answer_tries_one >= 0:
        ogun_riddle_answer = input("What am I? ")
        # answer_tries_one -= 1
        if ogun_riddle_answer.lower() == "chameleon":
            print(f"""{orisha.agemo_the_chameleon.name} says, {color.Fore.LIGHTGREEN_EX}your spark has matched your fire. 
                        {orisha.orunmila.name} is East from here.{color.Style.RESET_ALL}\n""")
            break
        if answer_tries_one == 1:
            print(f"{orisha.agemo_the_chameleon.name} says, {color.Fore.LIGHTGREEN_EX}you have one more try left {orisha.ogun.name}{color.Style.RESET_ALL}")
            hint_for_ogun = input("Do you need a hint? ")
            if hint_for_ogun.lower() == "yes" or hint_for_ogun.lower() == "y":
                chameleon_answer = input("*h******n")
                if chameleon_answer.lower() == "chameleon":
                    print(f"{color.Fore.LIGHTGREEN_EX}{orisha.ogun.name} you have finally proven yourself{color.Style.RESET_ALL}")
                    break
                elif chameleon_answer.lower() != "chameleon":
                    ofb.failed_branch_ogun()
                    break
            elif hint_for_ogun.lower() == "no" or hint_for_ogun.lower() == "n":
                print(f"{color.Fore.LIGHTGREEN_EX}You should have used the hint {orisha.ogun.name}{color.Style.RESET_ALL}")
                ofb.failed_branch_ogun()
                break
        elif answer_tries_one == 0:
            print(f"{color.Fore.LIGHTGREEN_EX}{orisha.ogun.name}, the Irunmole's would be disappointed. Go and prepare for your destiny!{color.Style.RESET_ALL}\n")
            ofb.failed_branch_ogun()
            break
        answer_tries_one -= 1
        print(f"You have {answer_tries_one} answers left {orisha.ogun.name}")

    ogun_adventure_two()


def ogun_adventure_two():
    print(orisha.ogun.origin_story)
    print("\n")

    gs.river.print_game_symbol()

    print("\n")
    gs.mountains.print_game_symbol()

    orunmila_waits = input(f"{orisha.orunmila.name} says, {color.Fore.YELLOW}I have been waiting for you {orisha.ogun.name}{color.Style.RESET_ALL}\n")
    print(f"{orisha.ogun.name} says, {color.Fore.MAGENTA}{orunmila_waits}{color.Style.RESET_ALL}\n")

    #print(f"{color.Style.RESET_ALL}")

    ascii.orunmila_symbol.print_orisha_symbol()

    print(f"{color.Fore.MAGENTA}I have passed {orisha.agemo_the_chameleon.name}'s test, I am here for my quest {orisha.orunmila.name}{color.Style.RESET_ALL}\n")
    print(f"""{color.Fore.YELLOW}
       I know what brings you here just like I knew when you were came to be or the love you have for your twin. 
       But there's more you have to do{color.Style.RESET_ALL}
       """)
    print(f"{color.Fore.YELLOW}You would have to answer this riddle, {orisha.ogun.name}:{color.Style.RESET_ALL}")

    ewi.orunmila_ewi_for_ogun_one.print_ewi()

    tries_two = 3
    while tries_two >= 1:
        orunmila_riddle = input("What is your answer? ").lower()
        tries_two -= 1
        if orunmila_riddle == "siamese twins":
            print(f"{orisha.orunmila.name} says, {color.Fore.YELLOW}you have done well {orisha.ogun.name}, O kare!{color.Style.RESET_ALL}")
            ogun_wants = input(f"{orisha.orunmila.name} asks, {color.Fore.YELLOW}what do you want {orisha.ogun.name}?{color.Style.RESET_ALL}")
            if "power" or "destiny" or "fate" in ogun_wants:
                print(f"""{color.Fore.YELLOW}
                   {orisha.orunmila.name} says, I have something for you {orisha.ogun.name}, 
                   this is called the {amulets.cloud_chariot.amulet_name}. I rode on it when Olodumare sent me 
                   from the heavens to create Aiye. Take it, may it guide you further on your journey.\n
                   {color.Style.RESET_ALL}""")
                print("amulet name:")
                amulets.cloud_chariot.print_amulet_name()
                print("\n")
                print("amulet description:")
                amulets.cloud_chariot.print_amulet_description()
                print("\n")
                print("amulet charm:")
                amulets.cloud_chariot.print_amulet_charm()
                print("\n")
                print(f"{orisha.ogun.name} says, mo dupe {orisha.orunmila.name}, I am most grateful.")

                keys.save_amulets(amulets.cloud_chariot.amulet_name)

                ascii.ogun_symbol.print_orisha_symbol()

                print(f"{color.Fore.YELLOW}Welcome to Stage 2 {orisha.ogun.name}{color.Style.RESET_ALL}")
                ogun_adventure_three()
                break
            elif tries_two == 0:
                print(f"The next time {orisha.orunmila.name} asks you what do you want, just say 'power'")
                break
        elif tries_two <= 0:
            print(f"{color.Fore.YELLOW}Go back and prepare yourself {orisha.ogun.name}!{color.Style.RESET_ALL}")
            ogun.ogun_gameplay()
            break
        print(f"You have {tries_two} tries left")

    #If the player gets the riddle, then go to stage 3.


def ogun_adventure_three():
    print("i'm here!!!!")