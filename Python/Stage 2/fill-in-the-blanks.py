# IPND Stage 2 Final Project

# This can be used as a study tool to help you remember important vocabulary!
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

easy_answers = ["function", "arguments", "None", "set"]

easy_statement = '''A ___1___ is created with the def keyword. You specify the
inputs a ___1___ takes by adding ___2___ separated by commas between the
parentheses. ___1___s by default return ___3___ if you don't specify the value
to return. ___2___ can be standard data types such as string, number,
dictionary, tuple, and ___4___ or can be more complicated such as objects and
lambda functions.'''


def Difficulty():
    """This function selects the difficulty chosen by user, and asks for the
    number of guesses the user wants for that difficulty
    """
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    level_input = raw_input("What's your desired difficulty? ")
    if level_input == "easy":
        print "You've chosen easy!"
        answers = easy_answers
        statement = easy_statement
        print ""
        print "How many guesses would you like per problem?"
        guess_input = raw_input("Please enter a positive integer number: ")
        return statement, answers, guess_input

    elif level_input == "medium":
        print "You've chosen medium!"
        answers = easy_answers
        statement = easy_statement
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

# def easy_mode(guess_input):
#     guesses = 0
#    while guesses < guess_input:


def answer_in_statement(blank, blanks):
    for answer in blanks:
        if answer in blank:
            return answer
    return None


# A player is prompted to replace words in
# statement, which appear in easy_string, medium_string or hard_string with
# their own words.
def play_game(guess_input, statement, answers):
    replaced = []
    guesses = 0
    statement = statement.split()
    while guesses < guess_input:
        for blank in statement:
            replacement = answer_in_statement(blank, answers)
            if replacement is not None:
                user_input = raw_input("What should be submitted for" +
                                       replacement + "? ")
                blank = blank.replace(replacement, user_input)
                replaced.append(blank)
            else:
                replaced.append(blank)
        replaced = " ".join(replaced)
    return replaced

print Difficulty()[0]  # returns just the first function value
