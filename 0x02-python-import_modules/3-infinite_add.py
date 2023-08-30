#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    val = 0
    for x in range(len(sys.argv) - 1):
        val += int(sys.argv[x + 1])
    print("{}".format(val))
