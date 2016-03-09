import fresh_tomatoes
import media


gatsby = media.Movie("Great Gatsby",
                     "The mysterious past and lavish lifestyle of Jay"
                     "Gatsby.",
                     "http://resizing.flixster.com/CwM_QL1Uyohgxpx1Tj-"
                     "P4CNT4YM=/800x1200/dkpu1ddg7pbsk.cloudfront.net/"
                     "movie/11/17/25/11172588_ori.jpg",
                     "https://youtu.be/OULhlaX6JY4")

man_on_fire = media.Movie("Man on Fire",
                       "A former assassin swears vengeance on those who committed an unspeakable act against the family he was hired to protect.",
                       "http://www.gstatic.com/tv/thumb/movieposters/34417/p34417_p_v8_aa.jpg",
                       "https://youtu.be/rb-ZEBBKolc")

inception = media.Movie("Inception",
                        "A thief who steals corporate secrets through use of the dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                        "http://www.filmofilia.com/wp-content/uploads/2010/04/Inception_poster.jpg",
                        "https://youtu.be/66TuSJo4dZM")

batman_begins = media.Movie("Batman Begins",
                            "Batman begins his war on crime to free the crime-ridden Gotham City from corruption that the Scarecrow and the League of Shadows have cast upon it.",
                             "http://vignette2.wikia.nocookie.net/batman/images/9/94/Batman_Begins_poster4.jpg",
                             "https://youtu.be/neY2xVmOfUM")

the_avengers = media.Movie

movies = [toy_story, avatar_story, man_fire, inception, batman_begins]
fresh_tomatoes.open_movies_page(movies)
