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
    level_input = raw_input("What's your desired difficulty? ").lower()
    if level_input == "easy":
        print "You've chosen easy!"
        answers = easy_answers
        statement = easy_statement
    elif level_input == "medium":
        print "You've chosen medium!"
        answers = medium_answers
        statement = medium_statement
    elif level_input == "hard":
        print "You've chosen hard!"
        answers = hard_answers
        statement = hard_statement
    else:
        print "That's not an option!"
    return (statement, answers)

statement, answers = game_level()


def answer_check(answers, answer_index, user_answer):
    if user_answer in answers[answer_index]:
        return user_answer
    return None


def play_game(statement, answers, blanks):
    print "\n" + statement
    print "How many guesses would you like per problem?"
    attempts_input = raw_input("Please enter a positive integer number: ")
    attempts = 0
    statement = statement.split()
    answer_index = 0
    for blank in enumerate(statement):
        if attempts < int(attempts_input):
            if blank in blanks:
                user_answer = raw_input("\n" + "What should be submitted for" +
                                        blank + "? " + "\n")
                good_answer = answer_check(answers, answer_index, user_answer)
                if good_answer is not None:
#                    statement[s_index] = good_answer
                    statement = " ".join(statement)
                    statement = statement.replace(blank, good_answer)
                    print statement + "\n"
                    answer_index += 1
                else:
                    print "\n" + "That's the wrong answer, please try again"
                    attempts += 1
                    print "You have " + str(int(attempts_input) - attempts) + " attempt(s) left" + "\n"
                    replaced = " ".join(statement)
                    print replaced + "\n"
        else:
            print "Sorry, you ran out of attempts"
            break
    if attempts < int(attempts_input):
        print "*******This is your final statement******* \n" + replaced

play_game(statement, answers, blanks)
