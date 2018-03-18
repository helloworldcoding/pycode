#!/usr/bin/python3
# encoding:utf-8


from collections import namedtuple

recodes = [
    ('zhagnsna', '12', '7'),
    ('lisi', '10', '8'),
    ('wangwu', '12', '7')
]

Student = namedtuple('Student', ['name', 'type_nump', 'size'])


def total_num(recodes):
    total = 0
    for recode in recodes:
        stu = Student(*recode)
        total += int(stu.type_nump) * int(stu.size)
    return total


print(total_num(recodes))
