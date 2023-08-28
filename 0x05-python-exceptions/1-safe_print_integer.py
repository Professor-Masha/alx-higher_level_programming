#!/usr/bin/python3


def safe_print_integer(value):
    """fun that Prints an integer with "{:d}".format

    Args:
        value (int): integer it prints.

    Returns:
        TypeError or ValueError
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

