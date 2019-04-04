# my_Media.py
import webbrowser

# Movie should be in uppercase accord. to Google Style Guide for Python


class Movie():
    """This class provides a way to store movie related information """

# for constant values Google suggests the use of all uppercase names:
    # const value:  VALID_RATINGS
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
