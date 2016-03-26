# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to
# complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs
# generator, you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use
# when testing your code.
# Your game should consist of 3 or more levels, so you should add your own
# paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs
a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by
default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as
string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda
functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working
# version of the project.

# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you
# open it it won't look like Python code! But you can run it just like a
# regular Python file to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs
# generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of
# NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

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


