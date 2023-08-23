import orisha
import game_symbols as gs
import game_animals as ga
import ascii
import origins_mechanics as om
import odu
import oshun_adventure as oshun
import training
import colorama as color


def oshun_branch():
    odu.orunmila_odu_one.print_odu()

    print("""
    They say since hunters have learnt to shoot without missing, Enele the bird has learnt to fly without perching.
    You woud need to go South-West from here to meet the Great Diviner, it is in his stones that perhaps your path 
    would be revealed and wisdom granted unto you
    """)

    om.origins_compass()

    to_meet_ifa = input("You would have to go and meet Ifa the Great Diviner, he's South-West from here")

    if 'sw' in to_meet_ifa.lower() or 'southwest' in to_meet_ifa.lower() or 'south-west' in to_meet_ifa.lower():

        def grass_fields():
            print(("|") * 50)
            print("\n")
            print(("/") * 50)
            print("\n")
            print(("|") * 50)
            print("\n")

        grass_fields()

        print(f"{color.Back.BLACK}Welcome to the White Fields. Ifa the Great Diviner is not far from here{color.Style.RESET_ALL}")
        gs.leaf.print_game_symbol()
        print("\n")
        gs.foot_steps.print_game_symbol()
        print("\n")

        odu.oshun_odu_four.print_odu()
        print("\n")

        ga.owl.print_game_symbol()

        print("The Owl that does not sleep is by the tree. Who knows what gifts it bears? \n")
        print(f"""
{color.Fore.LIGHTRED_EX}{orisha.oshun.name}, you want to pass me by, don't you know that the hunter does not
go to the forest without his charms?{color.Style.RESET_ALL}
""")
        print(f"{orisha.oshun.name} increases her steps")

        for i in range(10):
            gs.foot_steps.print_game_symbol()

        print(f"""
{orisha.oshun.name} increases her pace but The Owl that does not sleep is remarkably spry
for it's reputation \n""")

        owl_talk = input("Do you want to talk to The Owl that does not sleep? ")

        if owl_talk.lower() == "y" or owl_talk.lower() == "yes":
            print(f"{orisha.oshun.name} says {owl_talk}")
            ascii.yemoja_symbol.print_orisha_symbol()
            owl_converse_one = input(f"{color.Fore.LIGHTRED_EX}Where are you off to {orisha.oshun.name}{color.Style.RESET_ALL} ")
            if "meet" in owl_converse_one.lower() or "going" in owl_converse_one.lower():
                print(f"""
                        {orisha.oshun.name} says {owl_converse_one}.\n 
                        {color.Fore.LIGHTBLUE_EX}I thought The Owl That Never Sleeps is abreast of all
                        that moves through these trees and grass \n{color.Style.RESET_ALL}""")
                print(f"{color.Fore.LIGHTRED_EX}{orisha.oshun.name} even the farmer with the keenest nose cannot smell\
                 the rain {color.Style.RESET_ALL}\n")
                print(f"""{color.Fore.LIGHTRED_EX}
The Owl That Never Sleeps says, because you have decided to talk with me, I have something 
for you {orisha.oshun.name} to help you along the quest {color.Style.RESET_ALL}\n""")
                print("But first you must answer this riddle {color.Style.RESET_ALL}\n")
                grass_fields()
                print(f"{orisha.oshun.name} sits on the grass, listening to {ga.owl.animal_name} riddle\n")

                print(f"{ga.owl.animal_name} says, \n")

                owl_riddle = input(f"""{color.Fore.LIGHTRED_EX}
                I am water
                I am light
                I am the sun
                I am the night
                What I'm I?{color.Style.RESET_ALL} \n""")

                # There should be a while loop counter here for amount of attempts. If more than 3 then move to this failed branch.
                # Provide and implement the key press functions here, it's applicability in the game should be tested here
                # provide the player with hints perhaps the hints should have a particular amount and should not be indefinite
                # if the player gets amulets, the player is granted more hints. The player should start with two hints then as
                # the player gets more amulets the hints increase.

                if "creation" in owl_riddle.lower() or "olodumare" in owl_riddle.lower():
                    print(f"""
{ga.owl.animal_name} says, {color.Fore.LIGHTRED_EX}you have done well {orisha.oshun.name} 
now here's a gold leaf for you, it fell from the first tree{color.Style.RESET_ALL} 
""")

                    gs.leaf.print_game_symbol()

                    print(f"{ga.owl.animal_name} says, {color.Fore.LIGHTRED_EX}let it be with you at all times{color.Style.RESET_ALL}")

                    oshun_thanks = input(" \n")
                    if "thank" in oshun_thanks or "happy" in oshun_thanks:
                        print(f"""
{color.Fore.LIGHTRED_EX}
you are welcome {orisha.oshun.name}, may Olodumare guide you towards wisdom.
When you see a river, follow your North, {orisha.ifa.name} is waiting for you{color.Style.RESET_ALL}
""")

                    # -- > Continue from here!

                    # 2. suggest they go south west to meet Ifa the and get great wisdom from Ifa
                    # 3. Oshun narrates her ordeal to Ifa
                    # 4. Ifa is in a garden filled with white lotus flowers and plenty oif white sand
                    # 5. He has long beards
                    # 6. An Odu of Ifa goes here
                    # 7. Oshun panics and has the option to forfeit her quest to get her powers
                    # 8. Ifa urges her not to give up, for failure is a stepping stone
                    # 9. Oshun's eyes swell with tears, she feels like a failure and for the first time as a goddess, she feels vulnerable, weak, human
                    # 10. this realisation grips her and it slowly grows to resignation
                    # 11. Ifa recites a great Odu for Oshun and sings her Oriki - praise names
                    # 12. Oshun seems revoitalized
                    # 13. Ifa then asks Oshun to tell the riddle that she failed
                    # 14. Oshun tells Ifa the riddle, Ifa gives Oshun  a necklace made out of her tears
                    # 15. Ifa tells Oshun that this necklace would give her infinite wisdom
                    # . 16. Oshun is revitalized, filled with vim and vigour
                    #  17. But on her way back to meet Agemo, she encounters Eshu the trickster god
                    # 18. Eshu tries to trick Oshun into giving him the necklace by making a bet that if she knows his riddle, he would come to her aid anytime
                    # 19. Eshu recites a very hard riddle, many lines long
                    # 20. But Oshun with her new infinte wisdom because of the tear drop necklace passes the riddle with ease ---> give a clue here
                    else:
                        print(f"{color.Fore.LIGHTRED_EX}You are ungrateful, Ifa is waiting for you {color.Style.RESET_ALL}\n")
                        ga.owl.print_game_symbol()
                        ga.dove.print_game_symbol()
                        print(f"{ga.owl.animal_name} has flown away angrily without giving you directions \
                        next time always reply with thanks {orisha.oshun.name}")
                        oshun.oshun_adventure()
                elif owl_riddle.lower() == "t" or owl_riddle.lower() == "training":
                    print("You need some training?")
                    training.training_ground_one()
                    # pass the function to continue the game here

                #elif whereby the player misses the question
        elif owl_talk.lower().lower() == "t" or owl_talk.lower().lower() == "training":
            print("You need some training?")
            training.training_ground_one()
        else:
            # -- continue the branch to meet Ifa
            print(f"You have not proven yourself {orisha.oshun.name}, you must be ready, like a palm tree is.")
            oshun_branch()


def failed_branch_ogun():
    print("Beginning of failed branch")

#failed_branch_oshun()



