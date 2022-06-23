import time
from dl_list import Node,double_list
from heaps import Heap
from csv_transformation import movies_attributes

movie_of_genres = ['Animation', 'Comedy', 'Family', 'Adventure',
                   'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                   'Thriller', 'Horror', 'History', 'Science Fiction',
                   'Mystery', 'War', 'Music', 'Documentary',
                   'Western']
categories_of_films_numbers = {movie_of_genres.index(v) + 1: v for v in movie_of_genres}


def show_categories():
    print("""There is plenty categories of movies.Many movies could be find in more categories.""")
    print(f"Possible categories and their type numbers are:\n")
    for number, cat in categories_of_films_numbers.items():
        # time.sleep(0.5) Add after finishing program
        print(cat, number)


def select_category():
    num = int(input("Select category by typing the its number.\n:"))
    return num


def goodbye():
    print("I hope you enjoyed our recommender and we hope u will enjoy your selected movie.\n"
          "Bye.")


def basic_menu():
    # vytvoření dvojitého listu z kategorií
    dlinked_list_categories = [Node(movie_genre) for movie_genre in movie_of_genres]
    welcome_file = open("../data/welcome.txt", "r", encoding = "utf-8")
    print(welcome_file.read())
    welcome_file.close()
    # time.sleep(5) Add after finishing program
    show_categories()
    entry = select_category()
    while entry in categories_of_films_numbers.keys():
        print(dlinked_list_categories[entry-1].data.heap)
        # attributes_of_movies = movies_attributes(r"../data/movies_metadata.csv")
        # vypsání tří filmů
        answer = input("Are you satisfied? ")
        if answer.lower() in ["y","yes"]:
            break
    goodbye()


basic_menu()