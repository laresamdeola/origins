import oshun_gameplay as oshun
import ogun_gameplay as ogun


def orisha_selection():
  player_element = ""
  with open("elements.txt", 'r') as elements_object:
    player_element = elements_object.readlines()
    player_element = str(player_element[0])
    print(type(player_element))
    print(player_element)
    if player_element == "water":
      #print(player_element)
      oshun.oshun_gameplay()
    elif player_element == "earth":
      ogun.ogun_gameplay()
