#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """a fun that prints an integer with "{:d}".format()

    Args:
        value (int): Integer to print

    Returns:
        TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

