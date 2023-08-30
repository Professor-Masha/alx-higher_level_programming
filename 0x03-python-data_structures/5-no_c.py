#!/usr/bin/python3
def no_c(my_string):
    newval = (val for val in my_string if val != 'c' and val != 'C')
    x = "".join(newval)
    return (x)
