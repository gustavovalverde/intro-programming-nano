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

print "Please select a game difficulty by typing it in!"
print "Possible choices include easy, medium, and hard."
level_input = raw_input("What's your desired difficulty? ")


def game_level(level_input):
    """This function selects the difficulty chosen by user, and asks for the
    number of guesses the user wants for that difficulty
    """
    if level_input == "easy":
        print "You've chosen easy!"
        answers = easy_answers
        statement = easy_statement
        return statement, answers
    elif level_input == "medium":
        print "You've chosen medium!"
        answers = easy_answers
        statement = easy_statement
        return statement, answers
    elif level_input == "hard":
        print "You've chosen hard!"
        answers = easy_answers
        statement = easy_statement
        return statement, answers
    else:
        print "That's not an option!"


def check_answer(user_response, answers):
    answer_set_index = 0
    blank_set_index = 0
    user_prompt = 1
    while answer_set_index < len(answers):
            if user_response == answers[answer_set_index]:
                return "Correct!"
            return "Incorrect.  Please try your answer again."


def answer_in_statement(blank, blanks):
    for answer in blanks:
        if answer in blank:
            return answer
    return None


def play_game(statement, answers, blanks):
    game_level(level_input)  # returns just the first function value
    print "How many guesses would you like per problem?"
    attempts_input = raw_input("Please enter a positive integer number: ")
    replaced = []
    attemps = 0
    statement = statement.split()
    while attemps < attempts_input:
        for blank in blanks:
            user_answer = raw_input("What should be submitted for" +
                                    blank + "? ")
            if replacement is not None:
                user_input = raw_input("What should be submitted for" +
                                       replacement + "? ")
                blank = blank.replace(replacement, user_input)
                replaced.append(blank)
            else:
                replaced.append(blank)
        replaced = " ".join(replaced)
    return replaced

play_game(easy_statement, easy_answers)
