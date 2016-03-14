
import fresh_tomatoes  # This module builds the webpage.
import media  # This one defines the classes and functions used here.

# Define each Video object information. Movie or TV Show.
gatsby = media.Movies("Great Gatsby",
                      "The mysterious past and lavish lifestyle of Jay"
                      " Gatsby.",
                      "http://resizing.flixster.com/CwM_QL1Uyohgxpx1Tj-"
                      "P4CNT4YM=/800x1200/dkpu1ddg7pbsk.cloudfront.net/"
                      "movie/11/17/25/11172588_ori.jpg",
                      "https://youtu.be/OULhlaX6JY4",
                      str(105000000))

man_on_fire = media.Movies("Man on Fire",
                           "A former assassin swears vengeance on those who"
                           " committed an unspeakable act against a family",
                           "http://www.gstatic.com/tv/thumb/movieposters/"
                           "34417/p34417_p_v8_aa.jpg",
                           "https://youtu.be/rb-ZEBBKolc",
                           str(70000000))

inception = media.Movies("Inception",
                         "A thief who steals corporate secrets through use of"
                         " the dream-sharing technology.",
                         "http://www.filmofilia.com/wp-content/uploads/2010/"
                         "04/Inception_poster.jpg",
                         "https://youtu.be/66TuSJo4dZM",
                         str(160000000))

batman_begins = media.Movies("Batman Begins",
                             "Batman begins his war on crime to free the"
                             " crime-ridden Gotham City from corruption.",
                             "http://vignette2.wikia.nocookie.net/batman/"
                             "images/9/94/Batman_Begins_poster4.jpg",
                             "https://youtu.be/neY2xVmOfUM",
                             str(150000000))

the_avengers = media.Movies("The Avengers",
                            "Earth's mightiest heroes must come together and"
                            " learn to fight as a team.",
                            "https://upload.wikimedia.org/wikipedia/en/f/f9/"
                            "TheAvengers2012Poster.jpg",
                            "https://youtu.be/rD8lWtcgeyg",
                            str(220000000))

forrest_gump = media.Movies("Forrest Gump",
                            "Forrest Gump, while not intelligent, has"
                            " been present at many historic moments.",
                            "https://upload.wikimedia.org/wikipedia/en/6/67/"
                            "Forrest_Gump_poster.jpg",
                            "https://youtu.be/Wc8GlIT1ZzU",
                            str(55000000))

gladiator = media.Movies("Gladiator",
                         "When a Roman general is betrayed he comes to"
                         " Rome as a gladiator to seek revenge.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8d/"
                         "Gladiator_ver1.jpg",
                         "https://youtu.be/ol67qo3WhJk",
                         str(103000000))

braveheart = media.Movies("Brave Heart",
                          "When his secret bride is executed, William Wallace"
                          " begins a revolt against King Edward I of England",
                          "https://upload.wikimedia.org/wikipedia/en/5/55/"
                          "Braveheart_imp.jpg",
                          "https://youtu.be/wj0I8xVTV18",
                          str(72000000))

game_thrones = media.TVShow("Game of Thrones",
                            "Batman begins his war on crime to free the"
                            "crime-ridden Gotham City from corruption.",
                            "http://vignette2.wikia.nocookie.net/batman/"
                            "images/9/94/Batman_Begins_poster4.jpg",
                            "https://youtu.be/BpJYNVhGf1s",
                            str(6),
                            str(60))

the_arrow = media.TVShow("The Arrow",
                         "Batman begins his war on crime to free the"
                         "crime-ridden Gotham City from corruption.",
                         "http://thenationalstudent.com/admin/images/"
                         "tinymce/1497/wp_arrow_leather_ipad_768_1024.jpeg",
                         "https://youtu.be/neY2xVmOfUM",
                         str(4),
                         str(92))

fuller_house = media.TVShow("Fuller House",
                            "Batman begins his war on crime to free the"
                            "crime-ridden Gotham City from corruption.",
                            "http://episodetube.com/wp-content/uploads/2016/"
                            "02/fullherhousesc.jpg",
                            "https://youtu.be/neY2xVmOfUM",
                            str(2),
                            str(14))

# Movies takes a list of items to display in the webpage.
# This is built by fresh_tomatoes.py
movies = [gatsby, man_on_fire, inception, batman_begins, the_avengers,
          forrest_gump, gladiator, braveheart, game_thrones, the_arrow,
          fuller_house]

# This is where the "magic" happens.
# Here we call the function that makes the hard work.
# It takes the 'movies' list as input and creates an HTML file with this info.
# See open_movies_page() function inside of'fresh_tomatoes.py' for more...
fresh_tomatoes.open_movies_page(movies)
