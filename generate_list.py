"""
Module that generates different types of lists for the experiments:
1. random lists
2. and ascending and a descending list
3. lists with a random amount of repeated elements
The last function generates the necessary amount of each of these for a given size
"""

import random


def generate_random(power):
    """
    Generates 5 random lists of a certain size
    :param power: power of 2
    :return: generated lists
    """
    randlist = []
    for i in range(5):
        experiment = []
        for j in range(2 ** power):
            experiment.append(random.randint(0, 10000))
        randlist.append(experiment)
    return randlist


def generate123(power):
    """
    Generates 3 lists that contain a random number of ones, twos and threes
    :param power: power of 2
    :return: generated lists
    """
    lst123 = []
    for i in range(3):
        experiment = []
        for j in range(2 ** power):
            experiment.append(random.randint(1, 3))
        lst123.append(experiment)
    return lst123


def generate_ascending_descending(power):
    """
    Generates lists that have ascending and descending elements
    :param power: power of 2
    :return: generated lists
    """
    ascending = []
    for i in range(2 ** power):
        ascending.append(i)
    descending = ascending[::-1]
    return ascending, descending


def generate_lists(power):
    """
    Calls the above functions and generates 4 types of lists for a given size
    :param power: power of 2
    :return: list of lists
    """
    rand = generate_random(power)
    sortedlists = generate_ascending_descending(power)
    ascending = sortedlists[0]
    descending = sortedlists[1]
    list123 = generate123(power)

    return [rand, [ascending], [descending], list123]

