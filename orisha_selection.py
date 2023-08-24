import oshun_gameplay as oshun
import ogun_gameplay as ogun


def orisha_selection():
  player_element = ""
  with open("elements.txt", 'r') as elements_object:
    player_element = elements_object.readlines()
    #print(player_element[0])
    #oshun.oshun_gameplay()
  # there's a bug here
  if str(player_element[0]) == "water":
    print(player_element[0])
    oshun.oshun_gameplay()
  elif str(player_element[0]) == "earth":
    ogun.ogun_gameplay()
