class Heap:

    def __init__(self, heap = list()):
        self.heap = heap

    def get_heap_value(self):
        return self.heap

    def insert_into_heap(self,value):
        self.heap.append(value)

    def heap_sort(self):
        pass