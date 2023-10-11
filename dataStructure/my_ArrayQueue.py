#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/11 13:19
@user: jiananwang
@title: my_ArrayQueue
"""


class ArrayQueue:
    def __init__(self, size: int):
        self.__nums: list[int] = [0] * size  # 数组长度
        self.__front: int = 0  # 队首指针
        self.__size: int = 0  # 队列长度

    def capacity(self) -> int:
        """
        返回数组长度，而不是队列长度
        :return:
        """
        return len(self.__nums)

    def get_size(self) -> int:
        """
        返回队列长度
        :return:
        """
        return self.__size

    def is_empty(self) -> bool:
        return self.__size == 0

    def push(self, num: int):
        if self.__size == self.capacity():
            raise IndexError("capacity full")

        rear: int = (self.__front + self.__size) % self.capacity()
        # 通过取余操作实现环形数组
        self.__nums[rear] = num
        self.__size += 1

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('empty queue')
        return self.__nums[self.__front]

    def pop(self) -> int:
        num: int = self.peek()
        self.__front = (self.__front + 1) % self.capacity()
        self.__size -= 1
        return num

    def to_list(self) -> list[int]:
        ls = [0] * self.get_size()
        for i in range(self.__size):
            ls[i] = self.__nums[(self.__front % self.capacity())]
            self.__front += 1
        return ls


if __name__ == '__main__':
    myArrayQueue = ArrayQueue(5)

    print(myArrayQueue.get_size())
    print(myArrayQueue.is_empty())

    for i in range(5):
        myArrayQueue.push(i)

    print(myArrayQueue.get_size())
    print(myArrayQueue.is_empty())
    print(myArrayQueue.peek())

    myArrayQueue.pop()
    myArrayQueue.pop()
    myArrayQueue.pop()

    print(myArrayQueue.get_size())
    print(myArrayQueue.is_empty())
    print(myArrayQueue.peek())

    print(myArrayQueue.to_list())
