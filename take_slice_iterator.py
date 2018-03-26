#!/usr/bin/python3
# encoding:utf-8


import itertools


def count(start=1, end=0, step=1):
    num = start
    while True:
        if num >= end:
            break
        yield num
        num += step


def whileTrue(n):
    while True:
        yield n
        n += 1


c = count(1, 10)
for x in itertools.islice(c, 2, 5):
    print(x)

print(next(c))
