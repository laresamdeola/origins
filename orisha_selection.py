import oshun_gameplay as oshun
import ogun_gameplay as ogun


def orisha_selection():
  element = ""
  with open("elements.txt", 'r') as elements_object:
    player_element = elements_object.readlines()
    print(player_element)
    element = str(player_element[0]).strip()
  if element == "water":
    oshun.oshun_gameplay()
  elif element == "earth":
    ogun.ogun_gameplay()
