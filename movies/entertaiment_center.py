#!/usr/bin/python

"""
Here is the list of movies which gets feed into fresh_tomatoes.py file.
"""

import fresh_tomatoes
import media


anchor_man = media.Movie("AnchorMan",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MzYwMzk5Ml5BMl5BanBnXkFtZTcwOTI4NzUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://youtu.be/Ip6GolC7Mk0")

old_school = media.Movie("Old School",
"https://images-na.ssl-images-amazon.com/images/M/MV5BYzI4NDIzMDgtNGNkZi00MTI2LWJhYzgtYzM5NThhMTQ0OGIzXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://youtu.be/VqtymOtKr48")

captain_america = media.Movie("Captain America",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
"https://youtu.be/W4DlMggBPvc")


iron_man = media.Movie("Iron Man",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG",
"https://youtu.be/7H0yo-lDuk0")

guardians_of_galaxy = media.Movie("Guardians of Galaxy",
"https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",
"https://youtu.be/d96cjJhvlMA")

doctor_strange = media.Movie("Doctor Strange",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY317_CR1,0,214,317_AL_.jpg",
"https://youtu.be/HSzx-zryEgM")

movies = [anchor_man, old_school, captain_america, iron_man, guardians_of_galaxy, doctor_strange]

fresh_tomatoes.open_movies_page(movies)
