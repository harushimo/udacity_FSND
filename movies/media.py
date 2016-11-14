"""
This is movie class which we will instiate in our entertainment.py file
"""

import webbrowser

class Movie():

	"""
	Movie object initialization contains

	movie_title - contains the title of the movie
	poster_image - contains the url of the image for the movie
	youtube_trailer - contains the youtube link for each movie

	"""

	def __init__(self, movie_title, poster_image, youtube_trailer):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer
