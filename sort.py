import time

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
    print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))

def selectionsort(list) -> (int, int):
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
    print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))

def bubblesort(list) -> (int, int):
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
    print("Comparisons: {}, swaps: {}".format(n_compars, n_swaps))
