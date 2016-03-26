# IPND Stage 2 Final Project

# This can be used as a study tool to help you remember important vocabulary!

easy_statement = '''A ___1___ is created with the def keyword. You specify the
inputs a ___1___ takes by adding ___2___ separated by commas between the
parentheses. ___1___s by default return ___3___ if you don't specify the value
to return. ___2___ can be standard data types such as string, number,
dictionary, tuple, and ___4___ or can be more complicated such as objects and
lambda functions.'''

easy_answers = ["Function", "arguments", "None", "dictionaries"]

# If you need help, you can sign up for a 1 on 1 coaching appointment:
# https://calendly.com/ipnd1-1/20min/


def Difficulty(user_level):
    """This function selects the difficulty chosen by user, and asks for the
    number of guesses the user wants for that difficulty
    """
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    level_input = raw_input("What's your desired difficulty? ")
    if level_input == "easy":
        print "You've chosen easy!"
        print ""
        print "How many guesses would you like per problem?"
        guess_input = raw_input("Please enter a positive integer number: ")
        return easy_statement, easy_answers, guess_input

    elif level_input == "medium":
        print "You've chosen medium!"
        print ""
        print "How many guesses would you like per problem?"
        guess_input = raw_input("Please enter a positive integer number: ")
        medium_mode(guess_input)

    elif level_input == "hard":
        print "You've chosen hard!"
        print ""
        print "How many guesses would you like per problem?"
        guess_input = raw_input("Please enter a positive integer number: ")
        hard_mode(guess_input)
    else:
        print "That's not an option!"
        continue

def easy_mode(guess_input):
    guesses = 0
    while guesses < guess_input:



def word_in_pos(word, sample):
    for pos in answers:
        if pos in word:
            return pos
    return None

# A player is prompted to replace words in
# ml_string, which appear in easy_string, medium_string or hard_string with
# their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement is not None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced
