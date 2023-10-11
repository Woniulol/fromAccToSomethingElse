#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/11 14:59
@user: jiananwang
@title: my_ArrayDeque
"""


class ArrayDeque:
    def __init__(self, size: int):
        self.__nums: list[int] = [0] * size  # capacity
        self.__front: int = 0  # front position
        self.__size: int = 0  # queue size

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

    def index(self, i: int) -> int:
        """
        计算环形数组所以，通过取余操作实现数组首尾相连
        当i越过数组尾部后，回到头部
        当i雨过数组头部后，回到尾部
        :param i:
        :return:
        """
        return (i + self.capacity()) % self.capacity()

    def push_first(self, num: int):
        """
        队首入队
        :param num:
        :return:
        """
        if self.__size == self.capacity():
            raise IndexError("full capacity")
        self.__front = self.index(self.__front - 1)
        self.__nums[self.__front] = num
        self.__size += 1

    def push_last(self, num: int):
        """
        队尾入队
        :param num:
        :return:
        """
        if self.__size == self.capacity():
            raise IndexError("full capacity")
        rear = self.index(self.__front + self.__size)
        self.__nums[rear] = num
        self.__size += 1

    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError("empty queue")
        return self.__nums[self.__front]

    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError("empty queue")
        last = self.index(self.__front + self.__size - 1)
        return self.__nums[last]

    def pop_first(self) -> int:
        """
        队首出队
        :return:
        """
        num = self.peek_first()
        self.__front = self.index(self.__front + 1)
        self.__size -= 1
        return num

    def pop_last(self) -> int:
        """
        队尾出队
        :return:
        """
        num = self.peek_last()
        self.__size -= 1
        return num

    def to_array(self) -> list[int]:
        res = []
        for i in range(self.__size):
            res.append(self.__nums[self.index(self.__front + i)])
        return res


if __name__ == '__main__':
    myArrayDeque = ArrayDeque(10)

    print(myArrayDeque.get_size())
    print(myArrayDeque.is_empty())

    for i in range(3):
        myArrayDeque.push_first(i)
        myArrayDeque.push_last(i)

    print(myArrayDeque.get_size())
    print(myArrayDeque.is_empty())
    print(myArrayDeque.peek_first())
    print(myArrayDeque.peek_last())

    myArrayDeque.pop_first()
    myArrayDeque.pop_last()

    print(myArrayDeque.get_size())
    print(myArrayDeque.is_empty())
    print(myArrayDeque.peek_first())
    print(myArrayDeque.peek_last())

    print(myArrayDeque.to_array())





