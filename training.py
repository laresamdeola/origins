import orisha
import ewi
import random
import origins_keys as keys
import random
import origins


ewis = (f"{ewi.blc_ewi.ewi_passage}", f"{ewi.roo_ewi.ewi_passage}", f"{ewi.sn_ewi.ewi_passage}",
              f"{ewi.s_ewi.ewi_passage}", f"{ewi.cld_ewi.ewi_passage}", f"{ewi.golden_ewi.ewi_passage}",
              f"{ewi.dgf_ewi.ewi_passage}")

random_ewi = random.choice(ewis)


def training_ground_one():
    print(orisha.ogun.origin_story)
    print("You have come here because you're interested in fulfilling your destiny. Rere O!")
    ewi_train_question = input("Are you ready to train yourself on ewi?").lower()

    def training_ground():
        ewi_answers = ["black cobra", "giraffe", "golden tree frog", "salt", "kangaroo", "clouds",
                       "ostrich", "snake", "dragonfly"]
        if ewi_train_question == "yes" or ewi_train_question == "y":
            print(random_ewi)
            trainer_answer = input("What is your answer? ")
            if trainer_answer in ewi_answers:
                print("O kare!")
                training_ground()
            elif trainer_answer == "h":
                print("Sorry! no hints or help in the training ground!")
                training_ground()
            elif trainer_answer == "q" or trainer_answer == "quit" or trainer_answer == "x":
                keys.exit.key_action()
            elif trainer_answer not in ewi_answers:
                print("Keep trying")
                training_ground()
        elif ewi_train_question == "no" or ewi_train_question == "n":
            origins.origins()

    training_ground()


#training_ground_one()