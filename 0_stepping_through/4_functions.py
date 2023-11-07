#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# --- function declaration ---


def be_more_excited(text: str) -> str:
    # a local variable
    excited_text = f"{text}!"
    # the function's return value is read from excited_text
    return excited_text


# --- function calls ---
# write 3+ more test cases

# try stepping over this function call
return_value_1 = be_more_excited("spaghetti")

# try stepping all the way through this function call
return_value_2 = be_more_excited("waffles")

# try stepping into this function call
#   then stepping out of it before the function returns
return_value_3 = be_more_excited("orange juice")


print(return_value_1)
print(return_value_2)
print(return_value_3)
