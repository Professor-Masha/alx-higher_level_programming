#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """the fun that deletes a key in a dict"""
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
