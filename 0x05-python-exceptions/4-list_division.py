#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """a fun that divides two lists elements

    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): No of elements to divide

    Returns:
        List of length list_length containing all the division
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
