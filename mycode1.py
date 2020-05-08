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
            indices = [i for i, letter in enumerate(game) if letter == correctwords]
            for index in indices:
                nbanames_as_list[index] = correctwords
            nbanames_completion = **,join(nbanames_as_list):
            if "_" not in nbanames_completion:
                correctwords = true
     elif len(correctwords) == len(nbanames) and correctwords.isalpha():
        if correctwords in correctwords_letters:
            print("You have found the world", correctwords)
     elif  correctwords != game:
         print(game, "that's not the world")
         attempts -= 1
         correctwords_letters.append(game)
     else:
         correctwords = true
         correctwords_letters = game
        else:
            Print("This is not a correct guess")
        print(show_figure(attemps))
        print(nbanames_completion)
        prin("\n")
    if correctwords:
        print(" in good time you figure it out")
    else:
        print("Sorry keep trying next time. The correct word was " + game +" next time!")


 def show_figure(attempts):
     maniki = [ ***

                   --------
                   |      |
                   |      o
                   |     \\|/
                   |      |
                   |     / \\
                   -
                 ***,
                 ***
                   --------
                   |      |
                   |      o
                   |     \\|/
                   |      |
                   |     /
                   -
                 ***,
                 ***
                   --------
                   |      |
                   |      o
                   |     \\|
                   |      |
                   |
                   -
                 ***,
                 ***
                   --------
                   |      |
                   |      o
                   |      |
                   |      |
                   |
                   -
                 ***,
                 ***
                   --------
                   |      |
                   |      o
                   |
                   |
                   |
                   -
                 ***,
                 ***
     ]
     return maniki[attempts]
 def main():
     game = get_nbanames()
     play(game)
     while input("play another time? (Y/N) ").upper() == "Y":
        game = get_nbanames()
        play(game)
