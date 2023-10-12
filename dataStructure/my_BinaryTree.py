#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/12 13:34
@user: jiananwang
@title: my_binary_tree
"""


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


if __name__ == '__main__':
    # 初始化二叉树
    # 初始化节点
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)

    # 构建引用指向（指针）
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
