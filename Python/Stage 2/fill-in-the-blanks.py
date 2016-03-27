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


def game_level():
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
    elif level_input == "medium":
        print "You've chosen medium!"
        answers = easy_answers
        statement = easy_statement
    elif level_input == "hard":
        print "You've chosen hard!"
        answers = easy_answers
        statement = easy_statement
    else:
        print "That's not an option!"
    return (statement, answers)

statement, answers = game_level()


def answer_check(answers, user_answer, blanks):
    for answer in blanks:
        if user_answer in answers:
            return answer
    return None


def play_game(statement, answers, blanks):
    print statement
    print "How many guesses would you like per problem?"
    attempts_input = raw_input("Please enter a positive integer number: ")
    replaced = []
    attemps = 0
    statement = statement.split()
    while attemps < attempts_input:
        for blank in blanks:
            user_answer = raw_input("What should be submitted for" +
                                    blank + "? ")
            the_answer = answer_check(answers, user_answer, blanks)
            if the_answer is not None:
                blank = blank.replace(user_answer, blank)
                replaced.append(blank)
                print replaced
            else:
                replaced.append(blank)
                attemps += attemps
        replaced = " ".join(replaced)
    return replaced

play_game(statement, answers, blanks)
