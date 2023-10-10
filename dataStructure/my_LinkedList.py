#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/9/23 14:33
@user: jiananwang
@title: my_linked_list
"""


class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        # value of a node
        self.next: ListNode | None = None
        # pointer to the next node

    def __str__(self):
        return str(self.val)


def insert(n0: ListNode, P: ListNode):
    """
    :param n0: existing node, an ListNode instance
    :param P: node insterted after n0, an ListNode instance
    :return: None
    """
    P.next = n0.next
    n0.next = P


def remove(n0: ListNode):
    """
    remove the first node after n0
    it seems to be quite difficult to remove a specific Node as you need to get the privous Node first
    :param n0: an ListNode instance
    :return: None
    """
    n0.next = n0.next.next


def access(head: ListNode, index: int) -> ListNode | None:
    """
    访问链表中索引为index的节点
    index为0返回的就是起始节点本身
    :param head: 起始节点 ListNode instance
    :param index: index
    :return: ListNode
    """
    target_node = head
    for i in range(index):
        target_node = target_node.next
    return target_node


def find(head: ListNode, target_value: int) -> int:
    """
    遍历列表，选择第一个值为target_value的节点，返回该节点的index
    :param head: 头节点
    :param target_value:
    :return: index int
    """
    index = 0
    while head:
        if head.val == target_value:
            return index
        head = head.next
        index += 1
    return -1


if __name__ == '__main__':

    # 初始化节点对象
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    # 构建引用指向关系
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(access(n1, 1))
    print(find(n0, 4))
