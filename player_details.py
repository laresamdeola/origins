import ascii
import orisha
import origins_keys as ork
import random


class PlayerCreation:
    def __init__(player, player_name, player_elements, player_color, player_number, player_day, player_metal):
        player.player_name = player_name
        player.player_elements = player_elements
        player.player_color = player_color
        player.player_number = player_number
        player.player_day = player_day
        player.player_metal = player_metal

    def the_player_name(player):
        player.player_name()

    def the_player_elements(player):
        player.player_elements()

    def the_player_color(player):
        player.player_color()

    def the_player_number(player):
        player.player_number()

    def the_player_day(player):
        player.player_day()

    def the_player_metal(player):
        player.player_metal()


def player_name_details():
    try:
        player_name_input = input("What is your name? ").lower()
        name = player_name_input
        if player_name_input.isalpha() is True:
            print(f"Welcome to ORIGINS {name} \n")
            with open("name.txt", 'w') as save_object:
                save_object.write(name + " ")
        elif player_name_input.isalpha() is False:
            invalid_name_reply = ("You can do better than this :)", "What kind of name is that?&%$",
                                  "Are you for real, that's an actual name??",
                                  f"You entered an invalid character:\
             {player_name_input}. Your name can only be the letters a - z",
                                  f"You entered an invalid character: {player_name_input}.\
             Your name can only be the letters a - z.")
            random_name_reply = random.choice(invalid_name_reply)
            print(random_name_reply)
            player_name_details()
    except Exception as name_error:
        print(f"You entered an invalid word: {name_error}. Enter only text characters and not numbers or \
        special characters.")
        player_name_details()


def player_elements_details():
    try:
        elements = ["water", "fire", "air", "earth"]
        player_elements_input = input("What is your favorite natural element? ").lower()
        the_element = player_elements_input
        if player_elements_input.isalpha() is True and player_elements_input in elements:
            print(f"Your natural element is {the_element} \n")
            with open("elements.txt", 'w') as elements_object:
                elements_object.write(the_element + " ")
        elif player_elements_input.isalpha() is False or player_elements_input not in elements:
            invalid_elements_reply = ("You can do better than this :)", "What did you just write?&%$",
                                      f"What kind of element is {player_elements_input}?",
                                      f"You can only choose one of four elements: water, fire, air or earth.\
            You chose {player_elements_input}")
            random_elements_reply = random.choice(invalid_elements_reply)
            print(random_elements_reply)
            player_elements_details()
    except Exception as ele_error:
        print(f"You entered an invalid word: {ele_error}. Enter only text characters and not numbers or \
        special characters.")
        player_elements_details()


def player_color_details():
    try:
        player_color_input = input("What is your favorite color? ").lower()
        color = player_color_input
        if player_color_input.isalpha() is True:
            print(f"Your favorite color is {color} \n")
            with open("color.txt", 'w') as color_object:
                color_object.write(color)
        elif player_color_input.isalpha() is False:
            invalid_color_reply = ("We both know that is not a color :(",
                                   f"So today you wore the color {player_color_input}", "ROYGBIV remember :)",
                                   f"Yellow is a color, blue is a color, {player_color_input} isn't one :("),
            f"You entered an invalid character: {player_color_input}. No color starts with a number :( Let's try again."
            random_color_reply = random.choice(invalid_color_reply)
            print(random_color_reply)
            player_color_details()
    except Exception as col_error:
        print(f"You entered an invalid word: {col_error}. Enter only text characters and not numbers or \
        special characters.")
        player_color_details()


def player_number_details():
    try:
        player_number_input = input("What is your favorite number? ").lower()
        number = player_number_input
        if player_number_input.isnumeric() is True:
            print(f"Your favorite number is {number} \n")
            with open("number.txt", 'w') as number_object:
                number_object.write(number)
        elif player_number_input.isnumeric() is False:
            invalid_number_reply = ("Lets count to 10: 1 2 3 4 5 6 7 8 ... :)", "Numbers not alphabets or special\
             characters", """
            Do you know there are over 9000 Orishas in the Yoruba Pantheon? Please select from
            numbers 1 - 10 and not 9000 :)
            """)
            random_number_reply = random.choice(invalid_number_reply)
            print(random_number_reply)
            player_number_details()
    except Exception as num_error:
        print(f"You entered an invalid word: {num_error}. Enter only text characters and not numbers or \
        special characters.")
        player_number_details()


def player_day_details():
    try:
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        player_day_input = input("What is your favorite day of the week? ").lower()
        day = player_day_input
        if player_day_input.isalpha() is True and player_day_input in days:
            print(f"Your favorite day is {day} \n")
            with open("day.txt", 'w') as day_object:
                day_object.write(day)
        elif player_day_input.isalpha() is False:
            invalid_day_reply = ("You have forgotten your days of the week??", f"""
                What kind of day is {player_day_input}?
                Days of the week like funday or some day! Just joking.
                """, f"""
The Yorubas have special names for days of the week. Thursdays are called Ojobo
""")
            random_day_reply = random.choice(invalid_day_reply)
            print(random_day_reply)
            player_day_details()
        else:
            invalid_day_reply = ("You have forgotten your days of the week??",
                                 f"""
                What kind of day is {player_day_input}?
                Days of the week like funday or some day! Just joking.
                """, "The Yorubas have special names for days of the week. Thursdays are called Ojobo")
            random_day_reply = random.choice(invalid_day_reply)
            print(random_day_reply)
            player_day_details()
    except Exception as day_error:
        print(f"You entered an invalid word: {day_error}. Enter only text characters and not numbers or \
        special characters.")
        player_day_details()


def player_metal_details():
    try:
        precious_metals = ["gold", "silver", "bronze", "brass", "ruby", "sapphire", "onyx", "diamond", "diamonds"]
        player_metal_input = input("What is your favorite precious metal? ").lower()
        metal = player_metal_input
        if player_metal_input.isalpha() is True and player_metal_input in precious_metals:
            print(f"Your favorite metal is {metal} \n")
            with open("metal.txt", 'a') as metal_object:
                metal_object.write(metal + " ")
        elif player_metal_input.isalpha() is False:
            invalid_metal_reply = ("Bling Bling, rappers love wearing them", f"""
Can you wear {player_metal_input} on your neck?""", """
One of the precious metals in Yoruba land is Brass. It is known to be beloved by many
Orishas like Oshun, Obatala""")
            random_metal_reply = random.choice(invalid_metal_reply)
            print(random_metal_reply)
            player_metal_details()
        else:
            invalid_metal_reply = ("Bling Bling, rappers love wearing them", f"Can you wear {player_metal_input} \
                        on your neck?", "One of the precious metals in Yorubaland is Brass. It is knownto be beloved by many \
                        Orishas like Oshun, Obatala")
            random_metal_reply = random.choice(invalid_metal_reply)
            print(random_metal_reply)
            player_metal_details()
    except Exception as met_error:
        print(f"You entered an invalid word: {met_error}. Enter only text characters and not numbers or \
        special characters.")
        player_metal_details()


player_one = PlayerCreation(player_name_details, player_elements_details, player_color_details, player_number_details,
                            player_day_details, player_metal_details)


# <--------------------------------------------------------------- Player Details Functions for Testing ---------------------------------------------------------------------------------------->

# Player Name

def is_lower():
    name = input("What is your name? ")
    return name.lower()


def not_number():
    name = input("What is your name? ")
    if name.isalpha() is True:
        return True
    elif name.isalpha() is not True:
        return False


#Player Elements

def is_element_lower():
    elements = input("What is your favorite natural element? ")
    return elements.lower()


def is_element():
    elements = input("What is your favorite natural element? ")
    elements_list = ["water", "fire", "air", "earth"]
    if elements in elements_list:
        return True
    else:
        return False


def is_an_element_name():
    elements = input("What is your favorite natural element? ")
    if elements.isalpha() is True:
        return True
    elif elements.isalpha() is not True:
        return False


def is_element_name_lower():
    elements = input("What is your favorite natural element?")
    if elements.isalpha() is False:
        return False
    if elements.isalpha() is True:
        return True


#Color

def is_color_lower():
    color = input("What is your favorite color? ")
    return color.lower()


def is_not_a_word():
    color = input("What is your favorite color? ")
    if color.isalpha() is True:
        return True
    elif color.isalpha() is not True:
        return False


def is_special_character():
    color = input("What is your favorite color? ")
    if color.isalpha() is True:
        return True
    elif color.isalpha() is not True:
        return False


# Day

def is_day_lower():
    days = input("What is your favorite day of the week? ")
    return days.lower()


def is_day():
    days = input("What is your favorite day of the week? ")
    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if days in days_list:
        return True
    else:
        return False


def is_a_day_name():
    days = input("What is your favorite day? ")
    if days.isalpha() is True:
        return True
    elif days.isalpha() is not True:
        return False


# Metal

def is_metal_lower():
    metals = input("What is your favorite metal? ")
    return metals.lower()


def is_metal():
    metals = input("What is your favorite metal? ")
    precious_metals = ["gold", "silver", "bronze", "brass", "ruby", "sapphire", "onyx", "diamond", "diamonds"]
    if metals in precious_metals:
        return True
    else:
        return False


def is_a_metal_name():
    metals = input("What is your favorite metal? ")
    if metals.isalpha() is True:
        return True
    elif metals.isalpha() is not True:
        return False



#player_metal_details()



#elements_present()



"""
def player_elements_details():
    try:
        elements = ["water", "fire", "air", "earth"]
        player_elements_input = input("What is your favorite natural element? ").lower()
        if player_elements_input.isalpha() is True and player_elements_input in elements:
            print(f"Your natural element is {player_elements_input} \n")
            with open("elements.txt", 'w') as elements_object:
                elements_object.write(player_elements_input)
        elif player_elements_input.isalpha() is False or player_elements_input not in elements:
            invalid_elements_reply = ("You can do better than this :)", "What did you just write?&%$",
                                      f"What kind of element is {player_elements_input}?",
                                      f"You can only choose one of four elements: water, fire, air or earth.\
            You chose {player_elements_input}")
            random_elements_reply = random.choice(invalid_elements_reply)
            print(random_elements_reply)
            player_elements_details()
    except Exception as ele_error:
        print(f"You entered an invalid word: {ele_error}. Enter only text characters and not numbers or \
        special characters.")
        player_elements_details()
"""

#player_one.player_elements()

# <-------------------------------------- Sorting Algorithms ------------------------------------------>

#name_of_tuple = ("x1", "x2", ... x(n))
#name_of_random_number = random.choice(name_of_tuple)

# <---------------------------------------------------------------------------------------------------->

#player_name_details()
"""
    def player_details():

        player_name = input("What is your name? ").lower()
        print(f"Welcome to ORIGINS {player_name} \n")
        return player_name

        player_elements = input("What is your favorite natural element? ")
        player_color = input("What is your favorite color? ")
        player_number = input("What is your favorite number? ")
        player_day = input("What is your favorite day of the week? ")
        player_metal = input("What is your favorite precious metal? ")

        if player_elements.lower() == "water" and (player_color.lower() == "yellow" or player_color.lower() == "gold") \
        and player_number == "5" and player_day.lower() == "friday" and (
        player_metal.lower() == "gold" or player_metal.lower() == "copper"
        or player_metal.lower() == "brass"):
            print(f"Your Orisha affinity is {orisha.oshun.name}: goddess of the sea and water bodies \n")
            print(ascii.yemoja_symbol.ascii_art + "\n")
            print("""
        #Welcome to ORIGINS. You would be using the goddess Oshun. She is the goddess of water
        #and water bodies. \n
        #)
        #player_choice = input("Do you want to know more about Oshun? ")
        #if player_choice.lower() == "yes" or player_choice.lower() == "y":
        #print(orisha.oshun.origin_story[0:500] + "\n")
        #else:
        #print("Please type 'yes' to continue playing ORIGINS \n")
"""


# ork.save_key.key_action()

# 1. Work more on the validation to make it easy and clear to choose Orishas
# 2. Create the Validation for 2 more characters - Ogun and Sango.

# player_details()


#class PlayerDetails:
#def __init__(self, elements, favorite_color, temperament):
#self.elements = elements
#self.favorite_color = favorite_color
#self.temperament = temperament

#player_one = PlayerDetails("fire", "white", "cool")

#print(player_one.elements)
"""



