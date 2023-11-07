#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Python implementation of a sort algorithm.
Best Case Scenario : O(n)
Worst Case Scenario : O(n^2) because native Python functions:min, max and remove are
already O(n)
"""


# !!! --- there is 1 mistake in this function --- !!!
def unknown_sort(collection):
    """Pure implementation of the fastest merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: a collection ordered by ascending

    Examples:
    >>> unknown_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> unknown_sort([])
    []

    >>> unknown_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    start, end = [], []
    while len(collection) > 1:
        max_one, min_one = min(collection), max(collection)
        start.append(min_one)
        end.append(max_one)
        collection.remove(min_one)
        collection.remove(max_one)
    end.reverse()
    return start + collection + end


# --- test the function ---

print(unknown_sort([]))

print(unknown_sort([1, 2, 3, 4, 5]))

print(unknown_sort([5, 4, 3, 2, 1]))

print(unknown_sort([0, -1, 1, -2, 2, -333, 333]))

print(unknown_sort([10203, 33243, 543, 213, 786, 12454]))


# adapted from TheAlgorithms/Python:
# https://github.com/TheAlgorithms/Python/blob/99f3a0e4c9b1a6d9ff5bba2adf65d90d55f2250a/sorts/unknown_sort.py
