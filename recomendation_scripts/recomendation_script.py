import time

from csv_transformation import movies_attributes

movie_of_genres = ['Animation', 'Comedy', 'Family', 'Adventure',
                       'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                       'Thriller', 'Horror', 'History', 'Science Fiction',
                       'Mystery', 'War', 'Music', 'Documentary',
                       'Western']
categories_of_films_numbers = {movie_of_genres.index(v) + 1:v for v in movie_of_genres}
def show_categories():
        print("""There is plenty categories of movies.
        Many movies could be find in more categories.""")
        print(f"Possible categories and their type numbers are:\n")
        for number, cat in categories_of_films_numbers.items():
                time.sleep(0.5)
                print(cat,number)
def select_category():
        num = int(input("Select category by typing the its number."))
        return num
def basic_menu():
    # vytvoření dvojitého listu z kategorií
    dlinked_list_categories = [1,2,3,45,6]
    welcome_file = open("../data/welcome.txt", "r", encoding = "utf-8")
    print(welcome_file.read())
    welcome_file.close()
    time.sleep(5)
    show_categories()
    entry = select_category()
    while entry in categories_of_films_numbers.keys():
        dlinked_list_categories(categories_of_films_numbers[entry])
        #vypsání tří filmů
        answer = input("Are you satisfied? ")



    attributes_of_movies = movies_attributes(r"../data/movies_metadata.csv")


basic_menu()