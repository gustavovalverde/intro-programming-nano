import urllib


def read_text():
    my_file = open("/home/vagrant/intro-programming-nano/Python/Profanity-"
                   "editor/movie_quotes.txt")
    contents_of_file = my_file.read()
    print contents_of_file
    my_file.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" +
                                text_to_check)
    output = connection.read()

    if "true" in output:
        print "Profanity Alert!"

    if "false" in output:
        print "Everything's good"

    else:
        "Something went wrong, the file might "

    connection.close()

read_text()
