#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/10 17:22
@user: jiananwang
@title: my_stack
"""
from my_LinkedList import ListNode


class LinkedListStack:
    def __init__(self):
        self.__peek: ListNode | None = None
        self.__size: int = 0

    def getSize(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return not self.__peek

    def push(self, val: int):
        """
        入栈，会在先实现一个ListNode实例，包含val值
        :param val: 新入栈的值
        :return:
        """
        node = ListNode(val=val)
        node.next = self.__peek
        # 先把__peek连接到node.next变成栈底，防止失去指针
        self.__peek = node
        # 再把新加入的node变成栈顶，保持peek状态
        self.__size += 1

    def peek(self) -> int:
        """
        访问栈顶元素
        :return:
        """
        if self.is_empty():
            raise IndexError('empty stack')
        return self.__peek.val

    def pop(self) -> int:
        """
        出栈
        :return: val of the top node
        """
        num = self.peek()
        # 先将__peek的值保存下来因为一会__peek会变
        self.__peek = self.__peek.next
        self.__size -= 1
        return num

    def to_list(self) -> list:
        """
        convert the stack to a list for visualization
        :return:
        """
        ls = []
        node = self.__peek
        while node:
            ls.append(node.val)
            # 不能用pop 不然convert完整个stack就没了 。。。 self.pop()
            node = node.next
        # ls.reverse()
        # 感觉不reverse更直观一点
        return ls


if __name__ == "__main__":
    myStack = LinkedListStack()
    print(myStack.is_empty())

    for i in range(10):
        myStack.push(i)

    print(myStack.is_empty())
    print(myStack.getSize())
    print(myStack.peek())

    myStack.pop()
    myStack.pop()
    myStack.pop()

    print(myStack.getSize())
    print(myStack.peek())

    print(myStack.to_list())




