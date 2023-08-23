import oshun_gameplay as oshun
import ogun_gameplay as ogun


def orisha_selection():
    with open("elements.txt", 'r') as elements_object:
        player_element = elements_object.readlines()
        if player_element[0] == "water":
            oshun.oshun_gameplay()
        elif player_element[0] == "earth":
            ogun.ogun_gameplay()

