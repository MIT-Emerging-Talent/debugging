#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci(num: int) -> int:
    """calculates the n'th term in the Fibonacci sequence"""

    if num < 2:
        return num

    minus_1 = fibonacci(num - 1)
    minus_2 = fibonacci(num - 2)
    result = minus_2 + minus_1

    return result


# write 3+ more test cases
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(6))
print(fibonacci(12))
print(fibonacci(24))
