#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numval = abs(number) % 10
if number < 0:
    numval = -numval
print("Last digit of {} is {} and is ".format(number, numval), end="")
if numval > 5:
    print("greater than 5")
elif numval == 0:
    print("0")
else:
    print("less than 6 and not 0")
