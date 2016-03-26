# IPND Stage 2 Final Project

# This can be used as a study tool to help you remember important vocabulary!

sample = '''A ___1___ is created with the def keyword. You specify the inputs
a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by
default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as
string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda
functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# If you need help, you can sign up for a 1 on 1 coaching appointment:
# https://calendly.com/ipnd1-1/20min/


def Difficulty(user_level):
    """This function selects the difficulty chosen by user, and asks for the
    number of guesses the user wants for that difficulty
    """
    level_input = raw_input()
    if level_input == "easy":
        print "You've chosen easy!"
        print ""
        print "How many guesses would you like per problem?"
        guess_input = raw_input("Please enter a positive integer number: ")
        easy_mode(guess_input)

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
