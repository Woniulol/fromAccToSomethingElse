#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/11 13:58
@user: jiananwang
@title: my_LinkedListDeque
"""


class DoubleLinkedListNode:
    def __init__(self, val):
        self.val: int = val
        self.next: DoubleLinkedListNode | None = None
        self.prev: DoubleLinkedListNode | None = None


class LinkedListDeque:
    def __init__(self):
        self.front: DoubleLinkedListNode | None = None
        self.rear: DoubleLinkedListNode | None = None
        self.__size: int = 0  # 双向队列的队列长度

    def get_size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.__size == 0

    def __push(self, val: int, is_front: bool):
        node = DoubleLinkedListNode(val=val)
        if self.__size == 0:
            self.front = node
            self.rear = node
        elif is_front:
            self.front.prev = node
            node.next = self.front
            self.front = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        self.__size += 1

    def push_first(self, num):
        """
        队首入队
        :param num:
        :return:
        """
        self.__push(val=num, is_front=True)

    def push_last(self, num):
        """
        队尾入队
        :param num:
        :return:
        """
        self.__push(val=num, is_front=False)

    def __pop(self, is_front: bool) -> int:
        if self.is_empty():
            raise IndexError("empty queue")
        elif is_front:
            num: int = self.front.val
            fnext: DoubleLinkedListNode | None = self.front.next
            if fnext is not None:
                fnext.prev = None
                self.front.next = None
            self.front = fnext
        else:
            num: int = self.rear.val
            fprev: DoubleLinkedListNode | None = self.rear.prev
            if fprev is not None:
                fprev.next = None
                self.rear.prev = None
            self.rear = fprev
        self.__size -= 1
        return num

    def pop_first(self) -> int:
        return self.__pop(is_front=True)

    def pop_last(self) -> int:
        return self.__pop(is_front=False)

    def __peek(self, is_front: bool) -> int:
        if self.is_empty():
            raise IndexError("empty queue")
        elif is_front:
            num = self.front.val
        else:
            num = self.rear.val
        return num

    def peek_first(self) -> int:
        return self.__peek(is_front=True)

    def peek_last(self) -> int:
        return self.__peek(is_front=False)

    def to_array(self) -> list[int]:
        node = self.front
        res = [0] * self.get_size()
        for i in range(self.get_size()):
            res[i] = node.val
            node = node.next
        return res


if __name__ == '__main__':
    myLinkedListDeque = LinkedListDeque()

    print(myLinkedListDeque.get_size())
    print(myLinkedListDeque.is_empty())

    for i in range(3):
        myLinkedListDeque.push_first(i)
        myLinkedListDeque.push_last(i)

    print(myLinkedListDeque.get_size())
    print(myLinkedListDeque.is_empty())
    print(myLinkedListDeque.peek_first())
    print(myLinkedListDeque.peek_last())

    print('---start pop---')
    myLinkedListDeque.pop_first()
    myLinkedListDeque.pop_last()

    print(myLinkedListDeque.get_size())
    print(myLinkedListDeque.is_empty())
    print(myLinkedListDeque.peek_first())
    print(myLinkedListDeque.peek_last())

    print(myLinkedListDeque.to_array())



