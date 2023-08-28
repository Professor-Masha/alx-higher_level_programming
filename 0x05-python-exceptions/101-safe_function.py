#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """it executes a function safely

    Args:
        fct: Function to execute
        args: Arguments for fun

    Returns:
        If  error occurs - None
        Otherwise - The result of the call to fun
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
