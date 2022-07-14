import csv
import json

selected = ["genres", "overview", "title", "vote_average"]


def select_genres(genres_attr):
    """This function parses a genres of movies from string into list data type."""
    genres = genres_attr.replace("'", "\"")
    js = json.loads(genres)
    genres_of_movie = [line["name"] for line in js]
    return genres_of_movie


def movies_attributes(file,double_list):
    """ Read the original file and prepare info about movies to be inserted into categories.(Double linked list)."""
    with open(file, mode = "r", newline = "", encoding = "utf-8")as csv_reader:
        movies = csv.DictReader(csv_reader)
        for row in movies:
            movie_info = []
            for info in selected:
                if info == "genres":
                    movie_info.append(select_genres(row[info]))
                else:
                    movie_info.append(
                        float(row[info]) if info == "vote_average" and isinstance(row[info], str) else row[info])
            movie_info[-1], movie_info[1] = movie_info[1], movie_info[-1]
            movie_info[0], movie_info[2] = movie_info[2], movie_info[0]
            for genre in movie_info[2]:
                node_of_double_list = double_list.go_through(genre)
                try:
                    node_of_double_list.add_data(movie_info)
                except AttributeError:
                    continue
