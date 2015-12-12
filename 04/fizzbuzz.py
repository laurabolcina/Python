# coding=utf-8
__author__ = "Laura Bolčina"

number = int(raw_input("Enter a number between 1 and 100: "))

for x in range(1, number + 1):
    if (x % 3 == 0) and (x % 5 == 0):
        print "fizzbuzz"
    elif x % 3 == 0:
        print "fizz"
    elif x % 5 == 0:
        print "buzz"
    else:
        print x