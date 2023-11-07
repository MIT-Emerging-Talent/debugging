#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" lists are stored by reference

this means that two variables will actually point to the same list in memory
so when you update one variable, the other variable is also updated!

to avoid this, you must store a copy of the list in a new variable

copy this program into PythonTutor for a better visual understanding:

https://pythontutor.com/visualize.html#mode=edit

"""


numbers = [1, 2, 3, 4]

numbers.append(5)

other_numbers = numbers

other_numbers.append(6)

# !! what is stored in numbers right now?

numbers_copy = numbers.copy()

numbers_copy.append(7)

# !! what is stored in numbers_copy?

# !! what is stored in numbers?

# !! what is stored in other_numbers?
