#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 2
b = 1

assert a == 2, "a's initial value is 2"
assert b == 1, "b's initial value is 1"


temp = a
a = b
b = temp

assert a == 1, "a's final value is 1"
assert b == 2, "b's final value is 2"
