#!/usr/bin/python
# -*- coding: UTF-8 -*-


def y(list):
    for i in list:
        yield i


def exec(g):
    print(g)
    for i in g:
        print(i)


t = (123, 'xyz', 'zara', 'abc')
g = y(t)
exec(g)
