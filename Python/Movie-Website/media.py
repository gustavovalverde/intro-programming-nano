#
# Class definition file for my Movie Website.
# Primarily for use in 'entertainment_movies.py'
#


class Video():
    '''This Class (in the context of this project) refers to all video
       types, like Movies, TVShows and VideoClips (if any).
       '''
    def __init__(self, video_title, video_storyline, video_poster,
                 video_trailer):
        # Made from a basic Video (Movie or TV Show) information.
        self.title = video_title
        self.storyline = video_storyline
        self.poster = video_poster
        self.trailer = video_trailer


class Movies(Video):
    '''Defines a type of video (Movies), which it's only difference is
       the budgeted Box Office.
       '''
    def __init__(self, video_title, video_storyline, video_poster,
                 video_trailer, movie_box):
        # It inherits most of it's instance variables from Video() class.
        Video.__init__(self, video_title, video_storyline, video_poster,
                       video_trailer)
        self.boxoffice = movie_box  # The only instance variable defined here.


class TVShow(Video):
    '''Defines TV Shows (or series), which its a different type of video,
       which its compose of episodes and seasons.
       '''
    def __init__(self, video_title, video_storyline, video_poster,
                 video_trailer, show_seasons, show_episodes):
        Video.__init__(self, video_title, video_storyline, video_poster,
                       video_trailer)
        self.seasons = show_seasons
        self.episodes = show_episodes
