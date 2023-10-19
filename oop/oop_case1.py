#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/13 15:49
@user: jiananwang
@title: oop_case1
"""
import sys


# 实现一个Person类，打印当前时刻由这个Person类产生的实例有多少个
# 创建了一个 +1 删除了一个 -1

class Person:

    __personCount = 0

    def __init__(self):
        Person.__personCount += 1
        print('计数+1')

    def __del__(self):
        Person.__personCount -= 1
        print('计数-1')

    @classmethod
    def log(cls):
        print(f"当前人的个数是{cls.__personCount}")


p1 = Person()
p2 = Person()
p3 = Person()
del p1
p4 = Person()
p5 = Person()

Person.log()

print(sys.getrefcount(p2))
