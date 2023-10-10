#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/10 17:57
@user: jiananwang
@title: my_ArrayStack
"""


class ArrayStack:
    def __init__(self):
        self.__stack: list[int] = []
        # 在内部以一个动态数组的方式进行维护

    def getSize(self):
        return len(self.__stack)

    def is_empty(self):
        return self.__stack == []

    def push(self, item: int):
        self.__stack.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("empty")
        return self.__stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("empty")
        return self.__stack[-1]

    def to_list(self):
        ls = self.__stack
        ls.reverse()
        return ls


if __name__ == '__main__':

    myArrayStack = ArrayStack()

    print(myArrayStack.is_empty())
    print(myArrayStack.getSize())

    for i in range(10):
        myArrayStack.push(i)

    print(myArrayStack.is_empty())
    print(myArrayStack.getSize())
    print(myArrayStack.peek())

    myArrayStack.pop()
    myArrayStack.pop()
    myArrayStack.pop()

    print(myArrayStack.is_empty())
    print(myArrayStack.getSize())
    print(myArrayStack.peek())

    print(myArrayStack.to_list())



