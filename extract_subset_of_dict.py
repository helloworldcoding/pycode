#!/usr/bin/python3
# coding: utf-8

prices = {
    'acme': 34.54,
    'apple': 88,
    'huawei': 100,
    'mi': 89,
    'ngx': 99
}

p1 = {key: value for key, value in prices.items() if value > 80}
print(p1)
p3 = dict((key, value) for key, value in prices.items() if value > 88)
print(p3)
