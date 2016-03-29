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

medium_answers = ["function", "arguments", "None", "set"]

medium_statement = '''A ___1___ is created with the def keyword. You specify the
inputs a ___1___ takes by adding ___2___ separated by commas between the
parentheses. ___1___s by default return ___3___ if you don't specify the value
to return. ___2___ can be standard data types such as string, number,
dictionary, tuple, and ___4___ or can be more complicated such as objects and
lambda functions.'''

hard_answers = ["function", "arguments", "None", "set"]

hard_statement = '''A ___1___ is created with the def keyword. You specify the
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
    level_input = raw_input(bcolors.OKBLUE + "What's your desired difficulty? " + bcolors.ENDC).lower()
    if level_input == "easy":
        print bcolors.OKGREEN + "You've chosen easy!" + bcolors.ENDC + "\n"
        answers = easy_answers
        statement = easy_statement
    elif level_input == "medium":
        print bcolors.OKGREEN + "You've chosen medium!" + bcolors.ENDC + "\n"
        answers = medium_answers
        statement = medium_statement
    elif level_input == "hard":
        print bcolors.OKGREEN + "You've chosen hard!" + bcolors.ENDC + "\n"
        answers = hard_answers
        statement = hard_statement
    else:
        print bcolors.FAIL + "That's not an option!" + bcolors.ENDC + "\n"
    return (statement, answers)

statement, answers = game_level()


def answer_check(answers, answer_index, user_answer):
    if user_answer in answers[answer_index]:
        return user_answer
    return None


def play_game(statement, answers, blanks):
    print bcolors.OKBLUE + "Now you must fill the blanks here:" + "\n" + bcolors.ENDC + statement + "\n"
    print bcolors.OKBLUE + "How many guesses would you like per problem?" + bcolors.ENDC
    attempts_input = raw_input(bcolors.OKBLUE + "Please enter a positive integer number: " + bcolors.ENDC)
    attempts = 0
    answer_index = 0
    for blank in blanks:
        if answer_index < len(answers):
            correct = False
            while not correct:
                if attempts < int(attempts_input):
                    user_answer = raw_input(bcolors.OKBLUE + "\n" + "What should be submitted for" + blank + "? " + bcolors.ENDC + "\n")
                    good_answer = answer_check(answers, answer_index, user_answer)
                    if good_answer is not None:
                        statement = statement.replace(blank, good_answer)
                        print bcolors.OKGREEN + "Good, Thats the answer" + bcolors.ENDC + "\n"
                        print statement + "\n"
                        answer_index += 1
                        correct = True
                    else:
                        attempts += 1
                        if attempts == int(attempts_input):
                            break
                        print "\n" + bcolors.FAIL + "That's the wrong answer, please try again" + bcolors.ENDC
                        print bcolors.WARNING + "You have " + str(int(attempts_input) - attempts) + " attempt(s) left" + bcolors.ENDC + "\n"
                        print statement + "\n"
                else:
                    print bcolors.FAIL + "Sorry, you ran out of attempts" + bcolors.ENDC
                    break
    if attempts < int(attempts_input):
        print bcolors.GREEN + "       ******* Great, you completed the Quizz *******" + "\n" + bcolors.ENDC

play_game(statement, answers, blanks)
