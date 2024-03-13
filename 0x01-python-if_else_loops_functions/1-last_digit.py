#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num = number % 10
else:
    num = (number * -1) % 10
    num = num * -1

myStr = ""
if num > 5:
    myStr = "and is greater than 5"
elif num == 0:
    myStr = "and is 0"
elif num < 6 and num != 0:
    myStr = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, num, myStr))
