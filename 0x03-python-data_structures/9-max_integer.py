#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for x in range(0, len(my_list)):
            if x == 0:
                max = my_list[x]
            else:
                if my_list[x] > max:
                    max = my_list[x]
    return max
