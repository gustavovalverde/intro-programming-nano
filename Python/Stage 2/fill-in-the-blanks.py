# IPND Stage 2 Final Project

# This can be used as a study tool to help you remember important vocabulary!
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

easy_statement = '''There are three distinct computer programming languages that are used to create websites. The language that is used to define the structure of a website is called ___1___.  ___1___ stands for ___2___, and is used to create the text, images, and other elements that appear in a website.  The style of a webpage is defined using a language called ___3___, which stands for ___4___.  ___3___ is used to determine characteristics such as font style, font size, and background color.'''

easy_answers = ["HTML", "hyper text markup language", "CSS",
                "Cascading Style Sheets"]

medium_statement = '''A ___1___ serves as a placeholder to which we can assign a ___2___.  When a ___1___ is referenced in a program, it will always point to the ___2___ that was assigned to that particular ___1___.  A value can be a number, an equation, or a series of one of more characters which is called a ___3___.  The letter a is a ___3___ as is the sentence "I was a teenage werewolf!" Two or more ___3___s can be joined together by a process known as ___4___.'''

medium_answers = ["variable", "value", "string", "concatenation"]

hard_statement = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

hard_answers = ["function", "arguments", "None", "set"]


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

def play_game(statement, answers, blanks):
    print bcolors.OKBLUE + "Now you must fill the blanks here:" + "\n" + bcolors.ENDC + statement + "\n" + "\n" + bcolors.OKBLUE + "How many guesses would you like per problem?" + bcolors.ENDC
    attempts_input = raw_input(bcolors.OKBLUE + "Please enter a positive integer number: " + bcolors.ENDC)
    attempts = 0
    answer_index = 0
    for blank in blanks:
        if answer_index < len(answers):
            correct = False
            while not correct:
                if attempts < int(attempts_input):
                    answer_check(answers, answer_index, statement, blank, attempts, correct, attempts_input)
                else:
                    print bcolors.FAIL + "Sorry, you ran out of attempts" + bcolors.ENDC
                    break
    if attempts < int(attempts_input):
        print bcolors.GREEN + "       ******* Great, you completed the Quizz *******" + "\n" + bcolors.ENDC

def answer_check(answers, answer_index, statement, blank, attempts, correct, attempts_input):
    user_answer = raw_input(bcolors.OKBLUE + "\n" + "What should be submitted for" + blank + "? " + bcolors.ENDC + "\n")
    if user_answer in answers[answer_index]:
        statement = statement.replace(blank, user_answer)
        print "\n" + bcolors.OKGREEN + "Good, Thats the answer" + bcolors.ENDC + "\n" + statement + "\n"
        answer_index += 1
        correct = True
        return user_answer, correct, answer_index
    else:
        attempts += 1
        print "\n" + bcolors.FAIL + "That's not the answer, try again" + bcolors.ENDC + "\n" + bcolors.WARNING + "You have " + str(int(attempts_input) - attempts) + " attempt(s) left" + bcolors.ENDC + "\n" + statement + "\n"
        return attempts

play_game(statement, answers, blanks)
