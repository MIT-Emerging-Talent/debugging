#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("--- this function modifies the argument list ---")


def replace__side_effect(items, to_replace, replacer):
    for i in range(len(items)):
        if items[i] == to_replace:
            items[i] = replacer

    return items


list_1 = ["a", "b", "c", "b"]

# write 3+ more test cases
print(replace__side_effect(list_1, "a", 1))
print(replace__side_effect(list_1, "b", 2))
print(replace__side_effect(list_1, "c", 3))


print("--- this function does not modify the argument list ---")


def replace__pure(items, to_replace, replacer):
    items_copy = items.copy()

    for i in range(len(items_copy)):
        if items_copy[i] == to_replace:
            items_copy[i] = replacer

    return items_copy


list_2 = ["a", "b", "c", "b"]

# write 3+ more test cases
print(replace__pure(list_2, "a", 1))
print(replace__pure(list_2, "b", 2))
print(replace__pure(list_2, "c", 3))


# copy this program into PythonTutor for a better visual understanding:
#   https://pythontutor.com/visualize.html#mode=edit
