#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """list_of_integers: list of integers to find the peak.
    Returns: the peak or None"""
    if len(list_of_integers) == 0:
        return None
    else:
        peak = list_of_integers[0]
        for i in range(0, len(list_of_integers - 1)):
            if i > peak:
                peak = i
        return peak
