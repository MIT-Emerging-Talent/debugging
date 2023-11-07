#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This is a pure Python implementation of the bogosort algorithm,
also known as permutation sort, stupid sort, slowsort, shotgun sort, or monkey sort.
Bogosort generates random permutations until it guesses the correct one.

More info on: https://en.wikipedia.org/wiki/Bogosort

For doctests run following command:
python -m doctest -v bogo_sort.py
or
python3 -m doctest -v bogo_sort.py
For manual testing run:
python bogo_sort.py
"""

import random


# !!! --- there is 1 mistake in this function --- !!!
def bogo_sort(collection):
    """Pure implementation of the bogosort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bogo_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bogo_sort([])
    []
    >>> bogo_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def is_sorted(collection):
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while is_sorted(collection):
        random.shuffle(collection)
    return collection


# --- test the function ---

print(bogo_sort([]))

print(bogo_sort([1, 2, 3, 4, 5]))

print(bogo_sort([5, 4, 3, 2, 1]))

print(bogo_sort([0, -1, 1, -2, 2, -333, 333]))

print(bogo_sort([10203, 33243, 543, 213, 786, 12454]))


# adapted from TheAlgorithms/Python:
# https://github.com/TheAlgorithms/Python/blob/99f3a0e4c9b1a6d9ff5bba2adf65d90d55f2250a/sorts/bogo_sort.py
