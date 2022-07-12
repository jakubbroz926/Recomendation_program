import random


def quicksort(lst, start, end, function = True):
    if start >= end:
        return
    pivot_index = random.randrange(start, end)
    pivot_element = lst[pivot_index]
    lst[end], lst[pivot_index] = lst[pivot_index], lst[end]
    smaller_index = start
    if function:
        for i in range(start, end):
            if lst[i][1] > pivot_element[1]:  # from big to small number
                lst[i], lst[smaller_index] = lst[smaller_index], lst[i]
                smaller_index += 1
        lst[end], lst[smaller_index] = lst[smaller_index], lst[end]
        # print("{0} successfully partitioned".format(lst[start: end + 1]))
        quicksort(lst, start, smaller_index - 1)
        quicksort(lst, smaller_index + 1, end)
    else:
        for i in range(start, end):
            if lst[i][1] < pivot_element[1]:  # from small number to big
                lst[i], lst[smaller_index] = lst[smaller_index], lst[i]
                smaller_index += 1
        lst[end], lst[smaller_index] = lst[smaller_index], lst[end]
        # print("{0} successfully partitioned".format(lst[start: end + 1]))
        quicksort(lst, start, smaller_index - 1, False)
        quicksort(lst, smaller_index + 1, end, False)
