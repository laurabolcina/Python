# coding=utf-8
__author__ = "Laura Bolčina"

import random

def lotto(n):
    """ Generates a list of n numbers, no duplicates """
    a = random.sample(range(1, 40), n)
    return a

if __name__ == "__main__":
    print lotto(7)