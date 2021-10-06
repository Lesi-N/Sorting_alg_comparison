"""
Module for timing the execution of each sorting algorithm
and running all algorithms through the same lists
"""
from insertion import insertion_sort
from merge import merge_sort
from selection import selection_sort
from shell import shell_sort
import time
import copy


def time_shell(lst):
    """
    Times execution of shell sort
    :param lst:
    :return sorttime, comp: time taken to sort, num of comparisons
    """
    start = time.time()
    comp = shell_sort(lst)
    end = time.time()
    sorttime = end - start
    return sorttime, comp


def time_merge(lst):
    """
    Times execution of merge sort
    :param lst:
    :return sorttime, comp: time taken to sort, num of comparisons
    """
    start = time.time()
    comp = merge_sort(lst)
    end = time.time()
    sorttime = end - start
    return sorttime, comp


def time_selection(lst):
    """
    Times execution of selection sort
    :param lst:
    :return sorttime, comp: time taken to sort, num of comparisons
    """
    start = time.time()
    comp = selection_sort(lst)
    end = time.time()
    sorttime = end - start
    return sorttime, comp


def time_insertion(lst):
    """
    Times execution of insertion sort
    :param lst:
    :return sorttime, comp: time taken to sort, num of comparisons
    """
    start = time.time()
    comp = insertion_sort(lst)
    end = time.time()
    sorttime = end - start
    return sorttime, comp


def run_tests(lst):
    """
    Runs all sorting algorithms for the same lists of one type
    (for example for 5 random lists, the results of which are averaged)
    Iterates through list of lists
    :param lst: list of lists
    :return: list of lists (one for each algorithm),
    which contain time of execution and number of comparisons
    """
    results = [[[], []] for _ in range(4)]

    for i in range(len(lst)):
        a = copy.deepcopy(lst[i])
        b = copy.deepcopy(lst[i])
        c = copy.deepcopy(lst[i])

        shell = time_shell(lst[i])
        results[0][0].append(shell[0])
        results[0][1].append(shell[1])

        merge = time_merge(a)
        results[1][0].append(merge[0])
        results[1][1].append(merge[1])

        selection = time_selection(b)
        results[2][0].append(selection[0])
        results[2][1].append(selection[1])

        insertion = time_insertion(c)
        results[3][0].append(insertion[0])
        results[3][1].append(insertion[1])

    for i in range(len(results)):
        results[i] = tuple([sum(results[i][0]) / len(results[i][0]),
                            round(sum(results[i][1]) / len(results[i][1]))])

    return results
