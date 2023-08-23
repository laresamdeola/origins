

class Amulets:
    def __init__(amulet, amulet_name, amulet_description, amulet_affinity, amulet_charm):
        amulet.amulet_name = amulet_name
        amulet.amulet_description = amulet_description
        amulet.amulet_affinity = amulet_affinity
        amulet.amulet_charm = amulet_charm

    def print_amulet_description(amulet):
        print(amulet.amulet_description)

    def print_amulet_name(amulet):
        print(amulet.amulet_name)

    def print_amulet_affinity(amulet):
        print(amulet.amulet_description)

    def print_amulet_charm(amulet):
        print(amulet.amulet_charm)


eye_of_the_storm = Amulets("Eye of the Storm", """
The Eye of the Storm gives you powers over water bodies. It was said that it was created when grains of sand during
ctreation fell from Obatala's satchel and there and then Aye had it's first rain
""", "water", "Power to control the water element")

cloud_chariot = Amulets("Cloud Chariot", """
A special gift from Orunmila, an Irunmole. The cloud chariot is made out of clouds and float in the air. It is believed
that it was created when Orunmila wanted to navigate the Universe.
""", "air", "It can be used to fly from one point to another. Helps with speed.")

black_peacock = Amulets("Black Peacock", """
A Peacock's feathers are always resplendent with various colors. This makes the all-black peacock extremely rare and 
powerful amulet. The wielder of such an Amulet would gaiun infinite wisdom and be able to surpass an riddles the Orisha
or Irunmole might present. 
""", "water", "Wisdom, Power to answer riddles and complete quests")

ebony_sword = Amulets("Ebony Sword", """
A sword made from the bark of the African Ebony Tree. The sword grants the wielder unlimited strength when travelling
through plains and mountains. It is somewhat rare and a natural possession of Erinle. 
""", "earth", "Stamina")


#ebony_sword.print_amulet_description()








