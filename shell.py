def shell_sort(lst):
    """
    Sorts list using shell sort
    :param lst:
    :return: number of comparisons
    """
    height = len(lst) // 2
    comp = 0
    while height > 0:
        for i in range(height, len(lst)):
            pos = lst[i]
            j = i
            cur_comp = 0
            while j >= height and lst[j - height] > pos:
                lst[j] = lst[j - height]
                j -= height
                cur_comp += 1
            lst[j] = pos
            comp += cur_comp
            if cur_comp == 0:
                comp += 1
        height = height // 2

    return comp
