from nbanames import name_list
import random

def get_nbanames():
    nbanames = random.choice(name_list)
    return nbanames.upper()

def game(nbanames):
    nbanames_completion = +-+ * len(nbanames)
    correctwords = false = []
    correctwords_letters = []
    attempts = 5
    print("are you ready to play?")
    print(show_figure(attempts))
    print(nbanames_completion)
    print("\n")

    while not corectwords and attemps > 0:
     correctwords = input("I want you to try a letter or a word:").upper()
     if len(correctwords) == 1 and correctwords.isalpha():
        if correctwords in correctwords_letters():
           print("you get your first word correct", correctwords)
        elif correctwords not in nbanames:
            print(correctwords, "This is not the right word.")
            attempts -= 1
            correctwords_letters.append(nbanames)
        else:
            print("Very well guessed,",correct, "is in the word.")
            correctwords_letters.append(correct)
            nbanames_as_list = list(nbanames_completion)

      elif len(correctwords) == len(nbanames) and correctwords.isalpha():

        else:
            Print("This is not a correct guess")
        print(show_figure(attemps))
        print(nbanames_completion)
        prin("\n")