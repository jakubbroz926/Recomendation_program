import time
from dl_list import Node,double_list,linked_list
from csv_transformation import movies_attributes

movie_of_genres = ['Animation', 'Comedy', 'Family', 'Adventure',
                   'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                   'Thriller', 'Horror', 'History', 'Science Fiction',
                   'Mystery', 'War', 'Music', 'Documentary',
                   'Western']
categories_of_films_numbers = {movie_of_genres.index(v) + 1: v for v in movie_of_genres}


def show_categories():
    print("""There is plenty categories of movies. Many movies could be find in more categories.""")
    print(f"Possible categories and their type numbers are:\n")
    for number, cat in categories_of_films_numbers.items():
        print(cat, number)


def select_category():
    num = int(input("Select category by typing the its number.\n:"))
    while num > 18:
        print("You probably typed bigger number then possible category.")
        num = int(input("Select category by typing the its number.\n:"))
    movie_category = categories_of_films_numbers.get(num)
    return movie_category


def goodbye():
    print("I hope you enjoyed our recommender and we hope u will enjoy your selected movie.\n"
          "Bye.")


def printing_categories(dl_list):
    return linked_list.printing_list(dl_list)


def description(lst,number):
    for i in lst[number]:
        print(i)
    return


def results(lst_of_movie_cat):
    while lst_of_movie_cat:
        print("The three best movies in this category are:")
        for i,movie in enumerate(lst_of_movie_cat):
            print(movie[0],movie[1])
            if i == 2:
                break
        answer = input("If you want see description of these movies, type 1 or 2 or 3. If you want to see another movies type n, "
                       "If you different movies of different category, type d."
                       "For the end type x.\n:")
        if answer.isdigit():
            description(lst_of_movie_cat,int(answer)-1)
        elif answer == "n":
            results(lst_of_movie_cat[3:])
        elif answer == "d":
            return True
        elif answer == "x":
            return False


def main():
    welcome_file = open("../data/welcome.txt", "r", encoding = "utf-8")
    print(welcome_file.read())
    welcome_file.close()
    double_list_categories = double_list()
    for movie_of_genre in movie_of_genres:
        double_list_categories.add_tail(movie_of_genre)
    movies_attributes(r"../data/movies_metadata.csv",double_list_categories)
    double_list_categories.sort_the_categories()
    time.sleep(2)
    show_categories()
    entry = select_category()
    while entry in categories_of_films_numbers.values():
        our_movies = double_list_categories.go_through(entry).get_data()
        if results(our_movies):
            entry = select_category()
            continue
        answer = input("Are you satisfied? ")
        if answer.lower() in ["y","yes"]:
            break
        else:
            entry = select_category()
    goodbye()


if __name__ == "__main__":
    main()