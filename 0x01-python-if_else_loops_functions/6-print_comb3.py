#!/usr/bin/python3
"""Prints all possible combination of two digits
   the No are separated by , and the space
   01 and 10 are considered the same combn of the 2 digits 0 and 1
   Prints only the smallest combination of 2 digits.
"""
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 8 and y == 9:
            print("{}{}".format(x, y))
        else:
            print("{}{}".format(x, y), end=", ")
