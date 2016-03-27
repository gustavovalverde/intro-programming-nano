#IPND Stage 2 Final Project
#By Andy Torchia
#Here are the blank spaceholders
blanks = ["__1__", "__2__", "__3__", "__4__"]
#Quiz 1
quiz1 = """We hold these __1__ to be self-evident, that all men are created __2__,
that they are endowed by their Creator with certain unalienable __3__, that among
these are life, liberty and the pursuit of __4__."""
#Quiz 2
quiz2 = """We the People of the United States, in Order to form a more __1__ Union,
establish Justice, insure domestic Tranquility, provide for the common __2__,
promote the general Welfare, and secure the blessings of __3__ to ourselves and
our Posterity, do ordain and establish this __4__ for the United States of America."""
#Quiz 3
quiz3 = """Four score and __1__ years ago our fathers brought forth on this continent
a new nation, __2__ in liberty, and __3__ to the proposition that all men are
__4__ equal."""
#Here are the answers for the quizes. The program will check the user's
#responses against these.
quiz1_answers = ["truths", "equal", "rights", "happiness"]
quiz2_answers = ["perfect", "defense", "liberty", "constitution"]
quiz3_answers = ["seven", "conceived", "dedicated", "created"]
#This function will prompt the user to select one of the quizes.
#Then the program will tell the user which quiz was selected
#and then print the quiz.
quiz_select = raw_input("Please select a quiz. Enter easy, medium, or hard: ")
def choose_quiz(quiz_select):
    if quiz_select == "easy":
        return quiz1
    if quiz_select == "medium":
        return quiz2
    if quiz_select == "hard":
        return quiz3
print "You have selected the " + quiz_select + " quiz."
print
print choose_quiz(quiz_select) + "\n"
#This variable sets the number of guesses the user gets
attempts = raw_input("How many attempts to fill in the blanks would you like? ")
print
#This function will select the correct answer set based on which quiz the user chose.
def answer_set(quiz_select):
    if choose_quiz(quiz_select) == quiz1:
        return quiz1_answers
    if choose_quiz(quiz_select) == quiz2:
        return quiz2_answers
    if choose_quiz(quiz_select) == quiz3:
        return quiz3_answers
#This function checks the user's answer against the answer set
def answer_check(user_answer, correct_answer, answer_index):
     if user_answer == correct_answer[answer_index]:
         return "correct"
     return "wrong"
# This is the function for the game itself
def fill_in_the_blanks_quiz():
    attempt_index = 1  #Tracks the number of attempts to answer
    quiz = choose_quiz(quiz_select)  #This is the quiz that is being used. Blanks will be replaced with correct answers as the game progresses.
    correct_answer = answer_set(quiz_select)  #Stores the answer set for the quiz in use
    blank_index = 0  #This keeps track of which blank the user is trying to fill in

    answer_index = 0  #This keeps track of which answer we want to check
    while blank_index < len(blanks):
    if attempt_index > int(attempts):
        print  "Sorry you have run out of chances. Game over."
        blank_index = len(blanks) #this will end the while loop
    else:
        user_answer = raw_input("What should be substituted in for " + blanks[blank_index] + "?")
        if answer_check(user_answer, correct_answer, answer_index) == "wrong":
            attempt_index = attempt_index + 1
            print "Your answer was not correct!" + "\n"
            if attempt_index == int(attempts):
                print "This is your last chance to get this one." + "\n"
        if answer_check(user_answer, correct_answer, answer_index) == "correct":
            print "Correct!" + "\n"
            quiz = quiz.replace(blanks[blank_index], user_answer) #this replaces the blank with the correct answer
            print quiz + "\n" #this prints the quiz with the blank replaced
            blank_index += 1
            answer_index += 1
            attempt_index = 1 #reset to 1 after a correct answer
            if blank_index == len(blanks):
                print "You Won!!! Game Over."
fill_in_the_blanks_quiz()
