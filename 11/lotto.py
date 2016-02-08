# coding=utf-8
__author__ = "Laura Bolčina"

from random import randint

def lotto(n):
    """ Returns n random lotto numbers."""
    lotto_numbers = []
    while True:
        x = randint(1, 39)  # assuming lotto numbers go from 1 to 39
        if x not in lotto_numbers:
            lotto_numbers.append(x)
        else:
            continue
        if len(lotto_numbers) == n:  # this is called loop-and-a-half; while loop continues to run until this happens
            break
    return lotto_numbers