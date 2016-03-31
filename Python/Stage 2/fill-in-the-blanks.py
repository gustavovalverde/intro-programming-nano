# IPND Stage 2 Final Project

# This can be used as a study tool to help you remember important vocabulary!

easy_quiz = '''There are three distinct computer programming languages that are
used to create websites. The language that is used to define the structure of
a website is called ___1___.  ___1___ stands for hyper text markup language,
and is used to create the text, images, and other elements that appear in a
website. The style of a webpage is defined using a language called ___2___,
which stands for Cascading Style Sheets.  ___2___ is used to determine
characteristics such as font style, font size, and background color.'''

easy_answers = ["HTML", "CSS"]

easy_blanks = ["___1___", "___2___"]

medium_quiz = '''A ___1___ serves as a placeholder to which we can assign a
___2___. When a ___1___ is referenced in a program, it will always point to
the ___2___ that was assigned to that particular ___1___.  A value can be a
number, an equation, or a series of one of more characters which is called a
___3___.  The letter a is a ___3___ as is the sentence "I was a teenage
werewolf!" Two or more ___3___s can be joined together by a process known as
___4___.'''

medium_answers = ["variable", "value", "string", "concatenation"]

mediumBlanks = ["___1___", "___2___", "___3___", "___4___"]

hard_quiz = '''A ___1___ is created with the def keyword. You specify the
inputs a ___1___ takes by adding ___2___ separated by commas between the
parentheses. ___1___s by default return ___3___ if you don't specify the value
to return. ___2___ can be standard data types such as string, number,
dictionary, tuple, and ___4___ or can be more complicated such as objects and
lambda functions.'''

hard_answers = ["function", "arguments", "None", "set"]

hard_blanks = ["___1___", "___2___", "___3___", "___4___"]

quizzes = [easy_quiz, medium_quiz, hard_quiz]  # list for quizzes strings
answers = [easy_answers, medium_answers, hard_answers]  # list for answers lists
blanks = [easy_blanks, mediumBlanks, hard_blanks]  # list for blanks lists

# lists for each level with its quiz, answers and blanks
easy = [quizzes[0], answers[0], blanks[0]]
medium = [quizzes[1], answers[1], blanks[1]]
hard = [quizzes[2], answers[2], blanks[2]]

# Dictionary refering a string to a variable for later use in game_level().
# This is for user input validation.
levels = {'easy': easy, 'medium': medium, 'hard': hard}


def game_level():
    """This function selects the difficulty chosen by user, compares it with
    the 'levels' dictionary and returns all the variables needed for a level.
    """
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    choice = raw_input("What's your desired difficulty? ").lower()
    while choice not in levels:
        print "\n" + "That's not an option!" + "\n"
        choice = raw_input("What's your desired difficulty? ").lower()
    chosen_level = levels[choice]
    print "\n" + "Quiz for this difficulty:" + "\n" + chosen_level[0]
    return chosen_level


def game_attempts(chosen_level):
    """It also asks the user for the number of guesses the user wants for the
    chosen diffilcuty, for later use in play_game.
    """
    print "\n" + "How many guesses would you like per problem?"
    user_attempts = raw_input("Please enter a positive integer number: ")
    while user_attempts.isdigit() is not True:
        print "\n" + "Sorry, the program needs an integer" + "\n"
        user_attempts = raw_input("Please enter a positive integer number: ")
    return chosen_level, int(user_attempts)


def play_game(chosen_level):
    """This receives a tuple with chosen_level and user_attempts in it.
    It takes the first value to iterate over and validate each 'answer' with
    the respective 'blank' using a for loop and a zip. If the user answer is
    correct it keeps asking for the next 'blank', if its not then it loops in
    a 'while' until the right answer its given if attempts still remains"""
    # Answers_lists -->  chosen_level[0][1]
    # Blanks list -->  chosen_level[0][2]
    quiz_string = chosen_level[0][0]
    user_attempts = chosen_level[1]
    attempts = 0
    for answer, blank in zip(chosen_level[0][1], chosen_level[0][2]):
            user_answer = raw_input("\n" + "What should be submitted for" +
                                    blank + "? " + "\n")
            while user_answer != answer and attempts <= user_attempts:
                attempts += 1
                if attempts == user_attempts:
                    return "\n" + "Sorry, you ran out of attempts" + "\n"
                print "\n" + "That's not the answer, try again" + "\n" + "You have " + str((user_attempts - attempts)) + " attempt(s)"
                "left" + "\n" + quiz_string + "\n"
                user_answer = raw_input("\n" + "What should be submitted for" +
                                        blank + "? " + "\n")

            quiz_string = quiz_string.replace(blank, user_answer)
            print "\n" + "Good, thats correct" + "\n \n" + quiz_string + "\n"
    if attempts < user_attempts:
        return "       ******* Great, you completed the Quizz *******" + "\n"

print play_game(game_attempts(game_level()))
