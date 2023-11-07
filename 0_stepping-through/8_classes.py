#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value


class Circle:
    radius = PositiveNumber()

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)


# --- --- --- --- --- --- --- --- --- --- --- --- ---


circle = Circle(100)
print(circle.radius)  # 100

circle.radius = 500
print(circle.radius)  # 500

try:
    circle.radius = 0
except ValueError as err:
    print(err)


# adapted from https://realpython.com/python-classes/
