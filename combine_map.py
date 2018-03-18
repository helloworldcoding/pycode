#!/usr/bin/python3
# encoding:utf-8

from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': '2', 'z': 4}
d = {'dd': 'lll'}

c = ChainMap(a, b, d)
print(c)
print(len(c))
c['x'] = 'a'
c['y'] = 'y'
c['z'] = 'z'
del c['y']  # 对c的增删改查，都是针对a进行的
print(a)
print(b)
print(c)

c = c.new_child()
c['child'] = 'first_child'

print(c)
print(c.parents)
