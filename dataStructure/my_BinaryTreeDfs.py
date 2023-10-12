#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/12 13:58
@user: jiananwang
@title: my_BinaryTreeDfs
"""
from my_BinaryTree import TreeNode


def pre_order(root: TreeNode | None):
    """前序遍历"""
    res = []
    if root is None:
        return
    # 访问优先级： 根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: TreeNode | None):
    """中序遍历"""
    res = []
    if root is None:
        return
    # 访问优先级： 左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)


def post_order(root: TreeNode | None):
    """后续遍历"""
    res = []
    if root is None:
        return
    # 访问优先级： 左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)