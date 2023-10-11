#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/11 12:56
@user: jiananwang
@title: my_Queue
"""
from my_LinkedList import ListNode


class LinkedListQueue:
    def __init__(self):
        self.__front: ListNode | None = None
        self.__rear: ListNode | None = None
        self.__size: int = 0

    def get_size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return not self.__front

    def push(self, val: int):
        node = ListNode(val)

        if self.is_empty():
            self.__front = node
            self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = node

        self.__size += 1

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("empty queue")
        return self.__front.val

    def pop(self) -> int:
        num = self.peek()
        self.__front = self.__front.next
        self.__size -= 1
        return num

    def to_list(self) -> list[int]:
        ls = []
        while self.__front:
            ls.append(self.__front.val)
            self.__front = self.__front.next
        return ls


if __name__ == '__main__':
    myLinkedListQueue = LinkedListQueue()

    print(myLinkedListQueue.get_size())
    print(myLinkedListQueue.is_empty())

    for i in range(10):
        myLinkedListQueue.push(i)

    print(myLinkedListQueue.get_size())
    print(myLinkedListQueue.is_empty())
    print(myLinkedListQueue.peek())

    myLinkedListQueue.pop()
    myLinkedListQueue.pop()
    myLinkedListQueue.pop()

    print(myLinkedListQueue.get_size())
    print(myLinkedListQueue.is_empty())
    print(myLinkedListQueue.peek())

    print(myLinkedListQueue.to_list())



