import webbrowser


class Video():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer


class Movies():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 youtube_trailer):
        Video.__init__()
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

class Series():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

