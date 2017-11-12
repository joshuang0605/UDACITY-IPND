import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
         Behavior: Initialize the movie instance.
         Input: Arguments.
         Output: Values, if there is not, return none.
         """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Behavior: Open youtube trailer box when poster image being clicked
        Input: youtube trailer
        Output: Youtube trailer box being played in browser window.
        """
        webbrowser.open(self.trailer_youtube_url)
