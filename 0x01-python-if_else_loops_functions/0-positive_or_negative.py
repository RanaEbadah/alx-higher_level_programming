#!/usr/bin/python3
import random
number = random.randint(-10, 10)
numStatus = ""
if number > 0:
    numStatus = "is positive"
elif number == 0:
    numStatus = "is zero"
else:
    numStatus = "is negative"
print("{} {}".format(number, numStatus))
