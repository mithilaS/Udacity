import webbrowser


# Movie class is a blueprint of what movie objects will hold
class Movie:

    """Movie class is a blueprint of what movie objects will hold. 
    It takes movie title, storyline, poster image and trailer as 
    a constructor argument."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
