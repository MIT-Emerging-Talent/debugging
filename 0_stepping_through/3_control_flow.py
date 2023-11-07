#!/usr/bin/env python3
# -*- coding: utf-8 -*-

text = input("input some text for later: ")

sort_text = input('type "Y" to sort the text: ')

if sort_text == "Y":
    chars = []
    for char in text:
        chars.append(char)
    sorted_chars = sorted(chars)
    sorted_text = "".join(sorted_chars)
    print(sorted_text)
else:
    print(text)
