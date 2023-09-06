#!/usr/bin/python3
def uppercase(str):
    letterStr = ""
    i = 0
    for letter in str:
        if ord(letter) in range(97, 123):
            letterStr = chr(ord(letter) - 32)
        else:
            letterStr = letter
        if (i == len(str) - 1):
            print("{}".format(letterStr))
        else:
            print("{}".format(letterStr), end="")
        i += 1
