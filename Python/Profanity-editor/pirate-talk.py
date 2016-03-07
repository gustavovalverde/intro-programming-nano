import urllib


def read_text():
    my_file = open("/home/vagrant/intro-programming-nano/Python/Profanity-"
                   "editor/movie_quotes.txt")
    contents_of_file = my_file.read()
    print contents_of_file
    my_file.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" +
                                text_to_check)
    output = connection.read()
    print output
    connection.close()

read_text()
