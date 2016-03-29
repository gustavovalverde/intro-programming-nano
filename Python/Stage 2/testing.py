blanks=["___1___", "___2___", "___3___", "___4___"]



# Here is the first quiz!
quiz1= '''There are three distinct computer programming languages that are used to create websites.
The language that is used to define the structure of a website is called ___1___.  ___1___ stands for ___2___, and is used to create the
text, images, and other elements that appear in a website.  The style of a webpage is defined using a language called ___3___, which stands for
___4___.  ___3___ is used to determine characteristics such as font style, font size, and background color.'''

# Here is the second quiz:
quiz2='''A ___1___ serves as a placeholder to which we can assign a ___2___.  When a ___1___ is referenced in a program, it will always point
to the ___2___ that was assigned to that particular ___1___.  A value can be a number, an equation, or a series of one of more characters
which is called a ___3___.  The letter a is a ___3___ as is the sentence "I was a teenage werewolf!"
Two or more ___3___s can be joined together by a process known as ___4___.'''

# And the third quiz; I am using the sample paragraph above:
quiz3 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.  '''

# Now here are the answer sets for all three quizzes.  These answer sets will be referenced when the users respond to the answer prompts
answers_quiz1=["HTML", "hyper text markup language", "CSS", "Cascading Style Sheets"]
answers_quiz2=["variable", "value", "string", "concatenation"]
answers_quiz3=["function", "parameters", "none", "set"]








# Now, our first function.  This function will prompt the user to select one of three levels of difficulty: easy, medium, and difficult, and return
# as output the appropriate level quiz and answer set.
user_prompt=raw_input("Please select a level:easy, medium, or difficult")
def select_level(user_prompt):


    if user_prompt=="easy":
        return quiz1

    if user_prompt=="medium":
        return quiz2

    if user_prompt=="difficult":
        return quiz3



print select_level(user_prompt)


# This next function checks the user response with the answer list and returns whether the response is correct or incorrect.
def check_answer(user_response, answers, answer_set_index):

     if user_response==answers[answer_set_index]:
         return "Correct"
     return "Incorrect"




# And now for the game itself.. First, a quiz variable defines which quiz is being played as determined by the
# response that the player entered in the select_level function. Depending on which quiz is in play, the appropriate answer set is then stored in a variable named answers.
# This answer set will be be referenced when checking the user response in the check_answer function.

def fill_in_the_blanks():
    quiz=select_level(user_prompt)
    if quiz==quiz1:
        answers=answers_quiz1
    if quiz==quiz2:
        answers=answers_quiz2
    if quiz==quiz3:
        answers=answers_quiz3
    blanks_set_index=0# sets the blanks index to 0
    answer_set_index=0# when the check_answer function is called, the first answer in the appropriate answer set will be referenced
    while blanks_set_index<len(blanks):
        while answer_set_index<len(answers):
            user_response=raw_input("Please fill in the correct answer for " + blanks[blanks_set_index])# the user is prompted to fill in the first blank
            while check_answer(user_response, answers, answer_set_index)=="Incorrect": # if the answer checks out as "Incorrect:, the user is prompted to try again.
                user_response=raw_input("Incorrect response. Please fill in the correct answer for " + blanks[blanks_set_index])
            if check_answer(user_response, answers, answer_set_index)=="Correct":# if the user answers correctly,a message indicating the answer is correct will appear, and the quiz will
                print "Congratulations, your answer is correct!"# be re-printed with the blank replaced by the correct response
                quiz=quiz.replace(blanks[blanks_set_index], user_response)
                print quiz
                blanks_set_index +=1 #adds one to the blank-set-index.  The function loops back and the user is prompted to fill in the next blank.
                answer_set_index+=1 # advances the answer set index so the next answer is checked when the check answer function is called

    print "Congratulations! You have sucessfully completed this quiz!"


print fill_in_the_blanks()
