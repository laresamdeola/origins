from game_symbols import tears


#Create an intro and outro class.
def intro():
  origins_intro = """
    There was a time when all the gods and godess' were equal. None of them had any special 
    abilities. One fateful day, they approached Orunmila: a god regarded as the first son of
    Olodumare, creator of the heavens and the earth. The gods and goddess' lamented to Orunmila about their 
    predicament of being ordinary beings with no special powers.
    """

  origins_intro_continue = """
    They said that life had become boring and monotonous, they each wanted to be unique,
    they each wanted to be different. These are their Origins.
    """

  print(origins_intro)
  tears.print_game_symbol()
  print(origins_intro_continue)


#intro()
