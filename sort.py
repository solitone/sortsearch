import time

n_compars, n_swaps = 0, 0

def exchangesort(list: list) -> (int, int):
    """
    The simplest sorting algorithm.
    :param list: unsorted list.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    n_compars, n_swaps = 0, 0
    length = len(list)
    for i in range (0, length-1):
        for j in range(i+1, length):
            n_compars += 1
            if list[i] > list[j]:
                n_swaps += 1
                list[i], list[j] = list[j], list[i]
                yield (n_compars, n_swaps)
    #print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))

def selectionsort(list: list) -> (int, int):
    """
    Similar to exchange sort, but only one swap per list element.
    :param list: unsorted list.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    n_compars, n_swaps = 0, 0
    length = len(list)
    for i in range (0, length-1):
        smallest = i # index of the smallest value found
        for j in range(i+1, length):
            n_compars += 1
            if list[smallest] > list[j]:
                smallest = j
                swapNeeded = True
            yield (n_compars, n_swaps)
        n_swaps += 1
        list[i], list[smallest] = list[smallest], list[i]
        yield (n_compars, n_swaps)
    #print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))

def bubblesort(list: list) -> (int, int):
    """
    Bigger elements gradually bubble up to the end of the list.
    :param list: unsorted list.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    n_compars, n_swaps = 0, 0
    length = len(list)
    while(True):
        swapped = False
        for i in range (0, length-1):
            n_compars += 1
            if list[i] > list[i+1]:
                n_swaps += 1
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True
            yield (n_compars, n_swaps)
        if swapped == False:
            break
    #print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))

def insertionsort(list: list) -> (int, int):
    """
    ...
    :param list: unsorted list.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    n_compars, n_swaps = 0, 0
    length = len(list)
    for i in range(1, length):
        n_compars += 1
        # Python does not need a second variable for indexing:
        while i > 0 and list[i-1] > list[i]:
            n_swaps += 1
            list[i-1], list[i] = list[i], list[i-1]
            i -= 1
            yield (n_compars, n_swaps)
            n_compars += 1

def quicksort(list: list, lo: int, hi: int) -> (int, int):
    """
    Divide & impera, with pivot. Using a variation of Hoare’s Partition Scheme.
    :param list: unsorted list.
    :param lo: left side of the list to consider.
    :param hi: right side of the list to consider.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    global n_compars
    global n_swaps
    if lo < hi: # do nothing if out of range
        # Partition logic:
        pi = lo # choose left most element as pivot
        i, j = lo, hi
        while True:
            # Find 1st element from the right smaller than pivot (or equal to):
            while j > i and list[j] > list[pi]:
                n_compars += 1
                j += -1
                yield (n_compars, n_swaps)
            # Find 1st element from the left greater than pivot:
            while i < j and list[i] <= list[pi]:
                n_compars += 1
                i += 1
                yield (n_compars, n_swaps)
            if i == j: # When indexes meet, we're done:
                # put pivot in the right place by swapping it with i-element
                # and exit loop
                n_swaps += 1
                list[pi], list[i] = list[i], list[pi]
                pi = i
                yield (n_compars, n_swaps)
                break
            n_swaps += 1
            list[i], list[j] = list[j], list[i]
            yield (n_compars, n_swaps)

        yield from quicksort(list, lo, pi - 1)
        yield from quicksort(list, pi + 1, hi)
    #print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))

def mergesort(list: list, lo: int, hi: int) -> (int, int):
    """
    Another divide & impera approach, different from quick sort.
    :param list: unsorted list.
    :param lo: left side of the list to consider.
    :param hi: right side of the list to consider.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    global n_compars, n_swaps
    length = hi - lo + 1
    if length > 1:
        mid = lo + length // 2 - 1 # integer division
        yield from mergesort(list, lo, mid) # sort 1st half
        yield from mergesort(list, mid + 1, hi) # sort 2nd half
        yield from merge(list, lo, mid, hi) # merge 2 halves

def merge(list: list, lo: int, mid: int, hi: int) -> (int, int):
    """
    Utility function for mergesort.
    :param list: unique list consisting of two ordered lists; at the end of execution, it will contain the merged ordered list.
    :param lo: left side of the first list.
    :param mid: right side of the first list; mid + 1 is left side of second list.
    :param hi: right side of the second list.
    :return: tuple (n_compars, n_swaps), counting number of comparisons and number of swaps occurred.
    """
    global n_compars, n_swaps
    sorted = [] # temporary list for sorted merged list
    i, j = lo, mid + 1
    while i <= mid and j <= hi:
        n_compars += 1
        if list[i] <= list[j]:
            sorted.append(list[i])
            i += 1
        else:
            sorted.append(list[j])
            j += 1
        yield (n_compars, n_swaps)
    if i > mid: # 1st list finished
        sorted.extend(list[j:]) # add remaining elements of 2nd list
    else: # 2nd list finished
        sorted.extend(list[i:mid + 1]) # add remaining elements of 1nd list

    for idx, val in enumerate(sorted):
        n_swaps += 1
        list[lo + idx] = val
    yield (n_compars, n_swaps)


# def mergesort(list: list) -> list:
#     """
#     Test
#     """
#     print("list: ", end = '')
#     print(list)
#     length = len(list)
#     if length <= 1:
#         return list
#     else:
#         mid = length // 2  # integer division
#         left = mergesort(list[:mid]) # sort 1st half
#         right = mergesort(list[mid:]) # sort 2nd half
#         sorted = merge(left, right) # merge 2 halves
#         print("sorted: ", end = '')
#         print(sorted)
#         return sorted
