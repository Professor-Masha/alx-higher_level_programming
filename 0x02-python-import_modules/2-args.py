#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    val = len(sys.argv) - 1
    if val == 0:
        print("0 arguments.")
    elif val == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(val))
    for i in range(val):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
