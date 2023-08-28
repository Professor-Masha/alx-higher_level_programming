#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """a fun that Prints the first x elements integers of a list.

    Args:
        my_list (list): List to print element.
        x (int): No of elements of my list to print

    Returns:
        The No of elements to be printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
