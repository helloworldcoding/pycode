#!/usr/bin/python3
# encoding:utf-8

values = [1, 2, 4, '3', '-', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


int_vals = list(filter(is_int, values))
print(int_vals)
