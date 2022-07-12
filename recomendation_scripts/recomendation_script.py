import time
from dl_list import Node,double_list,linked_list
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
    movie_category = categories_of_films_numbers.get(num)
    return movie_category


def goodbye():
    print("I hope you enjoyed our recommender and we hope u will enjoy your selected movie.\n"
          "Bye.")


def printing_categories(dl_list):
    return linked_list.printing_list(dl_list)


def main():
    double_list_categories = double_list()
    for movie_of_genre in movie_of_genres:
        double_list_categories.add_tail(movie_of_genre)
    movies_attributes(r"../data/movies_metadata.csv",double_list_categories)
    #Zde je třeba všechny heapy sortovat dle ratingu filmu.
    #Projdou se všechny kategorie dl listu a seřadí se.
    double_list_categories.sort_the_categories()
    welcome_file = open("../data/welcome.txt", "r", encoding = "utf-8")
    print(welcome_file.read())
    welcome_file.close()
    # time.sleep(5) Add after finishing program
    show_categories()
    entry = select_category()
    while entry in categories_of_films_numbers.values():
        double_list_categories.go_through(entry).get_data().get_heap_value()
        #Zde se vrátí uživateli seznamu filmů z vybrané kategorie,
        #nesařazeno
        answer = input("Are you satisfied? ")
        if answer.lower() in ["y","yes"]:
            break
        else:
            entry = select_category()
    goodbye()


if __name__ == "__main__":
    main()