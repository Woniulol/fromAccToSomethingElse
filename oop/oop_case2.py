#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/14 19:59
@user: jiananwang
@title: oop_case2
"""


# 做一个计算器，实现基本的加减乘除运算，以及打印结果


# def jia(n1, n2):
#     return n1 + n2
#
#
# def jian(n1, n2):
#     return n1 - n2
#
#
# def cheng(n1, n2):
#     return n1 * n2
#
#
# res = jia(2, 4)
# res2 = cheng(5, 7)
# print(res)
# print(res2)
#
# # 计算下面的表达式
# # (2 + 6 - 4) * 5
#
# r1 = jia(2, 6)
# r2 = jian(r1, 4)
# r3 = cheng(r2, 5)
# print(r3)

# 现在的问题是代码在进行连续运算的时候很复杂
############################################################

# result = 0
#
#
# def first_value(v):
#     global result
#     result = v
#
#
# def jia(n):
#     global result
#     result += n
#
#
# def jian(n):
#     global result
#     result -= n
#
#
# def cheng(n):
#     global result
#     result *= n
#
#
# # (2 + 6 - 4) * 5
#
# first_value(2)
# jia(6)
# jian(4)
# cheng(5)
# print(result)


# 现在的问题是他是一个全局变量，特别不安全
# 代码很散
############################################################

# class Calculator:
#     __result = 0
#
#     @classmethod
#     def first_value(cls, v):
#         cls.__result = v
#
#     @classmethod
#     def jia(cls, n):
#         cls.__result += n
#
#     @classmethod
#     def jian(cls, n):
#         cls.__result -= n
#
#     @classmethod
#     def cheng(cls, n):
#         cls.__result *= n
#
#     @classmethod
#     def show(cls):
#         print(f'result is {cls.__result}')
#
#
# Calculator.first_value(2)
# Calculator.jia(6)
# Calculator.jian(4)
# Calculator.cheng(5)
#
# Calculator.show()

# 还是有问题
# 类对象只存在一份，无法同时进行多个Calculator的计算过程
# e.g. import进不同的file调用同一个类会相互干扰

############################################################

# class Calculator:
#     def check_num(self, num):
#         if not isinstance(num, int):
#             raise TypeError("num is not an int")
#
#     def __init__(self, num):
#         self.check_num(num)
#         self.__result = num
#
#     def jia(self, n):
#         self.check_num(n)
#         self.__result += n
#
#     def jian(self, n):
#         self.check_num(n)
#         self.__result -= n
#
#     def cheng(self, n):
#         self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print(f'result {self.__result}')
#
#
# c1 = Calculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

# 现在的问题是破坏了代码的单一指责
# 一个方法即负责数据验证又负责计算
############################################################

class Calculator:
    @staticmethod
    def __check_num_zsq(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError("num is not an int")
            return func(self, n)

        return inner

    @__check_num_zsq
    def __init__(self, num):
        self.__result = num

    @__check_num_zsq
    def jia(self, n):
        self.__result += n

    @__check_num_zsq
    def jian(self, n):
        self.__result -= n

    @__check_num_zsq
    def cheng(self, n):
        self.__result *= n

    def show(self):
        print(f'result {self.__result}')


c1 = Calculator(2)
c1.jia(6)
c1.jian(4)
c1.cheng(5)
c1.show()
