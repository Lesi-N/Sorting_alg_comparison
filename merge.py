def merge_sort(lst):
    """
    Sorts list using merge sort
    :param lst:
    return: number of comparisons
    """
    comp = 0
    if len(lst) > 1:

        middle = len(lst) // 2

        left = lst[:middle]
        right = lst[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            comp += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return comp
