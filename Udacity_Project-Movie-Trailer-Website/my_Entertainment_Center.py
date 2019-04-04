# my_Entertainment_Center.py
import fresh_tomatoes
import my_Media

"""my_Entertainment_Center.py contains a list of movie objects.
This file calls the constructor my_Media.Movie() to instantiate
movie objects."""

signs = my_Media.Movie(
    "Signs",
    "A family surrounded by signs of an alien presence",
    "http://www.gstatic.com/tv/thumb/movieposters/30099/p30099_p_v8_ad.jpg",
    "https://youtu.be/mTgO18G5zjI")
rear_window = my_Media.Movie(
    "Rear Window",
    "A wheelchair-bound photographer spies on his neighbours",
    "https://images-na.ssl-images-amazon.com/images/M/" +
    "MV5BNGUxYWM3M2MtMGM3Mi00ZmRiLWE0NGQtZjE5ODI2OTJhNTU0XkEyXkFqcGde" +
    "QXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,683,1000_AL_.jpg",
    "https://youtu.be/MW0y7i2AyNU")
matrix = my_Media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature " +
    "of his reality and his role in the war against its controllers",
    "https://images-na.ssl-images-amazon.com/images/"
    "M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXk" +
    "EyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
    "https://youtu.be/vKQi3bBA1y8")
titanic = my_Media.Movie(
    "Titanic",
    "Romance set against the ill-fated maiden voyage of the Titanic ship",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5" +
    "My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_" +
    "SY1000_CR0,0,671,1000_AL_.jpg",
    "https://youtu.be/zCy5WQ9S4c0")
jurassic_park = my_Media.Movie(
    "Jurassic Park",
    "During a preview tour, a theme park suffers a major power breakdown "
    "that allows its cloned dinosaur exhibits to run amok",
    "https://images-na.ssl-images-amazon.com/images/" +
    "M/MV5BMjM2MDgxMDg0Nl5BMl5B" +
    "anBnXkFtZTgwNTM2OTM5NDE@._V1_.jpg",
    "https://youtu.be/lc0UehYemQA")
poltergeist = my_Media.Movie(
    "Poltergeist",
    "A family's home is haunted by a host of ghosts",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzliZmRlYTctYm" +
    "NkYS00NzE5LWI1OWQtMTRiODY5MDMwMTVkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_" +
    "SY1000_CR0,0,656,1000_AL_.jpg",
    "https://youtu.be/9eZgEKjYJqA")

"""movies array is created in order to pass as an argument of the
open_movies_page() function"""
movies = [signs, rear_window, matrix, titanic, jurassic_park, poltergeist]

"""The list of movies above is what the open_movies_page() function
needs as input in order to build the HTML file to display on my website."""
fresh_tomatoes.open_movies_page(movies)
