#!/usr/bin/python3
# encoding:utf-8


def my_range(start, stop, increment=1):
    x = start
    while x < stop:
        yield x
        x += increment


my = my_range(1, 5)
print(next(my, None))
print(next(my, None))
print(next(my, None))
print(next(my, None))
print(next(my, None))
print(next(my, None))
print(next(my, None))
print(next(my, None))

for i in my_range(1, 10):
    print(i)
