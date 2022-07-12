from quicksort import quicksort
class Node:

    def __init__(self, category = None, data = [], next_node = None, prev_node = None):
        self.category = category
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_category(self):
        return self.category

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        self.next_node = value

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self,value):
        self.prev_node = value


class linked_list:

    def __init__(self):
        self.head_node = None

    def get_head_node(self):
        return self.head_node

    def add_head(self, value):
        if self.get_head_node():
            new_node = Node(value)
            new_node.set_next_node(self.get_head_node())
            self.head_node = new_node
        else:
            self.head_node = Node(value)

    def printing_list(self):
        lst = []
        current_node = self.get_head_node()
        while current_node:
            lst.append(current_node.get_category())
            current_node = current_node.get_next_node()
        print(lst)


class double_list:

    def __init__(self, head_node = None, tail_node = None):
        self.head_node = head_node
        self.tail_node = tail_node

    def get_head_node(self):
        return self.head_node

    def add_head(self,value):
        new_head = Node(value)
        current_node = self.head_node
        if current_node is not None:
            current_node.set_prev_node(new_head)
            new_head.set_next_node(current_node)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_tail(self, value):
        new_tail = Node(value)
        current_node = self.tail_node
        if current_node is not None:
            current_node.set_next_node(new_tail)
            new_tail.set_prev_node(current_node)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def go_through(self, value, node = None):
        if node is None:
            current_node = self.head_node
        else:
            current_node = node
        while current_node is not None:
            category = current_node.get_category()
            if category == value:
                return current_node #Zde bylo bylo možné vrátit uzel
            else:
                current_node = current_node.get_next_node()

    def sort_the_categories(self):
        current_node = self.head_node
        while current_node is not None:
            data_lst = current_node.get_data()
            quicksort(data_lst,0,len(data_lst)-1)
            current_node = current_node.get_next_node()