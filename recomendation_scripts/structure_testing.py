from dl_list import Node, linked_list,double_list
from heaps import Heap

movie_of_genres = ['Animation', 'Comedy', 'Family', 'Adventure',
                   'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                   'Thriller', 'Horror', 'History', 'Science Fiction',
                   'Mystery', 'War', 'Music', 'Documentary',
                   'Western']

b = double_list()
for i in movie_of_genres:
    b.add_tail(i)
b.update_heaps()