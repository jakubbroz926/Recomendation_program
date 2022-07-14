from dl_list import Node, linked_list,double_list

movie_of_genres = ['Animation', 'Comedy', 'Family', 'Adventure',
                   'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                   'Thriller', 'Horror', 'History', 'Science Fiction',
                   'Mystery', 'War', 'Music', 'Documentary',
                   'Western']

x = double_list()
for cat in movie_of_genres:
    x.add_tail(cat)
node = x.go_through("Fantasy")
node.add_data("Random movie")
print(node.category,node.data)