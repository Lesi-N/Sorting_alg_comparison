def selection_sort(lst):
    """
    Sorts list using selection sort
    :param lst:
    :return comp: number of comparisons
    """
    comp = 0
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[min] > lst[j]:
                min = j
            comp += 1
        lst[i], lst[min] = lst[min], lst[i]

    return comp
