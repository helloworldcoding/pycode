#!/usr/bin/python3
# coding:utf-8

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

sortByFname = sorted(rows, key=itemgetter('fname'))
sortByUid = sorted(rows, key=itemgetter('uid'))
print(sortByFname)
print(sortByUid)
