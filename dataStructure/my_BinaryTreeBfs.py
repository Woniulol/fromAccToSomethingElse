#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/12 13:41
@user: jiananwang
@title: my_BinaryTreeBfs
"""
from my_BinaryTree import TreeNode
from collections import deque


def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历"""
    # 初始化队列加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表用于保留遍历序列
    res = []
    while queue:
        # queue先进先出，把子节点append到后面并不会val添加到res的顺序
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保留节点值
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res


if __name__ == '__main__':
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    n6 = TreeNode(val=6)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6

    print(level_order(n1))
    print(level_order(n3))
