#!/usr/bin/python3
# encoding:utf-8


"""
iter(object)
iter(object, sentinel)

Python官方文档对于这种形式的解释是：“ If the second argument,
sentinel, is given, then object must be a callable object.
The iterator created in this case will call object
with no arguments for each call to its __next__() method;
if the value returned is equal to sentinel,StopIteration will be raised,
otherwise the value will be returned.”。
"""


class counter:

    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end

    def get_next(self):
        s = self.start
        if(self.start <= self.end):
            self.start += 1
        else:
            raise StopIteration

        return s


count = counter(1, 10)
iterator = iter(count.get_next, 8)

print(type(iterator))
for item in iterator:
    print(item)
