def insertion_sort(lst):
    """
    Sorts list using insertion sort
    :param lst: list of unsorted elements
    :return comp: number of comparisons
    """
    comp = 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        cur_comp = 0
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            cur_comp += 1
        comp += cur_comp
        if cur_comp == 0:
            comp += 1
        lst[j + 1] = key

    return comp
