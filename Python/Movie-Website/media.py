class Video():
    """This Class (in the context of this project) refers to all """
    def __init__(self, video_title, video_storyline, video_poster,
                 video_trailer):
        self.title = video_title
        self.storyline = video_storyline
        self.poster = video_poster
        self.trailer = video_trailer


class Movies(Video):
    def __init__(self, video_title, video_storyline, video_poster,
                 video_trailer, movie_box):
        Video.__init__(self, video_title, video_storyline, video_poster,
                       video_trailer)
        self.boxoffice = movie_box


class TVShow(Video):
    def __init__(self, video_title, video_storyline, video_poster,
                 video_trailer, show_seasons, show_episodes):
        Video.__init__(self, video_title, video_storyline, video_poster,
                       video_trailer)
        self.seasons = show_seasons
        self.episodes = show_episodes
