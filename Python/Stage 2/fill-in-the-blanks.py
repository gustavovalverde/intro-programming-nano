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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def game_level():
    """This function selects the difficulty chosen by user, and asks for the
    number of guesses the user wants for that difficulty
    """
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    level_input = raw_input("What's your desired difficulty? " + "\n").lower()
    if level_input == "easy":
        print "You've chosen easy!" + "\n"
        answers = easy_answers
        statement = easy_statement
    elif level_input == "medium":
        print "You've chosen medium!" + "\n"
        answers = medium_answers
        statement = medium_statement
    elif level_input == "hard":
        print "You've chosen hard!" + "\n"
        answers = hard_answers
        statement = hard_statement
    else:
        print "That's not an option!" + "\n"
    return (statement, answers)

statement, answers = game_level()


def answer_check(answers, answer_index, user_answer):
    if user_answer in answers[answer_index]:
        return user_answer
    return None


def play_game(statement, answers, blanks):
    print "Now you must fill the blanks here:" + "\n" + statement
    print "How many guesses would you like per problem?"
    attempts_input = raw_input("Please enter a positive integer number: ")
    attempts = 0
    answer_index = 0
    for blank in blanks:
        if answer_index < len(answers):
            correct = False
            while not correct:
                if attempts < int(attempts_input):
                    user_answer = raw_input("\n" + "What should be submitted for" + blank + "? " + "\n")
                    good_answer = answer_check(answers, answer_index, user_answer)
                    if good_answer is not None:
                        statement = statement.replace(blank, good_answer)
                        print statement + "\n"
                        answer_index += 1
                        correct = True
                    else:
                        attempts += 1
                        if attempts == int(attempts_input):
                            break
                        print "\n" + "That's the wrong answer, please try again"
                        print "You have " + str(int(attempts_input) - attempts)
                        + " attempt(s) left" + "\n"
                        print statement + "\n"
                else:
                    print "Sorry, you ran out of attempts"
                    break
    if attempts < int(attempts_input):
        print "       ******* Great, you completed the Quizz *******" + "\n"

play_game(statement, answers, blanks)
