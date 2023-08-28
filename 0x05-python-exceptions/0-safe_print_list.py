#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """fun that Prints x elememts in a list

    Args:
        my_list (list):List that prints elements
        x (int): Number of elements of my_list to print

    Returns:
        The number of elements that is printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
