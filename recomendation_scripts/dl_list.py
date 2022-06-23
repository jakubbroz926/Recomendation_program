from heaps import Heap


class Node:

    def __init__(self, category = None, data = Heap(), next_node = None):
        self.category = category
        self.data = data
        self.next_node = next_node

    def get_category(self):
        return self.category

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        self.next_node = value


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


