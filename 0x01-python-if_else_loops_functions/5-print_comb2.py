#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        numstr = '0' + str(num)
    else:
        numstr = str(num)
    if (num < 99):
        print("{}".format(numstr), end=", ")
    else:
        print("{}".format(numstr))
