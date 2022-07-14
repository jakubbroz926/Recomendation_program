import random


def quicksort(lst, start, end):
    if start >= end:
        return
    pivot_index = random.randrange(start, end)
    pivot_element = lst[pivot_index]
    lst[end], lst[pivot_index] = lst[pivot_index], lst[end]
    smaller_index = start
    for i in range(start, end):
        try:
            if lst[i][1] > pivot_element[1]:  # from big to small number
                lst[i], lst[smaller_index] = lst[smaller_index], lst[i]
        except TypeError:
            pass
        smaller_index += 1
        lst[end], lst[smaller_index] = lst[smaller_index], lst[end]
        quicksort(lst, start, smaller_index - 1)
        quicksort(lst, smaller_index + 1, end)