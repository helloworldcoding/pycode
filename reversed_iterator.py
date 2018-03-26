#!/usr/bin/python3
# encoding:utf-8


class Countdown:

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for i in reversed(Countdown(4)):
    print(i)

for i in Countdown(4):
    print(i)
