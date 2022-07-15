import time
from dl_list import double_list
from csv_transformation import movies_attributes

movie_of_genres = ['Animation', 'Comedy', 'Family', 'Adventure',
                   'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                   'Thriller', 'Horror', 'History', 'Science Fiction',
                   'Mystery', 'War', 'Music', 'Documentary',
                   'Western']

categories_of_films_numbers = {movie_of_genres.index(v) + 1: v for v in movie_of_genres}


def show_categories():
    """Prints categories to the screen so that user could more easily pick. Time function is there
    for better user experience. """
    print("""There is plenty categories of movies. Many movies could be find in more categories.""")
    print(f"Possible categories and their type numbers are:\n")
    for number, cat in categories_of_films_numbers.items():
        time.sleep(0.3)
        print(cat, number)


def select_category():
    """ User picks the category, which he wants to explore. Fnc. returns name of category as string."""
    num = int(input("Select category by typing the its number.\n:"))
    while num > 18:
        print("You probably typed bigger number then possible category.")
        num = int(input("Select category by typing the its number.\n:"))
    movie_category = categories_of_films_numbers.get(num)
    return movie_category


def goodbye():
    print("I hope you enjoyed our recommender and we hope u will enjoy your selected movie.\n"
          "Bye.")


def decision_tree(dl_list):
    """ There user asked what he want to do."""
    entry = select_category()
    movies = dl_list.go_through(entry).get_data()
    while movies:
        for i, movie in enumerate(movies):
            print(movie[0], movie[1])
            if i == 2:
                break
        # Prints the top three movies of genre.
        answer = input(
            "For description of movie type 1 or 2 or 3.\nFor next movies in this category type n.\n"
            "For different category type d.\n"
            "For the quit type x.\n:")
        if answer == "x":
            return
        elif answer == "d":
            entry = select_category()
            movies = dl_list.go_through(entry).get_data()
        elif answer.isdigit():
            print(movies[int(answer)][0] + "\n", movies[int(answer)][-1])


def main():
    """The main part of the program."""
    welcome_file = open("../data/welcome.txt", "r", encoding = "utf-8")  # Introduction of the program to the user,
    print(welcome_file.read())
    welcome_file.close()
    double_list_categories = double_list()
    for movie_of_genre in movie_of_genres:
        double_list_categories.add_tail(movie_of_genre)
    # Create double list,where nodes are movie genres.
    movies_attributes(r"../data/movies_metadata.csv", double_list_categories)
    # Adds movies to their genres. Single movie could be in multiple genres.
    double_list_categories.sort_the_categories()
    # Sorting the movies from the best rated movie to the worst rated movie
    time.sleep(2)
    show_categories()
    decision_tree(double_list_categories)
    goodbye()


if __name__ == "__main__":
    main()
