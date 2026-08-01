# Movie Collection Management System

class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    #movie category
    def category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"


class Cinema:
    def __init__(self):
        self.movies = []

    # Add movie
    def add_movie(self, movie):
        self.movies.append(movie)

    # Display movie details
    def display_movies(self):
        print("\n----- Movie Collection -----")
        for movie in self.movies:
            print("Movie Name :", movie.movie_name)
            print("Rating     :", movie.rating)
            print("Ticket Price: ₹", movie.ticket_price)
            print("Category   :", movie.category())
            print("----------------------------")


# Main Program
cinema = Cinema()

n = int(input("Enter number of movies: "))

for i in range(n):
    print(f"\nEnter details of Movie {i+1}")
    name = input("Movie Name: ")
    rating = float(input("Rating (out of 10): "))
    price = float(input("Ticket Price: "))
    
    movie = Movie(name, rating, price)
    cinema.add_movie(movie)

cinema.display_movies()
