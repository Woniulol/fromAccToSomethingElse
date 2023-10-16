#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/12 17:58
@user: jiananwang
@title: my_BinarySearchTree
"""


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


class ArrayBinaryTree:
    def __init__(self):
        self.__root: TreeNode | None = None
    pass

    def insert(self, num: int):
        """插入节点"""
        # 若树为空，则初始化根节点
        if self.__root is None:
            self.__root = TreeNode(num)
            return
        # 循环查找，越过叶节点后跳出
        cur, pre = self.__root, None
        while cur is not None:
            # 找到重复节点直接返回, 二叉搜索树不允许重复值
            if cur.val == num:
                return
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left
        # 插入节点（建立连接）
        node = TreeNode(num)  # 初始化一个节点对象
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node

    def search(self, num: int) -> TreeNode | None:
        """查找节点"""
        cur = self.__root
        while cur is not None:
            if cur.val < num:
                cur = cur.right
            elif cur.val > num:
                cur = cur.left
            else:
                break
        return cur

    def remove(self, num: int):
        """删除节点"""

        # 若树为空，直接提前返回
        if self.__root is None:
            return

        # 循环查找，越过叶节点后跳出
        cur, pre = self.__root, None
        while cur is not None:
            # 如果找到待删除节点，跳出循环
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left

        # 若无待删除节点，则直接返回
        if cur is None:
            return

        # 子节点数量 0 or 1
        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            # 删除节点cur
            if cur != self.__root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                # 若删除节点为根节点，则重新制定根节点
                self.__root = child
        # 子节点数量为2
        else:
            # 获取中序遍历中 cur的下一个节点
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            # 递归删除节点tmp
            self.remove(tmp.val)
            # 用tmp覆盖cur
            cur.val = tmp.val


if __name__ == '__main__':
    myArrayBinaryTree = ArrayBinaryTree()
    myArrayBinaryTree.insert(1)
    myArrayBinaryTree.insert(3)
    myArrayBinaryTree.insert(2)
    myArrayBinaryTree.insert(10)