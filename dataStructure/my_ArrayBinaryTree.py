#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/12 14:21
@user: jiananwang
@title: my_ArrayBinaryTree
"""


class ArrayBinaryTree:
    """使用数组表示的二叉树类"""
    """
    每个索引位置存放的不是TreeNode!!!
    通过直接计算索引的到左右和父节点
    """

    def __init__(self, arr: list[int | None]):
        self.__tree = list(arr)

    def size(self):
        """节点数量"""
        return len(self.__tree)

    def val(self, i: int) -> int | None:
        """获取索引为i的节点的val"""
        # 若索引越界则返回None，表示空位
        if i < 0 or i >= self.size():
            return None
        return self.__tree[i]

    def left(self, i: int) -> int:
        """获取索引为i节点的左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """获取索引为i节点的右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取索引为i节点的父节点的索引"""
        return (i - 1) % 2  # 这里计算的是索引值

    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        """
        直接遍历数组
        数组存储二叉树的层序遍历顺序和遍历数组的顺序是一致的
        """
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def __dfs(self, i: int, order: str):
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == "pre":
            self.res.append(self.val(i))
        self.__dfs(self.left(i), order)
        # 中序遍历
        if order == 'in':
            self.res.append(self.val(i))
        self.__dfs(self.right(i), order)
        # 后续遍历
        if order == 'post':
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        """前序遍历"""
        self.res = []
        self.__dfs(0, order='pre')
        return self.res

    def in_order(self) -> list[int]:
        """中序遍历"""
        self.res = []
        self.__dfs(0, order='in')
        return self.res

    def post_order(self) -> list[int]:
        """后序遍历"""
        self.res = []
        self.__dfs(0, order='post')
        return self.res


if __name__ == '__main__':
    myArrayBinaryTree = ArrayBinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(myArrayBinaryTree.level_order())
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(myArrayBinaryTree.pre_order())
    # [1, 2, 4, 8, 9, 5, 10, 3, 6, 7]
    print(myArrayBinaryTree.in_order())
    # [8, 4, 9, 2, 10, 5, 1, 6, 3, 7]
    print(myArrayBinaryTree.post_order())
    # [8, 9, 4, 10, 5, 2, 6, 7, 3, 1]

