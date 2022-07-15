import random
import sys

sys.setrecursionlimit(1200)


def quicksort(lst, start, end):
    """Recursion was increased so the program would go without break
by reaching the recursion limit.
I used this quicksort function earlier in different program at much larger sample( around million),
so any advice how improve is welcome"""
    if start >= end:
        return
    pivot_index = random.randrange(start, end)
    pivot_element = lst[pivot_index]
    lst[end], lst[pivot_index] = lst[pivot_index], lst[end]
    smaller_index = start
    for i in range(start, end):
        if lst[i][1] > pivot_element[1]:  # from big to small number
            lst[i], lst[smaller_index] = lst[smaller_index], lst[i]
            smaller_index += 1
    lst[end], lst[smaller_index] = lst[smaller_index], lst[end]
    quicksort(lst, start, smaller_index - 1)
    quicksort(lst, smaller_index + 1, end)