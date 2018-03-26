#!/usr/bin/python3
# encoding:utf-8

"""
你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。
你想直接在你的这个新容器对象上执行迭代操作。

定义一个__iter__()方法，将迭代操作代理到容器内部的对象上去。
"""


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        # return 'Node({0})'.format(self._value)
        # '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr())
        # 可以用于在格式化某个值之前对其进行转化:
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    gradeFather = Node(1)
    father = Node(11)
    uncol = Node(12)
    lisi = Node(111)
    zhangsan = Node(121)
    father.add_child(lisi)
    uncol.add_child(zhangsan)
    gradeFather.add_child(father)
    gradeFather.add_child(uncol)

    for child in gradeFather:
        print(child)
        for c in child:
            print(c)
