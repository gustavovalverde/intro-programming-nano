print "Welcome to my first quiz with user input"
print "Lets get cracking straight away"
print
import time
#Setting the difficulty level based on raw user input
difficulty_level = raw_input("Which difficulty level would you like? Type EASY, MEDIUM or HARD to continue?  ")
if difficulty_level.upper() == "EASY":
    time.sleep(1)
    print "Here it goes..."
    print
    time.sleep(1)
    print "Here's your text. Should be an easy one. Just fill in the blanks for _Word_ 1-3."
    print
    print
    print "Python is a _Word1_ language that provides constructs intended to enable clear programs on both small and large scale. Python implementation was started in December _Word2_ by Guido von Rossum. The most simple function in Python is _Word3_ and normally used at the beginning to tell Python to write 'Hello World' on the screen."
    print
    # A list of replacement words to be passed in to the play game function.
    parts_of_speech1  = ["_Word1_", "_Word2_", "_Word3_"]
    # The following are some test strings to pass in to the play_game function.
    easy_text = "Python is a _Word1_ language that provides constructs intended to enable clear programs on both small and large scale. Python implementation was started in December _Word2_ by Guido von Rossum. The most simple function in Python is _Word3_ and normally used at the beginning to tell Python to write 'Hello World' on the screen."
    # Checks if a word in parts_of_speech is a substring of the word passed in.
    def word_in_pos_easy(word, parts_of_speech1):
        for pos in parts_of_speech1:
            if pos in word:
                return pos
        return None
    # Plays a full game of mad_libs. A player is prompted to replace words in the easy text,
    # which appear in parts_of_speech with their own words.
    def easy_game(easy_text, parts_of_speech1):
        replaced = []
        easy_text = easy_text.split()
        for word in easy_text:
            replacement = word_in_pos_easy(word, parts_of_speech1)
            if replacement != None:
                user_input = raw_input("Type in: " + replacement + " ")
                word = word.replace(replacement, user_input)
                replaced.append(word)
            else:
                replaced.append(word)
        replaced = " ".join(replaced)
        print
        time.sleep(1)
        print "Ok, lets see your results. Does it make sense?"
        print
        time.sleep(1)
        return replaced
        print
        time.sleep(1)
    print easy_game(easy_text, parts_of_speech1)
# Difficulty Level Medium
if difficulty_level.upper() == "MEDIUM":
    time.sleep(1)
    print "Good choice. Lets see how much you know about Python"
    print
    time.sleep(1)
    print "Here's your text. It's a tricky one that requires some more knowledge about Python. Just fill in the blanks for _Word_ 1-3."
    print
    print
    print "A string object is _Word1_, i.e. it cannot be modified after it has been created. An important concept in Python and other programming languages is _Word2_. You use them to store a value. To assign a value to a Variable you use the _Word3_ operator. A more versatile data type in Python is _Word4_. They contain items separated by commas and within square brackets. To some extent they are similar to arrays in C."
    print
    # A list of replacement words to be passed in to the play game function.
    parts_of_speech2  = ["_Word1_", "_Word2_", "_Word3_", "_Word4_"]
    # The following are some test strings to pass in to the play_game function.
medium_text = "A string object is _Word1_, i.e. it cannot be modified after it has been created. An important concept in Python and other programming languages is _Word2_. You use them to store a value. To assign a value to a Variable you use the _Word3_ operator. A more versatile data type in Python is _Word4_. They contain items separated by commas and within square brackets. To some extent they are similar to arrays in C."
# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos_medium(word, parts_of_speech2):
    for pos in parts_of_speech2:
        if pos in word:
            return pos
    return None
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def medium_game(medium_text, parts_of_speech2):
    replaced = []
    medium_text = medium_text.split()
    for word in medium_text:
        replacement = word_in_pos_medium(word, parts_of_speech2)
        if replacement != None:
            user_input = raw_input("Type in: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print
    time.sleep(1)
    print "OK, lets see your results. Does it make sense?"
    print
    time.sleep(1)
    return replaced
    print
    time.sleep(1)
print medium_game(medium_text, parts_of_speech2)
# Difficulty Level Hard
if difficulty_level.upper() == "HARD":
    time.sleep(1)
    print "Bold move! Here we go. Check out this text. It's a tough one"
    print
    time.sleep(1)
    print "Here's your text. This one requires quite some Python knowledge"
    print
    print
    print "Similar to other programming languages, Python has flow controls. The most known statement is the _Word1_ statement. It can be combined with an else statement and helps to process a logic based on a specific condition. For more repetitive processing one needs to use loops. _Word2_ loops execute a sequence of statements multiple times and abbreviates the code that manages the loop variable._Word3_ loops repeat a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body."
    print
    # A list of replacement words to be passed in to the play game function.
    parts_of_speech3  = ["_Word1_", "_Word2_", "_Word3_"]
    # The following are some test strings to pass in to the play_game function.
    hard_text = "Similar to other programming languages, Python has flow controls. The most known statement is the _Word1_ statement. It can be combined with an else statement and helps to process a logic based on a specific condition. For more repetitive processing one needs to use loops. _Word2_ loops execute a sequence of statements multiple times and abbreviates the code that manages the loop variable. _Word3_ loops repeat a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body."
    # Checks if a word in parts_of_speech is a substring of the word passed in.
    def word_in_pos_hard(word, parts_of_speech3):
        for pos in parts_of_speech3:
            if pos in word:
                return pos
        return None
    # Plays a full game of mad_libs. A player is prompted to replace words in the hard text,
    # which appear in parts_of_speech with their own words.
    def hard_game(hard_text, parts_of_speech3):
        replaced = []
        hard_text = hard_text.split()
        for word in hard_text:
            replacement = word_in_pos_hard(word, parts_of_speech3)
            if replacement != None:
                user_input = raw_input("Type in: " + replacement + " ")
                word = word.replace(replacement, user_input)
                replaced.append(word)
            else:
                replaced.append(word)
        replaced = " ".join(replaced)
        print
        time.sleep(1)
        print "OK, lets see your results. Does it make sense?"
        print
        time.sleep(1)
        return replaced
        print
    print hard_game(hard_text, parts_of_speech3)
