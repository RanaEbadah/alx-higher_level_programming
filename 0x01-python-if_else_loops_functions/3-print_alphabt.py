#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) in ('q', 'e'):
        continue
    else:
        print("{}".format(chr(letter)), end='')
