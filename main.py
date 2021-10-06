"""
Main module for conducting the sorting algorithms comparison experiment
"""

from generate_list import generate_lists
from timing import *


def main():
    """
    Main function
    Generates lists and conducts all experiments
    :return:
    """
    types = ["Random list average", "Ascending list", "Descending list", "123 list average"]
    for p in range(7, 16):
        listoflists = generate_lists(p)
        print(f"\n\n2 ** {p}")
        for i in range(len(types)):
            times = run_tests(listoflists[i])
            print(f"{types[i]} shell sorting time: {times[0][0]}. Number of comparisons: {times[0][1]}")
            print(f"{types[i]} merge sorting time: {times[1][0]}. Number of comparisons: {times[1][1]}")
            print(f"{types[i]} selection sorting time: {times[2][0]}. Number of comparisons: {times[2][1]}")
            print(f"{types[i]} insertion sorting time: {times[3][0]}. Number of comparisons: {times[3][1]}\n")


main()
