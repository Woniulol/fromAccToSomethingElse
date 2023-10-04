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
        self.next: ListNode | None = None


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n4 = ListNode(5)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
